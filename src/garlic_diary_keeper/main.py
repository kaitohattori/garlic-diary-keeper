from camera import Camera
from model.diary import Diary
from model.garlic.garlic_factory import GarlicFactory
from diary_keeper import DiaryKeeper

def main():
    # 写真を撮る
    camera = Camera()
    photo = camera.take()

    # にんにく
    garlic = GarlicFactory.build()
    
    # 日記
    diary = Diary(garlic, photo)

    # 日記をつける
    diary_keeper = DiaryKeeper()
    diary_keeper.keep(diary)

if __name__ == "__main__":
    main()
