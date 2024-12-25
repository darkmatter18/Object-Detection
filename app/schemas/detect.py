from uuid import UUID

from pydantic import BaseModel


class DetectionRequestResponse(BaseModel):
    id: UUID
