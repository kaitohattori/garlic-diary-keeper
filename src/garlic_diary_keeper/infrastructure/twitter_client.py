import tweepy

from infrastructure.model.tweet.tweet_content import TweetContent
from settings import settings


class TwitterClient(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(
            settings.twitter_api_key,
            settings.twitter_api_key_secret
        )
        auth.set_access_token(
            settings.twitter_access_token,
            settings.twitter_access_token_secret
        )
        self.api = tweepy.API(auth)

    def post_tweet(self, content: TweetContent):
        # Tweet text with image
        self.api.update_status_with_media(
            status=content.text.value,
            filename=content.photo.path,
        )

    def get_trend_topic(self):
        trends = self.api.get_place_trends(id = settings.twitter_woeid)
        first_trend_topic = trends[0]['trends'][0]['name']
        hash_ignored_first_trend_topic = first_trend_topic if first_trend_topic[:1] != '#' else first_trend_topic[1:]
        return hash_ignored_first_trend_topic
