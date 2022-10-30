import os
from time import sleep

import cv2

from exception.exceptions import CameraCaptureException
from model.photo.photo import Photo
from settings import settings


class Camera:
    def activate(self):
        # Initialize video capture
        video_capture = cv2.VideoCapture(0)
        # Wait 3 seconds for preparing video capture
        sleep(3)
        return video_capture

    def take(self) -> Photo:
        # Acitivate the camera
        video_capture = self.activate()

        # Get the current frame from video capture
        result, frame = video_capture.read()
        if result is False:
            raise CameraCaptureException

        # Save the frame to path
        Camera.save_image(settings.captured_image_path, frame)

        return Photo(settings.captured_image_path)

    def load_from_local(self) -> Photo:
        return Photo(settings.captured_image_path)

    @staticmethod
    def save_image(path: str, image):
        # make directories if not exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # save image to path
        cv2.imwrite(path, image)
