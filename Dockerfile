# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your app code into the container
COPY main.py .

# Install Flask
RUN pip install flask

# Expose the port your app runs on
EXPOSE 5000

# Command to run your app
CMD ["python", "main.py"]
