from responders.responder import Responder
from praw.models import Comment
import submission_types

from helpers import KamerledenHelper

class EKResponder(Responder):
    def should_respond(self, comment: Comment) -> bool:
        if comment.submission.author.name == comment.author.name:
            return False

        return comment.submission.link_flair_text == submission_types.EK_STEMMING

    def respond(self, comment: Comment):
        if not self.should_respond(comment):
            return None

        if comment.author.name.lower() in KamerledenHelper.eerste_kamerleden():
            return None

        return {'template': 'ek'}
