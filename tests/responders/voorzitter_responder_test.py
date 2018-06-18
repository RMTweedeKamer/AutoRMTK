import unittest
import submission_types
import reddit
import vcr
from responders import VoorzitterResponder

class TestVoorzitterResponder(unittest.TestCase):
    @vcr.use_cassette('tests/cassettes/responders/voorzitter_responder.test_nviv.yml', record_mode='new_episodes')
    def test_no_voorzitter_in_votings(self):
        comment = reddit.client().comment(id="dzpm1ak")
        response = VoorzitterResponder().respond(comment)
        self.assertIsNone(response)

    @vcr.use_cassette('tests/cassettes/responders/voorzitter_responder.test_dro.yml', record_mode='new_episodes')
    def test_dont_respond_op(self):
        comment = reddit.client().comment(id="e0fabk6")
        response = VoorzitterResponder().respond(comment)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
