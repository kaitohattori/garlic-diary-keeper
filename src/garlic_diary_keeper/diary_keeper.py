from model.diary import Diary
from infrastructure.model.tweet.tweet_content import TweetContent
from infrastructure.twitter_client import TwitterClient


class DiaryKeeper(object):
    def __init__(self):
        self.twitter_client = TwitterClient()

    def keep(self, diary: Diary):
        # Twitterに日記を投稿する
        self.post_tweet(diary)

    def post_tweet(self, diary: Diary):
        # ツイート内容を作成する
        tweet_content = TweetContent.fromDiary(diary)

        # ツイートする
        self.twitter_client.post_tweet(tweet_content)
