FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requierements.txt /app/requierements.txt
RUN pip install -r requierements.txt
COPY . /app

CMD python main.py