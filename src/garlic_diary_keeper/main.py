from ai_text_generator import AITextGenerator
from camera import Camera
from model.diary_text import DiaryText
from model.diary_tag import DiaryTag
from model.diary import Diary
from model.garlic.garlic_factory import GarlicFactory
from diary_keeper import DiaryKeeper
from infrastructure.twitter_client import TwitterClient


def main():
    # 写真を撮る
    camera = Camera()
    photo = camera.take()
    # photo = camera.load_from_local()

    # トレンドを取得する
    twitter_client = TwitterClient()
    trend_topic = twitter_client.get_trend_topic()

    # 日記
    generator = AITextGenerator()
    generated_text = generator.generate(trend_topic)

    # にんにく
    garlic = GarlicFactory.build()

    diary_text = DiaryText.fromTemplate(generated_text, garlic)
    diary_tag = DiaryTag(trend_topic)
    diary = Diary(diary_text, diary_tag, photo)

    # 日記をつける
    diary_keeper = DiaryKeeper()
    diary_keeper.keep(diary)


if __name__ == "__main__":
    main()
