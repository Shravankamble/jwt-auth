FROM python:3.11-alpine3.18

WORKDIR /app

ARG HASH_KEY=c049838c449b63b0d44e6f2ce940734ed21ed130e2e1382e80e7b21b4893b403

ENV SECRET_KEY=${HASH_KEY}

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]