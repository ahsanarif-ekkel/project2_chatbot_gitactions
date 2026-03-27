FROM python:3.13-slim

# Set working directory in container
WORKDIR /app

# Install dependencies first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose the port your app listens on
EXPOSE 8080

# Run your app
CMD ["python", "main.py"]
