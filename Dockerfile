FROM python:3.11-alpine3.18

WORKDIR /app

# your hash key comes here, use cmd(openssl rand -hex 32) to generate a hash,
# this below hashed key is used for testing.
ARG HASH_KEY=c049838c449b63b0d44e6f2ce940734ed21ed130e2e1382e80e7b21b4893b403

# don't share your hash in public repositories like this 
ENV SECRET_KEY=${HASH_KEY}

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]