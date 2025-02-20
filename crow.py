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
