from abc import ABCMeta, abstractmethod
from praw.models import Comment

class Responder(metaclass=ABCMeta):
    @abstractmethod
    def respond(self, comment: Comment):
        pass

    @abstractmethod
    def should_respond(self, comment: Comment):
        pass
