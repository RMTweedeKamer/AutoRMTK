import unittest
import submission_types
import reddit
from vcr_unittest import VCRTestCase

from submissers import ResultatenSubmisser
from praw.models import Submission

class TestResultatenSubmisser(VCRTestCase):
    def test_submiss1(self):
        stemming = reddit.client().submission(id='8mj4nz')
        self.assertDictEqual(
            ResultatenSubmisser().submiss(stemming),
            {
                'template': 'resultaten',
                'title': 'Resultaten Stemming Eerste Kamer over W0124',
                'flair': 'UITSLAGEN',
                'invalid_votes': 0,
                'opkomst_percentage': 88,
                'results': {
                    'W0124': {-1: 0, 0: 0, 1: 7}
                },
                'date': '27-05-2018',
                'submissions': {'W0124': Submission(reddit.client(), id='8b6nkk')},
            }
        )

    def test_submiss2(self):
        stemming = reddit.client().submission(id='8mj3f6')
        self.assertDictEqual(
            ResultatenSubmisser().submiss(stemming),
            {
                'template': 'resultaten',
                'title': 'Resultaten Stemming Tweede Kamer over M0309 t/m M0311, W0125',
                'flair': 'UITSLAGEN',
                'invalid_votes': 0,
                'opkomst_percentage': 96,
                'results': {
                    'M0309': {-1: 2, 0: 0, 1: 22},
                    'M0310': {-1: 7, 0: 1, 1: 16},
                    'M0311': {-1: 8, 0: 0, 1: 16}
                },
                'date': '27-05-2018',
                'submissions': {'M0309': None, 'M0310': None, 'M0311': Submission(reddit.client(), id='8m3sph')},
            }
        )

    def test_decide_if_through1(self):
        self.assertFalse(
            ResultatenSubmisser().decide_if_through(
                {-1: 3, 0: 1, 1: 2}
            )
        )

    def test_decide_if_through2(self):
        self.assertFalse(
            ResultatenSubmisser().decide_if_through(
                {-1: 3, 0: 1, 1: 3}
            )
        )

    def test_decide_if_through3(self):
        self.assertTrue(
            ResultatenSubmisser().decide_if_through(
                {-1: 3, 0: 2, 1: 4}
            )
        )

if __name__ == '__main__':
    unittest.main()
