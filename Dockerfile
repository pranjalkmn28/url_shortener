# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /url_shortner

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

    
# Copy the current directory contents into the container at /app
COPY . /url_shortner/


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]