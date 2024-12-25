from uuid import UUID
from celery.result import AsyncResult

from app.celery_app import app as celery_app

from app.schemas.detect import DetectionRequestResponse
from app.engine import detection


class DetectService:
    async def detect(self, video: bytes, content_type: str) -> DetectionRequestResponse:
        task: AsyncResult = detection_task.delay(video, content_type)  # type: ignore
        return DetectionRequestResponse(id=UUID(task.id))

    async def check_detection(self):
        pass


@celery_app.task(name="detect")
def detection_task(video: bytes, content_type: str):
    d = detection.instance()
    video_path = d.save(video, content_type)
    print(video_path)

detect_service = DetectService()
