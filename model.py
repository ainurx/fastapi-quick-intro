from typing import Optional
from pydantic import BaseModel
from uuid import uuid4, UUID

class Blog(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    content: str

class CreateBlog(Blog):
    title: str
    content: str

class updateBlog(Blog):
    title: Optional[str] = None
    content: Optional[str] = None