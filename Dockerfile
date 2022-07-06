FROM python:3
ENV PYTHONUNBUFFERED TRUE
COPY . .
RUN pip3 install -r requirements.txt