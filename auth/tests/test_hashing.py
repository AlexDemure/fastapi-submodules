import unittest

from backend.submodules.auth.security import get_password_hash, verify_password


class TestHashing(unittest.TestCase):

    test_password = "qwerty123"
    wrong_password = "qwerty1234"

    def test_hash_password(self):
        hashed_password = get_password_hash(self.test_password)
        self.assertIsInstance(hashed_password, str)

    def test_unhash_password(self):
        hashed_password = get_password_hash(self.test_password)
        self.assertIsInstance(hashed_password, str)
        decision = verify_password(self.test_password, hashed_password)
        self.assertIsInstance(decision, bool)
        self.assertEqual(decision, True)

        decision = verify_password(self.wrong_password, hashed_password)
        self.assertIsInstance(decision, bool)
        self.assertEqual(decision, False)
