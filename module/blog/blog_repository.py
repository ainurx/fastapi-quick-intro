from uuid import UUID
from .blog_dto import CreateBlog, UpdateBlog
from config.database.database import session
from config.database.schema import Blog

def get_all():
    result = session.query(Blog).all()
    return result

def get_by_id(id: UUID):
    result = session.query(Blog).filter(Blog.id == id).first()
    return result

def create(dtoBlog: CreateBlog):
    new_blog = Blog(title=dtoBlog.title, content=dtoBlog.content)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)
    return new_blog

def update(id: UUID, dtoBlog: UpdateBlog):
    session.query(Blog).filter(Blog.id == id).update(dtoBlog.model_dump(exclude_unset=True))
    session.commit()
    return session.query(Blog).filter(Blog.id == id).first()
    
def delete(id: UUID):
    session.query(Blog).filter(Blog.id == id).delete()
    session.commit()
