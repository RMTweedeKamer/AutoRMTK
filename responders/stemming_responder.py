from responders.responder import Responder
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

        vote_format = self.get_format(comment.submission.selftext)

        comment_format = self.get_format(comment.body)
        not_voted_on = vote_format - comment_format
        not_in_voting = comment_format - vote_format
        incorrect_keyword = set([k for k, vote in self.get_votes(comment.body).items() if vote == None])

        if not_voted_on == not_in_voting == incorrect_keyword == set():
            return None

        return {
            'template': 'stemming',
            'not_in_voting': not_in_voting,
            'not_voted_on': not_voted_on,
            'incorrect_keyword': incorrect_keyword
        }

    def get_format(self, body: str) -> set:
        """
        >>> body = 'Leden van de Tweede Kamer der Staten-Generaal,U kunt op de volgende moties en wetten uw stem uitbrengen:W0309: Motie tot inkorting appa-uitkeringKS0310: Motie tot differentiatie aan brengen in de titelatuur van bachelors op het HBO en de universiteitM0311: Motie tegen Bendelaars (bendebedelaarsproblematiek)Hanteer a.u.b. het volgende format:Telkens met twee spaties achter de regelVoor/Tegen/Onthouden:W0309:KS0310:M0311:'
        >>> get_format(body) == {'M0311', 'W0309', 'KS0310'}
        True
        """
        return set(re.findall(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*)', body))

    def vote_value(self, vote: str) -> int:
        """
        >>> vote_value('VOOR') == 1
        True
        >>> vote_value('onthouden') == 0
        True
        >>> vote_value('Tegen') == -1
        True
        >>> vote_value('random') == None
        True
        """
        return {'voor': 1, 'onthouden': 0, 'tegen': -1}.get(vote.lower())

    def get_votes(self, body: str) -> dict:
        votes = re.findall(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*\:\ *\w+)', body)
        votes = [re.search(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*)\:\ *(\w+)', vote, re.IGNORECASE) for vote in votes]
        votes = [[vote.group(1).upper(), self.vote_value(vote.group(2))] for vote in votes if vote != None]

        return dict(votes)

