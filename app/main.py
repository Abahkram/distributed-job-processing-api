from app.api.tasks import router as tasks_router
from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import task  

app = FastAPI(
    title="Distributed Job Processing API",
    description="API for submitting and tracking background jobs",
    version="1.0.0"
)

app.include_router(tasks_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Job Processing API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
