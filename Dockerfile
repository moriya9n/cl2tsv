FROM python:slim

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python3", "./cl2tsv.py"]

