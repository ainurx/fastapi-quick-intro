from fastapi import FastAPI, HTTPException

from typing import List
from uuid import UUID, uuid4
from model import Blog, updateBlog, CreateBlog

app = FastAPI()

blogRepository: List[Blog] = [
    Blog(
        id=uuid4(),
        title="One piece",
        content="it's real"
    ),
    Blog(
        id=uuid4(),
        title="My hero academia",
        content="number one hero"
    )
]


@app.get('/')
def main():
    return { "message": "Hello" }

@app.get('/blog')
def getBlogs():
    return blogRepository

@app.post('/blog')
def createBlog(blog: CreateBlog):
    blogRepository.append(blog)
    return blog

@app.get('/blog/{id}')
def findById(id:UUID):
    itemIndex = next((i for i, item in enumerate(blogRepository) if item.id == id), None)
    if itemIndex:
        return blogRepository[itemIndex]
    else: 
        raise HTTPException(status_code = 404, detail="blog not found")

@app.put('/blog/{id}')
def updateBlog(id: UUID, blog: updateBlog):
    itemIndex = next((i for i, item in enumerate(blogRepository) if item.id == id), None)

    if itemIndex:
        oldBlog = blogRepository[itemIndex]
        blogRepository[itemIndex] = oldBlog.model_copy(update=blog.dict(exclude_unset = True))
        return blogRepository[itemIndex]
    else:
        return { "message": "blog not found"}

@app.delete('/blog/{id}')
def deleteBlog(id: UUID):
    itemIndex = next((i for i, item in enumerate(blogRepository) if item.id == id), None) 
    if itemIndex: 
        del blogRepository[itemIndex]
        return { "message": f"Blog {id} deleted"}
    else:    
        return { "message": f"Blog {id} not found"}