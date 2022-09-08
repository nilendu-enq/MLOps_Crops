FROM python:3.9.7-slim-bullseye

WORKDIR /

RUN pip install flask pandas flask_cors sklearn
COPY server/model_server.py /
COPY models/ /models/
COPY dataset/split/y_label.csv /dataset/split/y_label.csv

ENTRYPOINT ["python", "model_server.py"]