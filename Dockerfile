# Dockerfile for Identifies AI Backend

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . ./

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "app.py"]
