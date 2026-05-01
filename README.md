# Distributed Job Processing API

Backend service for asynchronous job processing using Redis queue and worker architecture.

## Architecture

```
Client → FastAPI → Redis Queue → Worker → Database
```

## Features

- Create background jobs via REST API
- Track job status (pending, running, completed, failed)
- Support multiple job types:
  - report_generation
  - data_import
  - email_sending
- Redis queue for task distribution
- Background worker for processing jobs

## API Endpoints

### Create Job
POST /tasks

```json
{
  "job_type": "data_import"
}
```

### Get Job
GET /tasks/{id}

### Get All Jobs
GET /tasks

## Job Lifecycle

```
pending → running → completed
```

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Redis

## How to Run

### 1. Start Redis
```bash
redis-server
```

### 2. Run API
```bash
uvicorn app.main:app --reload
```

### 3. Run Worker
```bash
python -m app.workers.worker
```

## Example Response

```json
{
  "id": 1,
  "status": "completed",
  "job_type": "data_import",
  "result": "Data imported successfully"
}
```
