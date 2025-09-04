from test_server import TestServer
import unittest
from faker import Faker

from crow import crow
from crow import ServerError


class TestRegistration(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def tearDownClass(cls):
        TestServer.stop_all()

    async def test_registration_error_message_when_confirmation_required(self):
        test_server = TestServer(
            enable_registration=True,
            require_activation=True,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.URL

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        client = crow(url, username, password)

        with self.assertRaisesRegex(
            ServerError, "RespRegistrationAcceptedNeedsActivation"
        ):
            await client.register(email_address)

    async def test_registration_error_message_when_confirmation_not_required(
        self,
    ):
        test_server = TestServer(
            enable_registration=True,
            require_activation=False,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.URL

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        client = crow(url, username, password)

        with self.assertRaisesRegex(ServerError, "RespRegistrationAccepted"):
            await client.register(email_address)

    async def test_registration_raises_ServerError_when_registration_disabled(
        self,
    ):
        test_server = TestServer(
            enable_registration=False,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.URL

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        client = crow(url, username, password)

        with self.assertRaisesRegex(ServerError, "RespRegistrationDisabled"):
            await client.register(email_address)

    async def test_registration_raises_ValueError_when_password_is_None(
        self,
    ):
        test_server = TestServer()
        test_server.start()
        url = test_server.URL

        fake = Faker()

        username = fake.user_name()
        password = None
        email_address = fake.email()

        client = crow(url, username, password)

        with self.assertRaises(ValueError):
            await client.register(email_address)


if __name__ == "__main__":
    unittest.main()
