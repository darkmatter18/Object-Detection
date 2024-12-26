# Object Detection


## Introduction

This project is a simple object detection project using the Detectron2 library.


## Usage

1. Clone the repository
2. ```bash
   docker compose up
   ```

## API

Swagger UI: http://localhost:8000/docs

### Endpoints

1. `POST /detect`
   
   Create a Detection task using an image

2. `GET /detect/{task_id}`
   
   Get the result of a Detection task


## Tools

1. FastAPI (for API)
2. Celery (for async tasks)
3. Redis (for message broker)
4. Docker (for containerization)


## References

- [Detectron2](https://github.com/facebookresearch/detectron2)
- [PyTorch](https://pytorch.org/)
- [Docker](https://www.docker.com/)

