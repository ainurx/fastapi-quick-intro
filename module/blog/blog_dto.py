from typing import Optional
from pydantic import Field
from uuid import UUID, uuid4
from .blog_entity import Blog

class CreateBlog(Blog):
    id: Optional[UUID] = uuid4()

class UpdateBlog(Blog):
    # id: None = Field(exclude=True)
    id: Optional[UUID] = None
    title: Optional[str] = None
    content: Optional[str] = None