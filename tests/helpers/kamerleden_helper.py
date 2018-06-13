import unittest
from vcr_unittest import VCRTestCase
from helpers import KamerledenHelper

class TestStemmingHelper(VCRTestCase):
    def test_eerste_kamerleden(self):
        kamerleden = KamerledenHelper.eerste_kamerleden()
        self.assertEqual(len(kamerleden), 8)

    def test_tweede_kamerleden(self):
        kamerleden = KamerledenHelper.tweede_kamerleden()
        self.assertEqual(len(kamerleden), 25)

if __name__ == '__main__':
    unittest.main()
