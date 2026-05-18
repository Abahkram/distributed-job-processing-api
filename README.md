# Distributed Job Processing API

A backend system for asynchronous task processing built with FastAPI, PostgreSQL, Redis, and Docker Compose.

## Overview

This project demonstrates a distributed background job processing architecture where tasks are submitted through a REST API, placed into a Redis queue, processed by a worker service, and stored in PostgreSQL.

The system simulates real-world backend workflows such as:
- report generation
- data imports
- email processing
- asynchronous background jobs

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Docker Compose
- Uvicorn

---

# Features

- Create background jobs through REST API
- Queue-based task processing with Redis
- Worker service for asynchronous execution
- PostgreSQL persistence
- Task lifecycle management:
  - pending
  - running
  - completed
  - failed
- Dockerized infrastructure
- Swagger/OpenAPI documentation

---

# Architecture

Client → FastAPI API → Redis Queue → Worker → PostgreSQL

---

# API Endpoints

## Create Task

```http
POST /tasks

Example request:

{
  "job_type": "report_generation"
}

Supported job types:

report_generation
data_import
email_sending
Get All Tasks
GET /tasks
Get Task By ID
GET /tasks/{task_id}
Local Development Setup
Install dependencies
pip install -r requirements.txt
Run FastAPI
uvicorn app.main:app --reload
Run worker
python -m app.workers.worker
Swagger docs
http://127.0.0.1:8000/docs
Future Improvements
JWT authentication
Retry logic
Tests
CI/CD
Celery integration
Author

Markhabo Davlatova