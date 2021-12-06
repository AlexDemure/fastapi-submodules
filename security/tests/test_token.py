import unittest

from backend.submodules.security.utils import encode_token, decode_token, generate_random_code


class TestToken(unittest.TestCase):

    context = dict(name="security", value=generate_random_code())

    def test_token(self):
        security_token = encode_token(self.context)
        self.assertIsInstance(security_token, str)

    def test_verify_token(self):
        security_token = encode_token(self.context)
        self.assertIsInstance(security_token, str)
        context = decode_token(security_token)
        self.assertIsInstance(context, dict)
        self.assertEqual(self.context, context)
