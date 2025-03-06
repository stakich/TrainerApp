# Use an official Python 3 slim image as the base
FROM python:3.10-slim

# Set environment variables for Python (no bytecode .pyc files and stdout/stderr unbuffered)
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

# Install system dependencies (if any, e.g. for psycopg2). 
# Here we install gcc and libpq-dev for PostgreSQL compilation; if using psycopg2-binary, this may not be needed.
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies separately to leverage caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Django/Gunicorn will run on
EXPOSE 8000

# Default command to run the app using Gunicorn WSGI server
CMD ["gunicorn", "TrainerApp.wsgi:application", "--bind", "0.0.0.0:8000"]
