FROM python:3

RUN apt-get update
RUN apt-get install -y socat
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/chal
WORKDIR /opt/chal

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY flag.txt server.py ./

RUN adduser chal
USER chal
ENV FLAG="idek{St@rburst_str3@m!!!}"
CMD socat -v -T60 tcp-listen:1337,fork,reuseaddr system:"python3 server.py 2>&1"
