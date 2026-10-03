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

    # TODO: Return a more descriptive enum, e.g. ReigstrationResult.OK, RegistrationResult.NEEDS_ACTIVATION
    #  and RegistrationResult.REGISTRATION_DISABLED
    @staticmethod
    async def register(
        url: str,
        username: str,
        password: str,
        email: str | None = None,
        country: str | None = None,
        real_name: str | None = None,
    ):
        """Register the username to the server.

        This action will replace and then close any websocket currently open
        for this instance.

        Args:
            url: The websocket url to connect to, e.g. ws://example.com
            username: The username to register with.
            password: The password to register with.
            email: The email address to be registered. It may not be mandatory based on the server's configuration.
            country: A 2-letter country code in ISO format. Optional.
            real_name: The user's real name. Optional.

        Returns:
            ``True`` if the registration was successful, ``False`` if the emails needs to be confirmed and the account needs
                to be activated

        Raises:
            ValueError: If username, password and/or url are not provided.
            ServerError: If the server sends an error response.
        """
        if url is None:
            raise ValueError(
                "The server's WebSocket URL is required to register."
            )
        if username is None:
            raise ValueError("A username is required to register.")
        if password is None:
            raise ValueError("A password is required to register.")

        registration_client = protocol.client()
        registration_handler = handler.handler()
        registration_connection = connection.connection(registration_handler)

        await registration_connection.connect(url)
        registration_client.reset()

        kwargs = {}
        if email is not None:
            kwargs["email"] = email
        if country is not None:
            kwargs["country"] = country
        if real_name is not None:
            kwargs["real_name"] = real_name

        try:
            msg_bytes, msg_id = registration_client.build(
                protocol.session_commands.register,
                user_name=username,
                clientid=f"crow_{username}",
                password=password,
                **kwargs,
            )
            await registration_connection.send(msg_bytes)
            resp = await registration_handler.get_response(msg_id)
        finally:
            registration_connection.close()

        match resp.response_code:
            case protocol.Response.RespRegistrationAccepted:
                return True
            case protocol.Response.RespRegistrationAcceptedNeedsActivation:
                return False
            case _:
                raise ServerError(resp)

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
        # TODO: Cleanup this match statement
        match resp.response_code:
            case protocol.Response.RespOk:
                pass
            case protocol.Response.RespRegistrationAcceptedNeedsActivation:
                pass
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
