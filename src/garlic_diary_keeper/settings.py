import os

from error import SettingsLoadEnvironmentVariableException

class Settings(object):
    def __init__(self):
        self.captured_image_path = '/tmp/apps/garlic_diary_keeper/image.jpg'
        self.api_key = self.getenv('API_KEY')
        self.api_key_secret = self.getenv('API_KEY_SECRET')
        self.access_token = self.getenv('ACCESS_TOKEN')
        self.access_token_secret = self.getenv('ACCESS_TOKEN_SECRET')

    def getenv(self, key: str):
        if os.getenv(key):
            return os.getenv(key)
        else:
            raise SettingsLoadEnvironmentVariableException(key)

settings = Settings()
