import os
from time import sleep

import cv2

from error import CameraCaptureException
from model.photo.photo import Photo
from settings import settings

class Camera:
    def activate(self):
        video_capture = cv2.VideoCapture(0)
        # wait 3 seconds for preparing VideoCapture
        sleep(3)
        return video_capture

    def capture(self) -> Photo:
        video_capture = self.activate()

        result, frame = video_capture.read()
        if result is False:
            raise CameraCaptureException

        Camera.save_image(settings.captured_image_path, frame)

        return Photo(settings.captured_image_path)

    @staticmethod
    def save_image(path: str, image):
        # make directories if not exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # save image to path
        cv2.imwrite(path, image)
