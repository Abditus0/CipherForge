FROM python:3.9-slim

WORKDIR /app

# Install Flask
RUN pip install flask

# Copy all challenge files
COPY app.py .
COPY init_db.py .
COPY flag.txt .

# Initialize database
RUN python init_db.py

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]