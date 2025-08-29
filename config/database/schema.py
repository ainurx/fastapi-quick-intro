from uuid import uuid4
from sqlalchemy import Uuid, String, Text
from sqlalchemy.dialects.postgresql import UUID
from  sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .database import engine

class Base(DeclarativeBase):
    pass

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(60), nullable=False)
    content: Mapped[str] = mapped_column(Text)
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)