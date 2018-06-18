import unittest
from helpers import KamerledenHelper
import vcr

class TestKamerledenHelper(unittest.TestCase):
    @vcr.use_cassette('tests/cassettes/helpers/kamerleden_helper.test_eerste_kamer.yml', record_mode='new_episodes')
    def test_eerste_kamerleden(self):
        kamerleden = KamerledenHelper.eerste_kamerleden()
        self.assertEqual(len(kamerleden), 8)
 
    @vcr.use_cassette('tests/cassettes/helpers/kamerleden_helper.test_tweede_kamer.yml', record_mode='new_episodes')
    def test_tweede_kamerleden(self):
        kamerleden = KamerledenHelper.tweede_kamerleden()
        self.assertEqual(len(kamerleden), 25)

if __name__ == '__main__':
    unittest.main()
