from exception.exceptions import TweetBodyLengthException


class TweetText(object):
    def __init__(self, text: str, hash_tag: str):
        hashtag = f'\n{hash_tag}'
        self.value = f'{TweetText.sliceEndOfReadingPoint(text, 140 - len(hashtag))}{hashtag}'

    @staticmethod
    def sliceEndOfReadingPoint(text: str, max_length: int):
        try:
            index = text[:max_length].rindex('。')
            return text[:index+1]
        except:
            return text[:max_length]
