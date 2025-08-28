from pydantic import BaseModel
from uuid import UUID

class Blog(BaseModel):
    id: UUID
    title: str
    content: str