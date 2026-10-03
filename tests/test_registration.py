import unittest

from crow import ServerError, crow
from faker import Faker

from testatrice.testatrice import TestServer


class TestRegistration(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def tearDownClass(cls):
        TestServer.stop_all_server_containers()

    async def test_registration_returns_false_when_confirmation_required(self):
        test_server = TestServer(
            enable_registration=True,
            require_email_activation=True,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.ws_url

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        result = await crow.register(
            url, username, password, email=email_address
        )

        self.assertFalse(result)

    async def test_registration_returns_true_when_confirmation_not_required(
        self,
    ):
        test_server = TestServer(
            enable_registration=True,
            require_email_activation=False,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.ws_url

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        result = await crow.register(
            url, username, password, email=email_address
        )

        self.assertTrue(result)

    async def test_registration_raises_ServerError_when_registration_disabled(
        self,
    ):
        test_server = TestServer(
            enable_registration=False,
            username_min_length=1,
            username_max_length=99,
        )
        test_server.start()
        url = test_server.ws_url

        fake = Faker()
        username = fake.user_name()
        password = fake.password(length=10)
        email_address = fake.email()

        with self.assertRaisesRegex(ServerError, "RespRegistrationDisabled"):
            await crow.register(url, username, password, email=email_address)

    async def test_registration_raises_ValueError_when_password_is_None(
        self,
    ):
        test_server = TestServer()
        test_server.start()
        url = test_server.ws_url

        fake = Faker()

        username = fake.user_name()
        password = None
        email_address = fake.email()

        with self.assertRaises(ValueError):
            # noinspection bad-argument-type
            await crow.register(url, username, password, email=email_address)


if __name__ == "__main__":
    unittest.main()
