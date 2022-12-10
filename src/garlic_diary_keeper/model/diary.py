from model.diary_tag import DiaryTag
from model.diary_text import DiaryText
from model.photo.photo import Photo


class Diary(object):
    def __init__(self, text: DiaryText, tag: DiaryTag, photo: Photo):
        self.text = text
        self.tag = tag
        self.photo = photo
