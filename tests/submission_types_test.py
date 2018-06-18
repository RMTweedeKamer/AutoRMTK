import unittest
import submission_types
import reddit
import vcr

class TestSubmissionTypes(unittest.TestCase):
    @vcr.use_cassette('tests/cassettes/submission_types.test_debat.yml', record_mode='new_episodes')
    def test_debat(self):
        self.assert_flair_being_used(submission_types.DEBAT)

    @vcr.use_cassette('tests/cassettes/submission_types.test_ek_Stem.yml', record_mode='new_episodes')
    def test_ek_stemming(self):
        self.assert_flair_being_used(submission_types.EK_STEMMING)

    @vcr.use_cassette('tests/cassettes/submission_types.test_ek_tk_stem.yml', record_mode='new_episodes')
    def test_ek_tk_stemming(self):
        self.assert_flair_being_used(submission_types.EK_TK_STEMMING)

    @vcr.use_cassette('tests/cassettes/submission_types.test_eu.yml', record_mode='new_episodes')
    def test_europese_unie(self):
        self.assert_flair_being_used(submission_types.EUROPESE_UNIE)

    @vcr.use_cassette('tests/cassettes/submission_types.test_gebeurtenis.yml', record_mode='new_episodes')
    def test_gebeurtenis(self):
        self.assert_flair_being_used(submission_types.GEBEURTENIS)

    @vcr.use_cassette('tests/cassettes/submission_types.test_kamerstuk.yml', record_mode='new_episodes')
    def test_kamerstuk(self):
        self.assert_flair_being_used(submission_types.KAMERSTUK)

    @vcr.use_cassette('tests/cassettes/submission_types.test_kb.yml', record_mode='new_episodes')
    def test_koninklijk_besluit(self):
        self.assert_flair_being_used(submission_types.KONINKLIJK_BESLUIT)

    @vcr.use_cassette('tests/cassettes/submission_types.test_meta.yml', record_mode='new_episodes')
    def test_meta(self):
        self.assert_flair_being_used(submission_types.META)

    @vcr.use_cassette('tests/cassettes/submission_types.test_motie.yml', record_mode='new_episodes')
    def test_motie(self):
        self.assert_flair_being_used(submission_types.MOTIE)

    @vcr.use_cassette('tests/cassettes/submission_types.test_parlement.yml', record_mode='new_episodes')
    def test_parlement(self):
        self.assert_flair_being_used(submission_types.PARLEMENT)

    #@vcr.use_cassette('tests/cassettes/submission_types.test_.yml', record_mode='new_episodes')
    #def test_petitie(self):
    #    self.assert_flair_being_used(submission_types.PETITIE)

    #@vcr.use_cassette('tests/cassettes/submission_types.test_referendum.yml', record_mode='new_episodes')
    #def test_referendum(self):
    #    self.assert_flair_being_used(submission_types.REFERENDUM)

    @vcr.use_cassette('tests/cassettes/submission_types.test_tk_stemming.yml', record_mode='new_episodes')
    def test_tk_stemming(self):
        self.assert_flair_being_used(submission_types.TK_STEMMING)

    @vcr.use_cassette('tests/cassettes/submission_types.test_uitslagen.yml', record_mode='new_episodes')
    def test_uitslagen(self):
        self.assert_flair_being_used(submission_types.UITSLAGEN)

    @vcr.use_cassette('tests/cassettes/submission_types.test_vn.yml', record_mode='new_episodes')
    def test_verenigde_naties(self):
        self.assert_flair_being_used(submission_types.VERENIGDE_NATIES)

    @vcr.use_cassette('tests/cassettes/submission_types.test_verkiezingen.yml', record_mode='new_episodes')
    def test_verkiezingen(self):
        self.assert_flair_being_used(submission_types.VERKIEZINGEN)

    @vcr.use_cassette('tests/cassettes/submission_types.test_vragenuur.yml', record_mode='new_episodes')
    def test_vragenuur(self):
        self.assert_flair_being_used(submission_types.VRAGENUUR)

    @vcr.use_cassette('tests/cassettes/submission_types.test_wetsvoorstel.yml', record_mode='new_episodes')
    def test_wetsvoorstel(self):
        self.assert_flair_being_used(submission_types.WETSVOORSTEL)

    @vcr.use_cassette('tests/cassettes/submission_types.test_ek_debat.yml', record_mode='new_episodes')
    def test_ek_debat(self):
        self.assert_flair_being_used(submission_types.EK_DEBAT)

    def assert_flair_being_used(self, flair):
        submissions = reddit.client().subreddit('rmtk').search('flair:"' + flair + '"', limit=1)
        self.assertEqual(len(list(submissions)), 1, msg=flair)

if __name__ == '__main__':
    unittest.main()
