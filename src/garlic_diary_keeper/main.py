from camera import Camera
from model.garlic.garlic_factory import GarlicFactory
from model.tweet.tweet_body import TweetBody
from model.tweet.tweet_content import TweetContent
from tweeter import Tweeter

def main():
    # 写真を撮る
    camera = Camera()
    photo = camera.take()

    # にんにく
    garlic = GarlicFactory.build()

    # ツイート本文を作成する
    tweet_body = TweetBody.of(garlic)

    # ツイート内容を作成する
    tweet_content = TweetContent(tweet_body, photo)

    # ツイートする
    tweeter = Tweeter()
    tweeter.tweet(tweet_content)

if __name__ == "__main__":
    main()
