from ai_text_generator import AITextGenerator
from camera import Camera
from model.diary_text import DiaryText
from model.diary import Diary
from model.garlic.garlic_factory import GarlicFactory
from diary_keeper import DiaryKeeper


def main():
    # 写真を撮る
    camera = Camera()
    photo = camera.take()
    # photo = camera.load_from_local()

    # にんにく
    garlic = GarlicFactory.build()

    # 日記
    generator = AITextGenerator()
    generated_text = generator.generate()
    print(generated_text)

    diary_text = DiaryText.fromTemplate(generated_text, garlic)
    diary = Diary(diary_text, photo)

    # 日記をつける
    diary_keeper = DiaryKeeper()
    diary_keeper.keep(diary)


if __name__ == "__main__":
    main()
