"""module to read cockatrice replays and convert them to json

commandline usage:
    python -m crow.replay (convert | create) <input_file> <output_file>

convert: read a replay (.cor) input_file and convert it to a json output_file
create: read a json input_file and create a replay (.cor) output_file from it
"""
from google.protobuf import json_format

from . import protocol


def read_replay(replay):
    """create a protobuf replay object from serialized string

    replay: string representation of a replay
    returns a protobuf replay object
    """
    obj = protocol.GameReplay.FromString(replay)
    return obj


def open_replay(file):
    """open a file and create a protobuf replay object

    file: name of a cockatrice replay file
    returns a protobuf replay object
    """
    with open(file, "rb") as fp:
        return read_replay(fp.read())


def replay_to_json(replay):
    """convert a replay object to json string"""
    # preserving field names is not required but stops it from converting the
    # original snake cased names to camel case in the output
    return json_format.MessageToJson(replay, preserving_proto_field_name=True)


def json_to_replay(json):
    """convert a json string to a replay object"""
    return json_format.Parse(json, protocol.GameReplay())


def convert_to_json(input_file, output_file):
    """read a replay (.cor) input_file and convert it to a json output_file

    input_file: path to replay (.cor) file
    output_file: path to place the created json, output is clobbered
    """
    replay = open_replay(input_file)
    json = replay_to_json(replay)
    with open(output_file, "w") as fp:
        fp.write(json)


def create_from_json(input_file, output_file):
    """read a json input_file and create a replay (.cor) output_file from it

    input_file: path to json file
    output_file: path to place the created replay, output is clobbered
    """
    with open(input_file) as fp:
        json = fp.read()

    replay = json_to_replay(json)
    replaystr = replay.SerializeToString()
    with open(output_file, "wb") as fp:
        fp.write(replaystr)


def _usage_print():
    import sys

    print("error: invalid commandline arguments!\n", file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def _main(args):
    try:
        cmd, file, output = args
    except ValueError:
        _usage_print()

    if cmd == "convert":
        convert_to_json(file, output)
    elif cmd == "create":
        create_from_json(file, output)
    else:
        _usage_print()


if __name__ == "__main__":
    import sys

    _main(sys.argv[1:])
