from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.redis import redis_client, QUEUE_NAME
from app.models.task import Task
from app.schemas.task import TaskCreate

router = APIRouter()


@router.post("/tasks")
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        status="pending",
        job_type=task_data.job_type
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    redis_client.rpush(QUEUE_NAME, task.id)

    return {
        "id": task.id,
        "status": task.status,
        "job_type": task.job_type,
        "result": task.result
    }


@router.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return [
        {
            "id": task.id,
            "status": task.status,
            "job_type": task.job_type,
            "result": task.result
        }
        for task in tasks
    ]


@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return {"error": "Task not found"}

    return {
        "id": task.id,
        "status": task.status,
        "job_type": task.job_type,
        "result": task.result
    }
