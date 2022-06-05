import unittest

from password.pypassword import Password


class TestPassword(unittest.TestCase):

    def test_generate_32(self):
        pwd = Password()
        passphrase = pwd.generate(32)
        self.assertEqual(len(passphrase), 32)


if __name__ == '__main__':
    unittest.main()
