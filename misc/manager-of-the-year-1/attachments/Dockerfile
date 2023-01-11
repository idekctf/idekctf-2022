FROM python:3.9-slim

RUN python -m pip install numpy==1.19.5
RUN python -m pip install pandas==1.1.5
RUN python -m pip install scikit-learn==0.24.2

WORKDIR /home/ctf

COPY flag.txt .
COPY chall.py .
COPY secret.py .

CMD ["python", "chall.py"]
