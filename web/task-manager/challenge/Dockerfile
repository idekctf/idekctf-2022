FROM python:3.8.16-slim-bullseye

RUN apt update && apt install -y xxd

RUN python3 -m pip install flask pydash

RUN echo "idek{task_complete:capture_the_flag_0f25acc159}" > /flag-$(head -c 16 /dev/urandom | xxd -p).txt

RUN useradd ctf

USER ctf

WORKDIR /app

COPY . .

ENTRYPOINT ["python3", "app.py"]
