import unittest
import submission_types
import reddit
import vcr
from responders import StemmingResponder

class TestStemmingResponder(unittest.TestCase):
    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_ff1.yml', record_mode='new_episodes')
    def test_follows_format1(self):
        comment = reddit.client().comment(id="dzpm1ak")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_ff2.yml', record_mode='new_episodes')
    def test_follows_format2(self):
        comment = reddit.client().comment(id="dzrpx9y")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_ff3.yml', record_mode='new_episodes')
    def test_follows_format3(self):
        comment = reddit.client().comment(id="e041767")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_nvaa.yml', record_mode='new_episodes')
    def test_no_vote_at_all(self):
        comment = reddit.client().comment(id="dzrpoad")
        response = StemmingResponder().respond(comment)
        self.assertIsNone(response)

    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_nvo1.yml', record_mode='new_episodes')
    def test_not_voted_on1(self):
        comment = reddit.client().comment(id="dt6kgzo")
        response = StemmingResponder().respond(comment)
        self.assertDictEqual(response, {
            'template': 'stemming',
            'not_in_voting': set(),
            'not_voted_on': {'M0283', 'M0284'},
            'incorrect_keyword': set()
        })

    @vcr.use_cassette('tests/cassettes/responders/stemming_responder.test_nvo2.yml', record_mode='new_episodes')
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
