from . import connection
from . import protocol
from . import handler


class ServerError(Exception):
    def __init__(self, code):
        self.code = code
        self.name = protocol.Response.ResponseCode.Name(code)
        Exception.__init__(self, f"received error response: {self.name}")


class crow:
    def __init__(self, url, username, password=None):
        self.url = url
        self.username = username
        self.clientid = f"crow_{username}"
        self.password = password
        self._client = protocol.client()
        self._handler = handler.handler()
        self._connection = connection.connection(self._handler)

    async def login(self):
        await self._connection.connect(self.url)
        msg_bytes, msg_id = self._client.build(
            protocol.session_commands.login,
            user_name=self.username,
            clientid=self.clientid,
        )
        await self._connection.send(msg_bytes)
        response_code = await self._handler.get_response(msg_id)
        if response_code != protocol.Response.RespOk:
            raise ServerError(response_code)

    async def stop(self):
        self._connection.close()
