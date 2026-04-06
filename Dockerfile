# Base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the app with gunicorn (production server)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
