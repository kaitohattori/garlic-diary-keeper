from model.garlic.garlic import Garlic
from settings import settings


class DiaryTag(object):
    def __init__(self, value: str):
        self.value = f'#{value}'
