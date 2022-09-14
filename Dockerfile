FROM python:3.11-rc-alpine3.15

WORKDIR /app

COPY . .

RUN pip install "fastapi[all]" 
RUN pip install "python-jose[cryptography]"
RUN pip install "passlib[bcrypt]"


CMD [ "uvicorn", "main:app", "--reload" ]