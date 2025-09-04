import time
from enum import Enum

from faker import Faker
import os


class TestServer:
    """
    An interface to run fully configured testatrice instances in podman containers.
    It relies on the environment variable ``TESTATRICE_HOME`` to find testatrice's deployment script.
    Server identifier and exposed ports are decided at runtime.

    :ivar IDENTIFIER: The randomly chosen server identifier.
    :ivar TCP_PORT: The exposed TCP socket port the server listens to.
    :ivar URL: The full websocket URL to connect to the server, in the form ``ws://localhost:[port]``.
    """

    _USED_PORTS: set[int] = {1110, 1111}
    _USED_IDENTIFIERS: set[str] = set()
    _TEST_SERVERS: set = set()
    _TESTATRICE_DIR: str = os.environ["TESTATRICE_HOME"]

    class AuthenticationMethod(Enum):
        NONE = "none"
        PASSWORD = "password"
        SQL = "sql"

    class RoomMethod(Enum):
        CONFIG = "config"
        SQL = "sql"

    @staticmethod
    def stop_all() -> None:
        """
        Stops all known testatrice server instances, testatrice-database and testatrice-mailserver.
        """
        test_servers = set(TestServer._TEST_SERVERS)

        for test_server in test_servers:
            test_server.stop()

        os.system(f"podman stop testatrice-mailserver > /dev/null")
        os.system(f"podman stop testatrice-database > /dev/null")

    @staticmethod
    def _create_identifier() -> str:
        fake = Faker()
        identifier = fake.word()

        while identifier in TestServer._USED_IDENTIFIERS:
            identifier = fake.word()

        TestServer._USED_IDENTIFIERS.add(identifier)

        return identifier

    @staticmethod
    def _get_port() -> int:
        port = 4747
        while port in TestServer._USED_PORTS:
            port += 1

        TestServer._USED_PORTS.add(port)
        return port

    def __init__(
        self,
        require_client_id: bool = False,
        required_features: str = "''",
        idle_client_timeout: int = 3600,
        authentication_method: AuthenticationMethod = AuthenticationMethod.SQL,
        password: str = "password",
        enable_registration: bool = False,
        require_registration: bool = False,
        require_activation: bool = False,
        max_accounts_per_email: int = 2,
        enable_forgot_password: bool = True,
        forgot_password_token_life: bool = 60,
        enable_forgot_password_challenge: bool = False,
        password_min_length: int = 6,
        username_min_length: int = 6,
        username_max_length=12,
        username_disallow_lowercase: bool = False,
        username_disallow_uppercase: bool = False,
        username_disallow_numerics: bool = False,
        allowed_punctuation: str = "''",
        allow_punctuation_prefix: bool = False,
        room_method: RoomMethod = RoomMethod.CONFIG,
        max_game_inactivity_time: int = 120,
        log_path: str = "./logs",
    ):
        self._require_client_id: bool = require_client_id
        self._required_features: str = required_features
        self._idle_client_timeout: int = idle_client_timeout
        self._authentication_method: TestServer.AuthenticationMethod = (
            authentication_method
        )
        self._password: str = password
        self._enable_registration: bool = enable_registration
        self._require_registration: bool = require_registration
        self._require_activation: bool = require_activation
        self._max_accounts_per_email: int = max_accounts_per_email
        self._enable_forgot_password: bool = enable_forgot_password
        self._forgot_password_token_life: int = forgot_password_token_life
        self._enable_forgot_password_challenge: bool = (
            enable_forgot_password_challenge
        )
        self._password_min_length: int = password_min_length
        self._username_min_length: int = username_min_length
        self._username_max_length: int = username_max_length
        self._username_disallow_lowercase: bool = username_disallow_lowercase
        self._username_disallow_uppercase: bool = username_disallow_uppercase
        self._username_disallow_numerics: bool = username_disallow_numerics
        self._allowed_punctuation: str = allowed_punctuation
        self._allow_punctuation_prefix: bool = allow_punctuation_prefix
        self._room_method: TestServer.RoomMethod = room_method
        self._max_game_inactivity_time: int = max_game_inactivity_time
        self._log_path: str = log_path

        self.IDENTIFIER: str = TestServer._create_identifier()
        self.TCP_PORT: int = TestServer._get_port()
        self._websocket_port: int = TestServer._get_port()

        TestServer._TEST_SERVERS.add(self)

        self.URL: str = f"ws://localhost:{self._websocket_port}"

        self._command = self._generate_command()

    def _generate_command(self):
        command: str = (
            f"./testatrice.sh -s {self.IDENTIFIER} --tcp {self.TCP_PORT} --websocket {self._websocket_port}"
        )

        if self._require_client_id:
            command += " --require-client-id"

        if self._required_features is not None:
            command += f" --required-features {self._required_features}"

        if self._idle_client_timeout is not None:
            command += f" --idle-client-timeout {self._idle_client_timeout}"

        if self._authentication_method is not None:
            command += (
                f" --authentication-method {self._authentication_method.value}"
            )

        if self._password is not None:
            command += f" --password {self._password}"

        if self._enable_registration:
            command += " --enable-registration"

        if self._require_registration:
            command += " --require-registration"

        if self._require_activation:
            command += " --require-activation"

        if self._max_accounts_per_email is not None:
            command += (
                f" --max-accounts-per-email {self._max_accounts_per_email}"
            )

        if self._enable_forgot_password:
            command += " --enable-forgot-password"

        if self._forgot_password_token_life is not None:
            command += f" --forgot-password-token-life {self._forgot_password_token_life}"

        if self._enable_forgot_password_challenge:
            command += " --enable-forgot-password-challenge"

        if self._password_min_length is not None:
            command += f" --password-min-length {self._password_min_length}"

        if self._username_min_length is not None:
            command += f" --username-min-length {self._username_min_length}"

        if self._username_max_length is not None:
            command += f" --username-max-length {self._username_max_length}"

        if self._username_disallow_lowercase:
            command += " --username-disallow-lowercase"

        if self._username_disallow_uppercase:
            command += " --username-disallow-uppercase"

        if self._username_disallow_numerics:
            command += " --username-disallow-numerics"

        if self._allowed_punctuation is not None:
            command += f" --allowed-punctuation {self._allowed_punctuation}"

        if self._allow_punctuation_prefix:
            command += " --allow-punctuation-prefix"

        if self._room_method is not None:
            command += f" --rooms-method {self._room_method.value}"

        if self._max_game_inactivity_time is not None:
            command += (
                f" --max-game-inactivity-time {self._max_game_inactivity_time}"
            )

        if self._log_path is not None:
            command += f" --log-path {self._log_path}"

        return command

    def start(self):
        """
        Starts this testatrice-server instance and, if they are not already running, testatrice-database and testatrice-mailserver.
        """
        os.system(
            f'/bin/bash -c "cd {TestServer._TESTATRICE_DIR} && {self._command} > /dev/null"'
        )
        time.sleep(1)

    def stop(self):
        """
        Stops this testatrice-server instance.
        """
        TestServer._TEST_SERVERS.discard(self)
        os.system(
            f"podman stop testatrice-server-{self.IDENTIFIER} > /dev/null"
        )
