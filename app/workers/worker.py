import time

from app.core.database import SessionLocal
from app.core.redis import redis_client, QUEUE_NAME
from app.models.task import Task


def process_task(task: Task):
    time.sleep(5)

    if task.job_type == "report_generation":
        return "Report generated successfully"

    if task.job_type == "data_import":
        return "Data imported successfully"

    if task.job_type == "email_sending":
        return "Emails sent successfully"

    return f"Job '{task.job_type}' processed successfully"


def run_worker():
    print("Worker started. Waiting for jobs...")

    while True:
        _, task_id = redis_client.blpop(QUEUE_NAME)

        db = SessionLocal()

        try:
            task = db.query(Task).filter(Task.id == int(task_id)).first()

            if task is None:
                continue

            task.status = "running"
            db.commit()

            result = process_task(task)

            task.status = "completed"
            task.result = result
            db.commit()

            print(f"Task {task.id} completed")

        except Exception as error:
            if task:
                task.status = "failed"
                task.result = str(error)
                db.commit()

        finally:
            db.close()


if __name__ == "__main__":
    run_worker()
