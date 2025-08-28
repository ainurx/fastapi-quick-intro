from fastapi import HTTPException
from uuid import uuid4, UUID
from typing import List
from .blog_entity import Blog
from .blog_dto import CreateBlog, UpdateBlog

blog_repository: List[Blog] = [
    Blog(
        id=uuid4(),
        title="One piece",
        content="it's real"
    ),
    Blog(
        id=uuid4(),
        title="My hero academia",
        content="number one hero"
    ),
    Blog(
        id=uuid4(),
        title="Bleach: thousand year blood war",
        content="final arc"
    )
]

def get_all():
    return blog_repository

def get_by_id(id: UUID):
    blog_index = next((i for i, item in enumerate(blog_repository) if item.id == id), None)
    if blog_index:
        return blog_repository[blog_index]
    else:
        return blog_index

def create(dtoBlog: CreateBlog):
    blog_repository.append(dtoBlog)
    return dtoBlog

def update(id: UUID, dtoBlog: UpdateBlog):
    blogIndex = next((i for i, item in enumerate(blog_repository) if item.id == id ), None)
    if blogIndex:
        previous_blog = blog_repository[blogIndex]
        blog_repository[blogIndex] = previous_blog.model_copy(update=dtoBlog.model_dump(exclude_unset=True))
        return blog_repository[blogIndex]
    else:
        raise HTTPException(status_code=404, detail="blog not found")
    
def delete(id: UUID):
    blog_index = next((i for i, item in enumerate(blog_repository) if item.id == id ), None)
    if blog_index:
        del blog_repository[blog_index]
        return True
    else:
        raise HTTPException(status_code=404, detail="blog not found")
