from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tasks = []

class Task(BaseModel):
    id: int
    title: str

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    if not task.title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    tasks.append(task)
    return task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for i, t in enumerate(tasks):
        if t.id == id:
            del tasks[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
