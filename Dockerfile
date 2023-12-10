# Use a slim version of the Python 3.9 image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /opt/app

# Install PostgreSQL development files required for psycopg2
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /opt/app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /opt/app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV DEBUG_MODE=True

# Run main.py when the container launches
CMD ["python3", "-m", "main"]
