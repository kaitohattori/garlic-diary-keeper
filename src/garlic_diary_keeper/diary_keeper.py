from model.diary import Diary
from infrastructure.model.tweet.tweet_content import TweetContent
from infrastructure.tweeter import Tweeter

class DiaryKeeper(object):
    def keep(self, diary: Diary):
        # Twitterに日記を投稿する
        self.post_tweet(diary)

    def post_tweet(self, diary: Diary):
        # ツイート内容を作成する
        tweet_content = TweetContent.fromDiary(diary)

        # ツイートする
        tweeter = Tweeter()
        tweeter.tweet(tweet_content)
