import asyncio

from . import connection
from . import handler
from . import passwordhasher
from . import protocol


class ServerError(Exception):
    def __init__(self, response):
        self.response = response
        self.code = response.response_code
        self.name = protocol.Response.ResponseCode.Name(self.code)
        Exception.__init__(self, f"received error response: {self.name}")


class crow:
    def __init__(self, url, username, password=None, ping_time=5):
        self.url = url
        self.username = username
        self.clientid = f"crow_{username}"
        self.password = password
        self.ping_time = ping_time
        self._client = protocol.client()
        self._handler = handler.handler()
        self._connection = connection.connection(self._handler)

    async def register(self, email: str, country: str = None, real_name: str = None) -> bool:
        """
        Register the username to the server. This action will replace and then close any websocket
        currently open for this instance. It is recommended to not use the same instance to register
        and login.

        :param str email: Email address to be registered. Mandatory.
        :param str country: 2 letters country code in ISO format (default: None).
        :param str real_name: User's real name (default: None).
        :rtype: bool
        :raise ValueError: If ``self.password`` or ``email`` is None.
        :raise ServerError: If any error other than the email requiring verification occurs.
        :return: ``True`` if the registration was completed, ``False`` if the email address must be verified.
        """
        if self.password is None:
            raise ValueError("password cannot be None.")
        if email is None:
            raise ValueError("email cannot be None.")

        await self._connection.connect(self.url)
        self._client.reset()

        kwargs = {'email': email}
        if country is not None:
            kwargs['country'] = country
        if real_name is not None:
            kwargs['real_name'] = real_name

        try:
            await self.send_command(
                protocol.session_commands.register,
                user_name=self.username,
                clientid=self.clientid,
                password=self.password,
                **kwargs,
            )
        except ServerError as e:
            self._connection.close()
            if e.name == 'RespRegistrationAcceptedNeedsActivation':
                return False
            else:
                raise
        else:
            self._connection.close()
            return True

    async def login(self):
        await self._connection.connect(self.url)
        self._client.reset()
        kwargs = {}
        if self.password is not None:
            resp = await self.send_command(
                protocol.session_commands.get_salt, user_name=self.username
            )
            salt = resp.Extensions[protocol.password_salt_ext].password_salt
            hashed = passwordhasher.compute_hash(self.password, salt)
            kwargs["hashed_password"] = hashed

        try:
            await self.send_command(
                protocol.session_commands.login,
                user_name=self.username,
                clientid=self.clientid,
                **kwargs,
            )
        except ServerError:
            self._connection.close()
            raise

        self._ping_task = asyncio.create_task(self._ping_loop())

    async def send_command(self, command, *args, **kwargs):
        msg_bytes, msg_id = self._client.build(command, *args, **kwargs)
        await self._connection.send(msg_bytes)
        resp = await self._handler.get_response(msg_id)
        if resp.response_code != protocol.Response.RespOk:
            raise ServerError(resp)

        return resp

    async def _ping_loop(self):
        while self._connection.is_connected:
            await asyncio.sleep(self.ping_time)
            await self.send_command(protocol.session_commands.ping)

    async def send_message(self, user, message):
        await self.send_command(
            protocol.session_commands.message,
            user_name=user,
            message=message,
        )

    async def stop(self):
        self._ping_task.cancel()
        self._connection.close()
