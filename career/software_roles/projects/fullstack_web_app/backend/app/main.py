"""FastAPI application entrypoint: app config, CORS, and REST routes."""
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

# Create tables on startup (fine for SQLite / demo; use Alembic for real migrations).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Tracker API",
    description="A small REST API for managing tasks (CRUD) built with FastAPI + SQLAlchemy.",
    version="1.0.0",
)

# CORS — allow the Vite dev server and any origins listed in ALLOWED_ORIGINS.
default_origins = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"
allowed_origins = os.getenv("ALLOWED_ORIGINS", default_origins).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in allowed_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "service": "Task Tracker API", "docs": "/docs"}


@app.get("/api/health", tags=["health"])
def health():
    return {"status": "healthy"}


@app.get("/api/tasks", response_model=List[schemas.TaskOut], tags=["tasks"])
def list_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)


@app.post(
    "/api/tasks",
    response_model=schemas.TaskOut,
    status_code=status.HTTP_201_CREATED,
    tags=["tasks"],
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get("/api/tasks/{task_id}", response_model=schemas.TaskOut, tags=["tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/api/tasks/{task_id}", response_model=schemas.TaskOut, tags=["tasks"])
def update_task(
    task_id: int, updates: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, db_task, updates)


@app.delete(
    "/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"]
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, db_task)
    return None
