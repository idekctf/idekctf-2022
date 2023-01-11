from debian:bullseye

ARG FLAG=idek{FAKE_FLAG}

RUN apt update && apt install -y \
        curl \
        socat \
        pkg-config \
        build-essential \
        autoconf \
        bison \
        re2c \
        libxml2-dev \
        libsqlite3-dev \
        libssl-dev \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://www.php.net/distributions/php-8.2.0.tar.gz > php-8.2.0.tar.gz
RUN echo "435c4c2439db648cdf34236f7cd459f93f943fb788b66723a033610d4a059fc6 php-8.2.0.tar.gz" > php-8.2.0.sig && \
    sha256sum -c php-8.2.0.sig

RUN tar -xvf php-8.2.0.tar.gz

WORKDIR /php-8.2.0/

RUN ./configure --with-openssl --with-ffi && \
    make -j4 && \
    make install

WORKDIR /
RUN rm -rf /php-8.2.0/

COPY phpfun.sh error_handler.php /

RUN chmod +x /phpfun.sh && \
    echo "${FLAG}" > /flag.txt && \
    chmod 444 /flag.txt

RUN useradd ctf
USER ctf

ENTRYPOINT socat \
      TCP-LISTEN:1337,reuseaddr,fork,end-close \
      EXEC:"/phpfun.sh",pty,ctty,stderr,raw,echo=0
