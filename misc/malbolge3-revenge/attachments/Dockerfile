FROM python:3.11.1-slim as chroot

RUN apt update && apt install -y \
        socat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /home/user
WORKDIR /home/user

RUN mkdir directory_with_a_very_very_long_name_i_wonder_why_its_so_long
COPY flag_file_with_a_very_long_name.txt directory_with_a_very_very_long_name_i_wonder_why_its_so_long
COPY malbolge.py ./
COPY 4_heresy.py ./
COPY banner ./

CMD socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"/usr/local/bin/python 4_heresy.py"
