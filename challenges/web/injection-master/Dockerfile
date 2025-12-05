# Use a small, stable Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the challenge folder into the container
COPY . /app

# Install Flask (needed to run the web server)
RUN pip install flask

# Expose port 5000 so you can access the challenge in your browser
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
