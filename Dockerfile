FROM python:3.11.2-alpine3.17

WORKDIR /googly_eyes

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "--app", "service/src/googly_service", "run"]
