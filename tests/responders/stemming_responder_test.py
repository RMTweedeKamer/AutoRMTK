import unittest
import submission_types
import reddit
from vcr_unittest import VCRTestCase
from responders import StemmingResponder

class TestStemmingResponder(VCRTestCase):
    def test_follows_format1(self):
        comment = reddit.client().comment(id="dzpm1ak")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_follows_format2(self):
        comment = reddit.client().comment(id="dzrpx9y")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_follows_format2(self):
        comment = reddit.client().comment(id="e041767")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    def test_no_vote_at_all(self):
        comment = reddit.client().comment(id="dzrpoad")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

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

if __name__ == '__main__':
    unittest.main()
