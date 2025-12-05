FROM python:3.9-slim

WORKDIR /app

# Install Flask
RUN pip install flask

# Copy challenge files
COPY app.py .
COPY flag.txt .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]