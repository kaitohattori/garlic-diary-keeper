from exception.exceptions import TweetBodyLengthException


class TweetText(object):
    def __init__(self, text):
        if len(text) > 140:
            raise TweetBodyLengthException
        self.value = text
