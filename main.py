from fastapi import FastAPI

from module.blog.blog_controller import router as blog_routes

app = FastAPI()

@app.get('/')
def main():
    return { "message": "Hello" }

app.include_router(blog_routes)