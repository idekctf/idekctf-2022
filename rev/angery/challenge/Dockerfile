FROM ubuntu:22.04 as chroot

RUN apt-get update && apt-get install -y python3-pip gcc build-essential

RUN mkdir /home/user
WORKDIR /home/user

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY generate.py ./
COPY server.py ./
COPY flag.txt ./

FROM gcr.io/kctf-docker/challenge@sha256:d884e54146b71baf91603d5b73e563eaffc5a42d494b1e32341a5f76363060fb

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg --cwd /home/user -- /usr/bin/python3 server.py"