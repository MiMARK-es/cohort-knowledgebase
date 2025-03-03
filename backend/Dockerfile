FROM python:3.9

WORKDIR /app

# Set PYTHONPATH so Alembic can find `app`
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run migrations before starting the FastAPI server
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000