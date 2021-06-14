FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install python-multipart
COPY ./app /app