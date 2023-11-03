FROM python:3.11-alpine as builder

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./main.py ./

RUN apk add binutils
RUN pyinstaller --onefile main.py

FROM alpine as runner

WORKDIR /app

COPY --from=builder /app/dist/main /app/main

CMD [ "/app/main" ]