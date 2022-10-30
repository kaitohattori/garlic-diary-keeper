from model.garlic.garlic import Garlic
from model.photo.photo import Photo

class Diary(object):
    def __init__(self, garlic: Garlic, photo: Photo):
        self.garlic = garlic
        self.photo = photo
