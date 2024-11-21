import re
from urllib import response
import uuid
from fastapi import FastAPI
from pydantic import BaseModel  # Fixed typo: "pydentic" -> "pydantic"
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Task(BaseModel):
    id: Optional[UUID] = None  
    title: str
    description: Optional[str] = None  
    completed: bool = False

tasks = [] 

@app.get("/tasks/", response_model= Task)
def create_task(task:Task):
    task.id = uuid4()
    tasks.append(task)
    return task
@app.get("/")  
def read_tasks():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)




