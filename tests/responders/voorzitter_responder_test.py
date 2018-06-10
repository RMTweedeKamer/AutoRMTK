import unittest
import submission_types
import reddit
from vcr_unittest import VCRTestCase
from responders import VoorzitterResponder

class TestVoorzitterResponder(VCRTestCase):
    def test_no_voorzitter_in_votings(self):
        comment = reddit.client().comment(id="dzpm1ak")
        response = VoorzitterResponder().respond(comment)
        self.assertIsNone(response)

    def test_dont_respond_op(self):
        comment = reddit.client().comment(id="e0fabk6")
        response = VoorzitterResponder().respond(comment)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
