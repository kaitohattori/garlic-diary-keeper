from model.diary import Diary
from model.tweet.tweet_body import TweetBody
from model.tweet.tweet_content import TweetContent
from infrastructure.tweeter import Tweeter

class DiaryKeeper(object):
    def keep(self, diary: Diary):
        # Twitterに日記を投稿する
        self.post_tweet(diary)

    def post_tweet(self, diary: Diary):
        # ツイート本文を作成する
        tweet_body = TweetBody.of(diary.garlic)

        # ツイート内容を作成する
        tweet_content = TweetContent(tweet_body, diary.photo)

        # ツイートする
        tweeter = Tweeter()
        tweeter.tweet(tweet_content)

