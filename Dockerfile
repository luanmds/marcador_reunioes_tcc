FROM python:3.9.13-alpine3.15 as base
RUN apk update && apk add g++ libffi-dev


FROM base as builder

WORKDIR /app

COPY app/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app .

EXPOSE 5000

CMD ["python3", "main.py"]