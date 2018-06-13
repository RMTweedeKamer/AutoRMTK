import re

class StemmingHelper(object):
    @staticmethod
    def get_format(body: str) -> set:
        """
        >>> body = 'Leden van de Tweede Kamer der Staten-Generaal,U kunt op de volgende moties en wetten uw stem uitbrengen:W0309: Motie tot inkorting appa-uitkeringKS0310: Motie tot differentiatie aan brengen in de titelatuur van bachelors op het HBO en de universiteitM0311: Motie tegen Bendelaars (bendebedelaarsproblematiek)Hanteer a.u.b. het volgende format:Telkens met twee spaties achter de regelVoor/Tegen/Onthouden:W0309:KS0310:M0311:'
        >>> get_format(body) == {'M0311', 'W0309', 'KS0310'}
        True
        """
        return set(re.findall(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*)', body))

    @staticmethod
    def vote_value(vote: str) -> int:
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
        vote = vote.lower()

        if 'voor' in vote:
            return 1
        if 'onthoud' in vote:
            return 0
        if 'tegen' in vote:
            return -1

        return None

    @staticmethod
    def get_votes(body: str) -> dict:
        votes = re.findall(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*\:\ *\w+)', body)
        votes = [re.search(r'([A-Z]{1,2}[0-9]{4}\-?[A-Za-z0-9]*)\:\ *(\w+)', vote, re.IGNORECASE) for vote in votes]
        votes = [[vote.group(1).upper(), StemmingHelper.vote_value(vote.group(2))] for vote in votes if vote != None]

        return dict(votes)
