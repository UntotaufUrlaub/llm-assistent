FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install fastapi, uvicorn, python-multipart

EXPOSE 80

# Run the Streamlit app
CMD ["python", "main.py"]
