import unittest

from backend.submodules.auth.security import generate_token, decode_token
from backend.submodules.auth.schemas import Token, TokenPayload
from backend.submodules.auth.enums import TokenPurpose


class RaisedClass:
    pass


class TestToken(unittest.TestCase):

    token_subjects = ["test_token", str(1), str(None), "None", str(RaisedClass)]

    def test_get_token(self):
        for sub in self.token_subjects:
            token = generate_token(sub)
            self.assertIsInstance(token, Token)

        self.assertRaises(ValueError, generate_token, RaisedClass)
        self.assertRaises(ValueError, generate_token, None)
        self.assertRaises(ValueError, generate_token, list())

    def test_decode_token(self):
        for sub in self.token_subjects:
            token = generate_token(sub)
            self.assertIsInstance(token, Token)

            token_access_payload = decode_token(token.access_token, TokenPurpose.access)
            self.assertIsInstance(token_access_payload, TokenPayload)
            self.assertEqual(token_access_payload.sub, sub)

            token_refresh_payload = decode_token(token.refresh_token, TokenPurpose.refresh)
            self.assertIsInstance(token_refresh_payload, TokenPayload)
            self.assertEqual(token_refresh_payload.sub, sub)
