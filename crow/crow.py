import asyncio

from . import connection, handler, passwordhasher, protocol


class ServerError(Exception):
    """ServerError is raised when the server sends an error response."""

    def __init__(self, response):
        """Iinitialise a server error.

        Args:
            response: The protocol response object.
        """
        self.response = response
        self.code = response.response_code
        self.name = protocol.Response.ResponseCode.Name(self.code)
        Exception.__init__(self, f"received error response: {self.name}")


class RegistrationNeedsActivation(Exception):
    """RegistrationNeedsActivation is raised when activation is needed.

    The server can require new accounts to activate theri account before use,
    generally through an email code.
    """



class crow:
    """crow implements the cockatrice protocol as a client"""

    def __init__(
        self,
        url: str,
        username: str,
        password: str | None = None,
        ping_time: int = 5,
    ):
        """Initializes a Crow instance

        Args:
            url: The websocket url to connect to, eg ws://example.com
            username: The username to connect with.
            password: The password to connect with.
            ping_time: The frequency that pings are sent to the server to keep
                the connection live
        """
        self.url = url
        self.username = username
        self.clientid = f"crow_{username}"
        self.password = password
        self.ping_time = ping_time
        self._client = protocol.client()
        self._handler = handler.handler()
        self._connection = connection.connection(self._handler)

    async def register(
        self,
        email: str | None = None,
        password: str | None = None,
        country: str | None = None,
        real_name: str | None = None,
    ):
        """Register the username to the server.

        This action will replace and then close any websocket currently open
        for this instance.

        Args:
            email: Email address to be registered.
            password: Password to register, if not provided earlier.
            country: 2 letter country code in ISO format.
            real_name: User's real name.

        Raises:
            ValueError: If password is not provided
            RegistrationNeedsActivation: When the account needs activation.
            ServerError: When the server sends an error response.
        """
        if password is not None:
            self.password = password

        if self.password is None:
            raise ValueError("a password is required to register")

        await self._connection.connect(self.url)
        self._client.reset()

        kwargs = {}
        if email is not None:
            kwargs["email"] = email

        if country is not None:
            kwargs["country"] = country

        if real_name is not None:
            kwargs["real_name"] = real_name

        try:
            await self.send_command(
                protocol.session_commands.register,
                user_name=self.username,
                clientid=self.clientid,
                password=self.password,
                **kwargs,
            )
        finally:
            self._connection.close()

    async def login(self):
        """Log in to the server.

        Uses the provided information to start the connection and
        authenticate.

        Raises:
            ServerError: When the server sends an error response.
        """
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
        """Send a command to the server.

        Args:
            command: Protocol command to send.
            other args are used to construct the command.

        Returns:
            The response from the server.

        Raises:
            ServerError: When the server sends an error response.
        """
        msg_bytes, msg_id = self._client.build(command, *args, **kwargs)
        await self._connection.send(msg_bytes)
        resp = await self._handler.get_response(msg_id)
        match resp.response_code:
            case protocol.Response.RespOk:
                pass
            case protocol.Response.RespRegistrationAcceptedNeedsActivation:
                raise RegistrationNeedsActivation()
            case _:
                raise ServerError(resp)

        return resp

    async def _ping_loop(self):
        while self._connection.is_connected:
            await asyncio.sleep(self.ping_time)
            await self.send_command(protocol.session_commands.ping)

    async def send_message(self, user: str, message: str):
        """Send a direct message to a user on the server.

        Args:
            user: The username to send the message to.
            message: The text to send.

        Raises:
            ServerError: When the server sends an error response.
        """
        await self.send_command(
            protocol.session_commands.message,
            user_name=user,
            message=message,
        )

    async def stop(self):
        """Stop the current tasks and disconnect from the server."""
        try:
            self._ping_task.cancel()
        except AttributeError:
            pass

        self._connection.close()
