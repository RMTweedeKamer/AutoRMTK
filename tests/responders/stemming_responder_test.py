import unittest
import submission_types
import reddit
from vcr_unittest import VCRTestCase
from responders import StemmingResponder

class TestVoorzitterResponder(VCRTestCase):
    def test_follows_format1(self):
        comment = reddit.client().comment(id="dzpm1ak")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_follows_format2(self):
        comment = reddit.client().comment(id="dzrpx9y")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_no_vote_at_all(self):
        comment = reddit.client().comment(id="dzrpoad")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_get_vote_format1(self):
        submission = reddit.client().submission(id='8oag4a')
        format = StemmingResponder().get_format(submission.selftext)
        self.assertEqual(format, {'M0312', 'M0313', 'W0125-I', 'W0126'})

    def test_get_vote_format2(self):
        submission = reddit.client().submission(id='8mj3f6')
        format = StemmingResponder().get_format(submission.selftext)
        self.assertEqual(format, {'M0309', 'M0310', 'M0311'})

    def test_get_vote_format3(self):
        submission = reddit.client().submission(id='8ktghf')
        format = StemmingResponder().get_format(submission.selftext)
        self.assertEqual(format, {
            'M0295', 'M0296', 'M0297', 'M0298', 'M0299', 'M0300', 'M0301', 'M0302',
            'M0303', 'M0304', 'M0305', 'M0306', 'M0307', 'M0308', 'W0124'
        })


    def test_get_votes1(self):
        comment = reddit.client().comment(id="dzo84wk")
        votes = StemmingResponder().get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0309': 1,
            'M0310': 0,
            'M0311': 1
        })

    def test_get_votes2(self):
        comment = reddit.client().comment(id="dznyp21")
        votes = StemmingResponder().get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0309': 1,
            'M0310': -1,
            'M0311': -1
        })

    def test_get_votes3(self):
        comment = reddit.client().comment(id="dsppe6c")
        votes = StemmingResponder().get_votes(comment.body)
        self.assertDictEqual(votes, {
            'M0283': 1,
            'M0284': 0,
            'M0285': 1
        })

    def test_not_voted_on1(self):
        comment = reddit.client().comment(id="dt6kgzo")
        response = StemmingResponder().respond(comment)
        self.assertDictEqual(response, {
            'template': 'stemming',
            'not_in_voting': set(),
            'not_voted_on': {'M0283', 'M0284'},
            'incorrect_keyword': set()
        })

    def test_not_voted_on2(self):
        comment = reddit.client().comment(id="dzfj0ws")
        response = StemmingResponder().respond(comment)
        self.assertDictEqual(response, {
            'template': 'stemming',
            'not_in_voting': set(),
            'not_voted_on': {'M0295'},
            'incorrect_keyword': set()
        })

    def test_incorrect_keyword1(self):
        comment = reddit.client().comment(id="dsvimxl")
        response = StemmingResponder().respond(comment)
        self.assertDictEqual(response, {
            'template': 'stemming',
            'not_in_voting': set(),
            'not_voted_on': set(),
            'incorrect_keyword': {'M0285'}
        })


if __name__ == '__main__':
    unittest.main()
