from datetime import datetime
from email import message
from turtle import title
from typing import Text, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from datetime import datetime
from uuid import uuid4


app = FastAPI()

posts = []

#post model
class post(BaseModel):
        id:Optional[str]
        title:str
        author:str
        content: Text
        #creamos una fecha automatica apenas se cree
        created_at: datetime = datetime.now()
        published_at: Optional[datetime]
        published: bool = False

#sitio web incial
@app.get('/')
def rear_root():
    return {"welcome": "welcome to my REST-API"}

#Solicitud para ver post
@app.get('/posts')
def get_posts():
    return posts

#agregar un post
@app.post('/posts')
def save_post(post: post):
    post.id= str(uuid4())
    posts.append(post.dict())
    return posts[-1]
#Solucitar post al servidor
@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post['id']==post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")
#eliminar post al servidor
@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
            if post["id"]== post_id:
                posts.pop(index)
                return {"message": "Post has been deleted successful"}
    raise HTTPException(status_code=404, detail="Post Not Found")
#editar post
@app.put('/posts/{post_id}')
def update_post(post_id: str, updatepost: post):
    for index, post in enumerate(posts):
        if post["id"]== post_id:
            posts[index]["title"]=updatepost.title
            posts[index]["author"]=updatepost.author
            posts[index]["content"]=updatepost.content
            return {"message": "Post has been updated successful"}
    raise HTTPException(status_code=404, detail="Post Not Found")
        
            
        