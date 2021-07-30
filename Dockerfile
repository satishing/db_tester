FROM python:3.8

WORKDIR /app
COPY requirements.txt templates app.py /app/
RUN pip install -r requirements.txt
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]