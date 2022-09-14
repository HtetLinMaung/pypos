FROM python:bullseye

WORKDIR /app

COPY . .

RUN pip install "fastapi[all]" 
RUN pip install "python-jose[cryptography]"
RUN pip install "passlib[bcrypt]"


CMD [ "uvicorn", "main:app", "--reload" ]