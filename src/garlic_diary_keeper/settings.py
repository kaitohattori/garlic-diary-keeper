import os

from error import SettingsLoadEnvironmentVariableException

class Settings(object):
    def __init__(self):
        self.captured_image_path = '/tmp/apps/garlic_diary_keeper/image.jpg'
        self.twitter_api_key = self.getenv('TWITTER_API_KEY')
        self.twitter_api_key_secret = self.getenv('TWITTER_API_KEY_SECRET')
        self.twitter_access_token = self.getenv('TWITTER_ACCESS_TOKEN')
        self.twitter_access_token_secret = self.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    def getenv(self, key: str):
        if os.getenv(key):
            return os.getenv(key)
        else:
            raise SettingsLoadEnvironmentVariableException(key)

settings = Settings()
