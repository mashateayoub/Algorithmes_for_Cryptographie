import unittest
from aes import AES


class TestBlock(unittest.TestCase):
    def test_expected_value(self):
        message = b"\x32\x43\xF6\xA8\x88\x5A\x30\x8D\x31\x31\x98\xA2\xE0\x37\x07\x34"
        key = b"\x2B\x7E\x15\x16\x28\xAE\xD2\xA6\xAB\xF7\x15\x88\x09\xCF\x4F\x3C"
        ciphertext = AES(bytes(key)).encrypt(bytes(message))
        self.assertEqual(
            ciphertext,
            b"\x39\x25\x84\x1D\x02\xDC\x09\xFB\xDC\x11\x85\x97\x19\x6A\x0B\x32",
        )

    def test_expected_value1(self):
        """
        Mentionned Example in the AES_TES_EXAMPLE.pdf
        """
        message = b"\x54\x77\x6F\x20\x4F\x6E\x65\x20\x4E\x69\x6E\x65\x20\x54\x77\x6F"
        key = b"\x54\x68\x61\x74\x73\x20\x6D\x79\x20\x4B\x75\x6E\x67\x20\x46\x75"
        ciphertext = AES(bytes(key)).encrypt(bytes(message))
        self.assertEqual(
            ciphertext,
            b"\x29\xC3\x50\x5F\x57\x14\x20\xF6\x40\x22\x99\xB3\x1A\x02\xD7\x3A",
        )


def run():
    print('Usage: ./aes.py encrypt "key" "message"')
    print("Running tests...")
    unittest.main()


if __name__ == "__main__":
    run()
