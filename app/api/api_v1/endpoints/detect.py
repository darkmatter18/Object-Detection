from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Path, UploadFile, status

from app import services, schemas
from app.core.exceptions import APIException


router = APIRouter()

@router.post("/", description="Detect Objects from video", status_code=status.HTTP_202_ACCEPTED)
async def detect_video(video: UploadFile) -> schemas.DetectionRequestResponse:
    supported_types = ['video/mp4', 'video/x-matroska',
                               'video/ogg','video/quicktime', 'video/x-ms-wmv',
                               'video/webm']
    if video.content_type not in supported_types:
        raise APIException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type", message="Unsupported file type")
    return await services.detect_service.detect(video=await video.read(), content_type=video.content_type)


@router.get("/{detection_id}", description="Check if the processing is done or not")
async def check_detection(detection_id: Annotated[UUID, Path(description="Detection ID")]):
    return await services.detect_service.check_detection(detection_id=detection_id)
