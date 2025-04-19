# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create data directory for SQLite DB
RUN mkdir -p /app/data

# Copy requirements and install dependencies first (better cache usage)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and config
COPY alembic.ini .
COPY . .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose only port 8585
EXPOSE 8585

# Use entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
