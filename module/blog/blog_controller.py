from fastapi import APIRouter, Path, Body
from uuid import UUID

from .blog_dto import CreateBlog, UpdateBlog
from . import blog_service

router = APIRouter(prefix='/api')

@router.get('/blog')
def get_blogs():
    return blog_service.get_blogs()

@router.get('/blog/{id}')
def get_blog(id: UUID):
    return blog_service.get_blog_by_id(id)

@router.post('/blog')
def create_blog(dto: CreateBlog):
    return blog_service.create_blog(dto)

@router.put('/blog/{id}')
def update_blog(id: UUID = Path(...), dto: UpdateBlog = Body(...)):
    return blog_service.update_blog(id, dto)

@router.delete('/blog/{id}')
def delete_blog(id: UUID):
   return blog_service.delete_blog(id)