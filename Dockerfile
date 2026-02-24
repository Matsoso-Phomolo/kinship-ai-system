# Use a lightweight Python image
FROM python:3.14-slim

# Install SWI-Prolog and necessary tools
RUN apt-get update && \
    apt-get install -y swi-prolog && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your application files
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app will run on
EXPOSE 10000

# Start the Flask app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
