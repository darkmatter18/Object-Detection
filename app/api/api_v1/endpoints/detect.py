from fastapi import APIRouter, status

router = APIRouter()


@router.post("/", description="Detect Objects from video", status_code=status.HTTP_202_ACCEPTED)
async def detect_video():
    pass


@router.post("/{detection_id}", description="Check if the processing is done or not")
async def check_detection():
    pass
