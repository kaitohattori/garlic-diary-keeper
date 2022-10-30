from error import TweetBodyLengthException

class TweetBody(object):
    def __init__(self, text):
        if len(text) > 140:
            raise TweetBodyLengthException
        self.text = text
