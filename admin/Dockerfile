FROM python:3.9
ENV venv 1
WORKDIR /app
COPY requierements.txt /app/requierements.txt
RUN pip install -r requierements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000