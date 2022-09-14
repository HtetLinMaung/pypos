FROM python:bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]