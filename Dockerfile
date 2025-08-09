FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install streamlit

# Expose the Streamlit default port
EXPOSE 80

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
