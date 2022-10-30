from camera import Camera
from model.tweet.tweet_content import TweetContent
from tweet_body_generator import TweetBodyGenerator
from tweeter import Tweeter

def main():
    try:
        # 写真を撮る
        camera = Camera()
        photo = camera.capture()

        # ツイート本文を作成する
        generator = TweetBodyGenerator()
        tweet_body = generator.generate()

        # ツイート内容を作成する
        tweet_content = TweetContent(tweet_body, photo)

        # ツイートする
        tweeter = Tweeter()
        tweeter.tweet(tweet_content)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
