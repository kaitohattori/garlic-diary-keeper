import tweepy

from model.tweet.tweet_content import TweetContent
from settings import settings

class Tweeter(object):
    def __init__(self):
        self.api = None

    def authenticate(self) -> tweepy.API:
        auth = tweepy.OAuthHandler(settings.api_key, settings.api_key_secret)
        auth.set_access_token(settings.access_token, settings.access_token_secret)
        return tweepy.API(auth)

    def tweet(self, content: TweetContent):
        # Authenticate the twitter API
        api = self.authenticate()
        # Tweet text with image
        api.update_status_with_media(
            status = content.body.text, 
            filename = content.photo.path
        )
