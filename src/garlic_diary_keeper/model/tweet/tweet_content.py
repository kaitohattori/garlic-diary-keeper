from model.photo.photo import Photo
from model.tweet.tweet_body import TweetBody

class TweetContent(object):
    def __init__(self, body: TweetBody, photo: Photo):
        self.body = body
        self.photo = photo
