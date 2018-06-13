import unittest
import reddit
from vcr_unittest import VCRTestCase
from helpers import StemmingHelper

class TestStemmingHelper(VCRTestCase):
    def test_get_vote_format1(self):
        submission = reddit.client().submission(id='8oag4a')
        format = StemmingHelper.get_format(submission.selftext)
        self.assertEqual(format, {'M0312', 'M0313', 'W0125-I', 'W0126'})

    def test_get_vote_format2(self):
        submission = reddit.client().submission(id='8mj3f6')
        format = StemmingHelper.get_format(submission.selftext)
        self.assertEqual(format, {'M0309', 'M0310', 'M0311'})

    def test_get_vote_format3(self):
        submission = reddit.client().submission(id='8ktghf')
        format = StemmingHelper.get_format(submission.selftext)
        self.assertEqual(format, {
            'M0295', 'M0296', 'M0297', 'M0298', 'M0299', 'M0300', 'M0301', 'M0302',
            'M0303', 'M0304', 'M0305', 'M0306', 'M0307', 'M0308', 'W0124'
        })

    def test_get_vote_format_with_none(self):
        self.assertEqual(StemmingHelper.get_format(None), set())

    def test_get_votes1(self):
        comment = reddit.client().comment(id="dzo84wk")
        votes = StemmingHelper.get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0309': 1,
            'M0310': 0,
            'M0311': 1
        })

    def test_get_votes2(self):
        comment = reddit.client().comment(id="dznyp21")
        votes = StemmingHelper.get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0309': 1,
            'M0310': -1,
            'M0311': -1
        })

    def test_get_votes3(self):
        comment = reddit.client().comment(id="dsppe6c")
        votes = StemmingHelper.get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0283': 1,
            'M0284': 0,
            'M0285': 1
        })

    def test_get_votes_with_none(self):
        self.assertEqual(StemmingHelper.get_votes(None), {})

if __name__ == '__main__':
    unittest.main()
