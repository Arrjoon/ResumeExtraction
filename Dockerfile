# Use a stable base image
FROM python:3.12

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8001
# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
