FROM python:3.11-slim

ENV PORT=50052
ENV MODEL_PATH=/app/models/model.pkl
ENV MODEL_VERSION=v1.0.0
ENV BIND_ADDR=0.0.0.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 50052

CMD ["python", "-m", "server.server"]