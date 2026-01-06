from fastapi import Depends, Header, FastAPI, HTTPException, status
from pydantic import BaseModel
import os
API_KEY = os.getenv("BLOG_API_KEY")

app = FastAPI()

# Defines the post class
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool

# Defines the create post class
class PostCreate(BaseModel):
    title: str
    content: str
    published: bool

# Storage for posts
posts: list[Post] = [ ]



# A function to check for and validate the API key
def checkKey(x_api_key: str = Header(default=None)):
    if API_KEY is None:
        raise HTTPException(
            status_code=500,
            detail="API key is not configured"
        )
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    
@app.get("/")
async def root():
    return {"message": "Welcome to Nick's API-based blog project."}

# Routes (endpoints)

# An end point and a function that returns a list of all posts
@app.get("/posts")
def getPosts():
    return posts

# An end point and a function that creates a new post
@app.post("/posts")
def createPost(
    post: PostCreate, 
    api_key : str = Depends(checkKey)
):
    newId = len(posts) + 1

    newPost = Post(
        id = newId,
        title = post.title,
        content = post.content,
        published = post.published
    )

    posts.append(newPost)
    return newPost

# An endpoint and function that return the post associated with an id
@app.get("/posts/{postId}")
def getPost(postId: int):
    for post in posts:
        if post.id == postId:
            return post
    raise HTTPException(
        status_code=404,
        detail="Post not found"
    )

# An endpoint and a function that deletes an existing post
@app.delete("/posts/{postId}", status_code=status.HTTP_204_NO_CONTENT)
def deletePost(
    postId: int, 
    api_key = Depends(checkKey)):
    for index, post in enumerate(posts):
        if post.id == postId:
            posts.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Post not found"
    )


        

