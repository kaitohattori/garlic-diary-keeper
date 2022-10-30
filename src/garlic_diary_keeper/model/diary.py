from model.diary_text import DiaryText
from model.photo.photo import Photo


class Diary(object):
    def __init__(self, text: DiaryText, photo: Photo):
        self.text = text
        self.photo = photo
