from app.schemas.task import TaskCreate
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
import time

from app.core.database import get_db, SessionLocal
from app.models.task import Task

router = APIRouter()


def process_task(task_id: int):
    db = SessionLocal()

    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if task is None:
            return

        task.status = "running"
        db.commit()

        time.sleep(10)

        task.status = "completed"

        if task.job_type == "report_generation":
            task.result = "Report generated successfully"

        elif task.job_type == "data_import":
            task.result = "Data imported successfully"

        elif task.job_type == "email_sending":
            task.result = "Emails sent successfully"

        else:
            task.result = f"Job '{task.job_type}' processed successfully"

        db.commit()

    except Exception as error:
        task.status = "failed"
        task.result = str(error)
        db.commit()

    finally:
        db.close()


@router.post("/tasks")
def create_task(
    task_data: TaskCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    task = Task(
        status="pending",
        job_type = task_data.job_type
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    background_tasks.add_task(process_task, task.id)

    return {
        "id": task.id,
        "status": task.status,
        "job_type": task.job_type,
        "result": task.result
    }


@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return {"error": "Task not found"}

    return {
        "id": task.id,
        "job_type": task.job_type,
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
