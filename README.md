# Distributed Job Processing API

Backend service for submitting and processing background jobs asynchronously.

## Features

- Create background jobs via REST API
- Track job status (pending, running, completed, failed)
- Support for multiple job types:
  - report_generation
  - data_import
  - email_sending
- Asynchronous processing using FastAPI background tasks
- SQLite database with SQLAlchemy ORM

## API Endpoints

### Create Job
POST /tasks

Request:
```json
{
  "job_type": "data_import"
}

```

### Get Job by ID
GET /tasks/{id}

### Get All Jobs
GET /tasks

## Job Lifecycle

```text
pending → running → completed
```

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## How to Run

```bash
uvicorn app.main:app --reload
```

## API Documentation

After running the server, open:

```text
http://127.0.0.1:8000/docs
```
