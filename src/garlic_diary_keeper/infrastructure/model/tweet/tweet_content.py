from model.diary import Diary
from model.photo.photo import Photo
from infrastructure.model.tweet.tweet_text import TweetText


class TweetContent(object):
    def __init__(self, text: TweetText, photo: Photo):
        self.text = text
        self.photo = photo

    @classmethod
    def fromDiary(cls, diary: Diary):
        return cls(diary.text, diary.photo)
