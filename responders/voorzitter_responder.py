from responders.responder import Responder
from praw.models import Comment
import submission_types

class VoorzitterResponder(Responder):
    def should_respond(self, comment: Comment) -> bool:
        if "voorzitter" in comment.body.lower():
            return False

        if comment.submission.author.name == comment.author.name:
            return False

        return comment.submission.link_flair_text in [
            submission_types.WETSVOORSTEL, submission_types.UITSLAGEN,
            submission_types.PETITIE, submission_types.EUROPESE_UNIE,
            submission_types.REFERENDUM, submission_types.DEBAT,
            submission_types.KAMERSTUK, submission_types.VERENIGDE_NATIES,
            submission_types.KONINKLIJK_BESLUIT, submission_types.MOTIE
        ]

    def respond(self, comment: Comment):
        if not self.should_respond(comment):
            return None

        return {'template': 'voorzitter'}
