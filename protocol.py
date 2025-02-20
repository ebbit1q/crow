import collections

from . import pb

session_commands = collections.namedtuple("session_commands", ["login"])(
    pb.session_commands_pb2.Command_Login
)
GameReplay = pb.game_replay_pb2.GameReplay
Response = pb.response_pb2.Response
EVENT = pb.server_message_pb2.ServerMessage.SESSION_EVENT
SERVER_RESPONSE = pb.server_message_pb2.ServerMessage.RESPONSE


def parse_server_message(msg):
    got = pb.server_message_pb2.ServerMessage.FromString(bytes(msg))
    return got


def parse_client_message(msg):
    got = pb.commands_pb2.CommandContainer.FromString(bytes(msg))
    return got


class client:
    def __init__(self):
        self.message_id = 1

    def build(self, command, **kwargs):
        obj = command()
        for key, value in kwargs.items():
            setattr(obj, key, value)

        if command in session_commands:
            return self.build_session_cmd(obj)

    def build_session_cmd(self, command):
        container = pb.commands_pb2.CommandContainer()
        cmd = container.session_command.add()
        new = cmd.Extensions[command.ext]
        new.MergeFrom(command)
        message_id = self.message_id
        self.message_id += 1
        container.cmd_id = message_id
        return container.SerializeToString(), message_id
