from model.garlic.garlic import Garlic
from settings import settings


class DiaryText(object):
    def __init__(self, text: str):
        self.value = text

    @classmethod
    def fromTemplate(cls, text: str, garlic: Garlic):
        templated_text = settings.diary_text_format.format(
            garlic.elapsed_days(),
            text
        )
        return cls(DiaryText.sliceEndOfReadingPoint(templated_text, 140))

    @staticmethod
    def sliceEndOfReadingPoint(text: str, max_length: int):
        try:
            index = text[:max_length].rindex('。')
            return text[:index+1]
        except:
            return text[:max_length]
