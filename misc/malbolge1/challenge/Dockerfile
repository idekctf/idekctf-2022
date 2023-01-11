FROM python:3.11.1-slim as chroot

RUN mkdir /home/user
WORKDIR /home/user

RUN mkdir directory_with_a_very_very_long_name_i_wonder_why_its_so_long
COPY flag_file_with_a_very_long_name.txt directory_with_a_very_very_long_name_i_wonder_why_its_so_long
COPY malbolge.py ./
COPY 1_gluttony.py ./
COPY banner ./

FROM gcr.io/kctf-docker/challenge@sha256:501458c0426acc3b5a74a661791271faf0dca6555b46bfb76f944d2558bd08d5

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"nsjail --config /home/user/nsjail.cfg --cwd /home/user -- /usr/local/bin/python 1_gluttony.py"
