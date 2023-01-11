FROM ubuntu:latest as chroot

## General stuff
RUN apt update && apt upgrade
RUN apt-get install qemu-system-x86 -y
RUN /usr/sbin/useradd --no-create-home -u 1000 user

# RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
# RUN echo "ctf:ctf" | chpasswd
# WORKDIR /home/ctf

## Challenge files
COPY initramfs.cpio.gz /home/user/
COPY run.sh /home/user/
COPY vmlinuz /home/user/

FROM gcr.io/kctf-docker/challenge@sha256:d884e54146b71baf91603d5b73e563eaffc5a42d494b1e32341a5f76363060fb

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /home/user/run.sh"