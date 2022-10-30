from model.garlic.garlic import Garlic
from settings import settings


class DiaryText(object):
    def __init__(self, text: str):
        self.value = text

    @classmethod
    def fromTemplateWithGarlic(cls, garlic: Garlic):
        return cls(settings.diary_text_format.format(garlic.elapsed_days()))
