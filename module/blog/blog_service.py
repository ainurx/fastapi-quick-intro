from fastapi import HTTPException
from uuid import UUID

from .blog_dto import CreateBlog, UpdateBlog
from . import blog_repository

def get_blogs():
    return blog_repository.get_all()

def get_blog_by_id(id: UUID):
    blog = blog_repository.get_by_id(id)
    if blog:
        return blog
    else: 
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")

def create_blog(dto: CreateBlog):
    new_blog = blog_repository.create(dto)
    return new_blog

def update_blog(id: UUID, dto: UpdateBlog):
    get_blog_by_id(id)
    updated_blog = blog_repository.update(id, dto)
    return updated_blog

def delete_blog(id: UUID):
    get_blog_by_id(id)
    blog_repository.delete(id)
    return { "message": f"blog {id} deleted"}