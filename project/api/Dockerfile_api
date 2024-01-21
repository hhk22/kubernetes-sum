
FROM python:3.9

RUN mkdir -p /api
RUN mkdir -p /api/html
RUN mkdir -p /api/sentences
WORKDIR /api

COPY app.py ./app.py
COPY utils.py ./utils.py
COPY html/ ./html
COPY sentences/ ./sentences

RUN pip install --no-cache-dir fastapi uvicorn requests

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]