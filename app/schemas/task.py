from pydantic import BaseModel


class TaskCreate(BaseModel):
    job_type: str = "report_generation"
