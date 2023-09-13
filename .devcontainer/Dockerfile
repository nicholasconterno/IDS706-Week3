# Use the official Python base image
FROM python:3.9

# Install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gdb \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirements.txt and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Done
