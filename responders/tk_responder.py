from responders.responder import Responder
from praw.models import Comment
import submission_types

class TKResponder(Responder):
    def should_respond(self, comment: Comment) -> bool:
        if comment.submission.author.name == comment.author.name:
            return False

        return comment.submission.link_flair_text == submission_types.TK_STEMMING

    def respond(self, comment: Comment):
        if not self.should_respond(comment):
            return None

        if comment.author.name.lower() in self.kamerleden()['tweedeKamer']:
            return None

        import code; code.interact(local=dict(globals(), **locals()))

        return {'template': 'tk'}