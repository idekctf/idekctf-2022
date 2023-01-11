FROM python:3.8.2-slim-buster

RUN apt update && apt install -y gcc socat

RUN /usr/sbin/useradd --no-create-home -u 1000 user

WORKDIR /home/user

ADD jail.py readflag.c ./

ADD flag.txt /flag

RUN gcc readflag.c -static -o /readflag

RUN chmod 400 /flag

RUN chmod +x jail.py

RUN chmod +s /readflag

USER user

ENTRYPOINT socat \
	TCP-LISTEN:1337,reuseaddr,fork,end-close \
	EXEC:"./jail.py",pty,ctty,stderr,raw,echo=0
