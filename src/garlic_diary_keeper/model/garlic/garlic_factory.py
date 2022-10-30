from model.garlic.garlic import Garlic
from settings import settings

class GarlicFactory(object):
    @staticmethod
    def build() -> Garlic:
        return Garlic(settings.growth_start_date)
