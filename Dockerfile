# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY app.py .

# Set environment variables with defaults
ENV QR_DATA_URL="https://github.com/Hameed1117"
ENV QR_CODE_DIR="qr_codes"
ENV QR_CODE_FILENAME="github_qr.png"
ENV FILL_COLOR="black"
ENV BACK_COLOR="white"

# Create the output directory
RUN mkdir -p ${QR_CODE_DIR}

# Run the Python script when the container starts
CMD ["python", "app.py"]