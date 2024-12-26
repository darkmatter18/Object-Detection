import logging
from typing import Generator

import cv2


logger = logging.getLogger(__name__)

class BaseDetection:
    def save(self, video: bytes, content_type: str) -> str:
        import tempfile
        import mimetypes
        
        ext = mimetypes.guess_extension(content_type)
        if ext is None:
            raise ValueError(f"Unknown content type: {content_type}")
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as f:
            f.write(video)
            return f.name

    def read_video(self, file_name: str) -> Generator[cv2.typing.MatLike, None, None]:
        video = cv2.VideoCapture(file_name)

        while video.isOpened():

            has_frame, frame = video.read()

            if has_frame:
                    yield frame
            else:
                logger.warning("Error reading frame")
                break
        else:
            video.release()
            logger.error("Failed to read video feed")


    def detect(self, file_name: str):
        model_resp = []
        for i, frame in enumerate(self.read_video(file_name)):
            res = self.detect_frame_objects(frame)
            print(f"Frame {i}: {res}")
            model_resp.extend(res)
        
        ret_classess = self.classes_to_labels(list(set(model_resp)))
        return ret_classess

    def detect_frame_objects(self, frame):
        raise NotImplementedError

    def classes_to_labels(self, classes: list[int]) -> list[str]:
        raise NotImplementedError