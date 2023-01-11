FROM golang:1.19-alpine

ENV LISTEN_ADDR=":1337"
ENV FLAG="idek{REDACTED}"

WORKDIR /app
COPY readme.go .
RUN go build -o readme readme.go

USER nobody

CMD "/app/readme"
