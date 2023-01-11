FROM golang:1.19-alpine

ENV LISTEN_ADDR=":1337"
ENV FLAG="idek{BufF3r_0wn3rsh1p_c4n_b1t3!}"

WORKDIR /app
COPY readme.go .
RUN go build -o readme readme.go

USER nobody

CMD "/app/readme"
