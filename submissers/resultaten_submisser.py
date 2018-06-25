from praw.models import Submission, Comment
from responders import StemmingResponder, TKResponder, EKResponder
from helpers import StemmingHelper
from datetime import datetime
import re
import submission_types
from helpers import KamerledenHelper
import submission_types

class ResultatenSubmisser():
    def kamerstuk_submission(title):
        flairs = [submission_types.MOTIE, submission_types.WETSVOORSTEN]
        search_term = ' OR '.join([f'flair:"{flair}"' for flair in flairs])
        return next(reddit.client().subreddit('rmtk').search('flair:"TK STEMMING"', limit=1, sort='new'))

    def kamerleden_amount(self, flair: str) -> int:
        if flair == submission_types.EK_STEMMING:
            return len(KamerledenHelper.eerste_kamerleden())
        elif flair == submission_types.TK_STEMMING:
            return len(KamerledenHelper.tweede_kamerleden())
        else:
            raise ValueError

    def decide_if_through(self, counted_votes: dict) -> bool:
        return counted_votes[1] > counted_votes[-1]

    def submiss(self, stemming: Submission):
        voteables = sorted(StemmingHelper.get_format(stemming.selftext))
        votes = {v: {-1: 0, 0: 0, 1: 0} for v in voteables}
        user_votes = [
          c for c in stemming.comments if StemmingHelper.get_format(c.body) != set()
        ]
        valid_user_votes = [
          uv for uv in user_votes if self.comment_valid(uv)
        ]
        parsed_user_votes = [
          StemmingHelper.get_votes(vuv.body) for vuv in valid_user_votes
        ]

        print({ vuv.body: [StemmingHelper.get_votes(vuv.body), vuv.id] for vuv in valid_user_votes })

        for vote in parsed_user_votes:
            for voteable, vote_value in vote.items():
                votes[voteable][vote_value] += 1

        binary_results = {voteable: self.decide_if_through(counted_votes) for voteable, counted_votes in votes.items()}

        return {
            'template': 'resultaten',
            'title': 'Resultaten ' + stemming.title,
            'flair': submission_types.UITSLAGEN,
            'invalid_votes': len(user_votes) - len(valid_user_votes),
            'opkomst_percentage': int(round((100 * len(valid_user_votes) / self.kamerleden_amount(stemming.link_flair_text)))),
            'results': votes,
            'date': datetime.utcfromtimestamp(stemming.created_utc).strftime('%d-%m-%Y'),
            'submissions': {v: StemmingHelper.find_kamerstuk_submission(v) for v in voteables}
        }

    def comment_valid(self, comment: Comment):
        return [None, None, None] == [r.respond(comment) for r in [StemmingResponder(), TKResponder(), EKResponder()]]
