from responders.responder import Responder
from helpers.stemming_helper import StemmingHelper
from praw.models import Comment, Submission
import re
import submission_types

class StemmingResponder(Responder):
    def should_respond(self, comment: Comment) -> bool:
        if not isinstance(comment.parent(), Submission):
            return False
        if len([1 for c in comment.replies.list() if "meta" in c.body.lower()]) > 0:
            return False
        if not re.findall(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*\:\ *\w+)', comment.body):
            return False

        return comment.submission.link_flair_text in [
            submission_types.EK_STEMMING, submission_types.TK_STEMMING,
            submission_types.EK_TK_STEMMING
        ]

    def respond(self, comment: Comment):
        if not self.should_respond(comment):
            return None

        vote_format = StemmingHelper.get_format(comment.submission.selftext)

        comment_format = StemmingHelper.get_format(comment.body)
        not_voted_on = vote_format - comment_format
        not_in_voting = comment_format - vote_format
        incorrect_keyword = set([k for k, vote in StemmingHelper.get_votes(comment.body).items() if vote == None])

        if not_voted_on == not_in_voting == incorrect_keyword == set():
            return None

        return {
            'template': 'stemming',
            'not_in_voting': not_in_voting,
            'not_voted_on': not_voted_on,
            'incorrect_keyword': incorrect_keyword
        }
