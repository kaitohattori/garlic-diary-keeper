class GarlicDiaryKeeperException(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'


class CameraCaptureException(GarlicDiaryKeeperException):
    def __init__(self, message: str = None):
        if message:
            super().__init__(message)
        else:
            super().__init__('Camera capture failed.')


class TweetBodyLengthException(GarlicDiaryKeeperException):
    def __init__(self, message: str = None):
        if message:
            super().__init__(message)
        else:
            super().__init__('Tweet body should be less than 140 characters.')


class SettingsLoadEnvironmentVariableException(GarlicDiaryKeeperException):
    def __init__(self, key: str):
        super().__init__(f'Settings failed to load from environment variable. key=[{key}].')  # noqa: E501
