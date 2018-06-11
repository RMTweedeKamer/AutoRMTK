import unittest
import submission_types
import reddit
from vcr_unittest import VCRTestCase

class TestSubmissionTypes(VCRTestCase):
    def test_debat(self):
        self.assert_flair_being_used(submission_types.DEBAT)

    def test_ek_stemming(self):
        self.assert_flair_being_used(submission_types.EK_STEMMING)

    def test_ek_tk_stemming(self):
        self.assert_flair_being_used(submission_types.EK_TK_STEMMING)

    def test_europese_unie(self):
        self.assert_flair_being_used(submission_types.EUROPESE_UNIE)

    def test_gebeurtenis(self):
        self.assert_flair_being_used(submission_types.GEBEURTENIS)

    def test_kamerstuk(self):
        self.assert_flair_being_used(submission_types.KAMERSTUK)

    def test_koninklijk_besluit(self):
        self.assert_flair_being_used(submission_types.KONINKLIJK_BESLUIT)

    def test_meta(self):
        self.assert_flair_being_used(submission_types.META)

    def test_motie(self):
        self.assert_flair_being_used(submission_types.MOTIE)

    def test_parlement(self):
        self.assert_flair_being_used(submission_types.PARLEMENT)

    #def test_petitie(self):
    #    self.assert_flair_being_used(submission_types.PETITIE)

    #def test_referendum(self):
    #    self.assert_flair_being_used(submission_types.REFERENDUM)

    def test_tk_Stemming(self):
        self.assert_flair_being_used(submission_types.TK_STEMMING)

    def test_uitslagen(self):
        self.assert_flair_being_used(submission_types.UITSLAGEN)

    def test_verenigde_naties(self):
        self.assert_flair_being_used(submission_types.VERENIGDE_NATIES)

    def test_verkiezingen(self):
        self.assert_flair_being_used(submission_types.VERKIEZINGEN)

    def test_vragenuur(self):
        self.assert_flair_being_used(submission_types.VRAGENUUR)

    def test_wetsvoorstel(self):
        self.assert_flair_being_used(submission_types.WETSVOORSTEL)

    def test_ek_debat(self):
        self.assert_flair_being_used(submission_types.EK_DEBAT)

    def assert_flair_being_used(self, flair):
        submissions = reddit.client().subreddit('rmtk').search('flair:"' + flair + '"', limit=1)
        self.assertEqual(len(list(submissions)), 1, msg=flair)


if __name__ == '__main__':
    unittest.main()
