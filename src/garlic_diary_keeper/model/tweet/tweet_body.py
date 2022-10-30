from exception.exceptions import TweetBodyLengthException
from model.garlic.garlic import Garlic
from settings import settings

class TweetBody(object):
    def __init__(self, text):
        if len(text) > 140:
            raise TweetBodyLengthException
        self.text = text

    @classmethod
    def of(cls, garlic: Garlic):
        return cls(settings.tweet_body_format.format(garlic.elapsed_days()))
