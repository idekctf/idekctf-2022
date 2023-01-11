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
ENV FLAG="idek{H0n3sty_1s_th3_b3st_p0l1cy?_N0p3_b3c4us3_w3_ar3_h@ck3rs!}"
CMD socat -v -T60 tcp-listen:1337,fork,reuseaddr system:"python3 server.py 2>&1"
