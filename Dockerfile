# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the entrypoint for the web server
# Gunicorn will run the main.py application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
