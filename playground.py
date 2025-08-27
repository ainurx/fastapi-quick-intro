from typing import List
from uuid import uuid4
from model import Blog

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
    ),
    Blog(
        id=uuid4(),
        title="Boruto",
        content="Sasuke no. 1"
    )
]

print(f"blogRepository: {len(blogRepository)}")

for blog in blogRepository:
    print(blog.model_dump())

# List manipulation
# find by id 
    # return dict
    # retrun index
# Update one of blog
# Deleta blog from list

print("= AFTER INTERPRETATION =")
onePiece = list(filter(lambda item: item.title == "One piece", blogRepository))
print(*onePiece)

itemIndex = next(i for i, item in enumerate(blogRepository) if item.title == "Boruto")
oldBlog = blogRepository[itemIndex]
blogRepository[itemIndex] = oldBlog.model_copy(update={"title": "Naruto next generation"})
# blogRepository[itemIndex] = Blog(**oldBlog.__dict__, title="Naruto next generation")
# del blogRepository[itemIndex]
print(blogRepository)
