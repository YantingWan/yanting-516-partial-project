# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /ai_services on Docker
WORKDIR /ai_services

# Copy the current directory contents into the container at /ai_services
COPY . /ai_services

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available
EXPOSE 8000

# Run server.py when the container launches
CMD["python","server.py"]