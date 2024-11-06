# Use official Python image
FROM python:3.12

# Set work directory
WORKDIR /src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

WORKDIR /src/app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL="postgres://username:password@postgresserver/dbname"

EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
