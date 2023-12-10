# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /opt/app

# Copy the current directory contents into the container at /opt/app
COPY . /opt/app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV DEBUG_MODE=True

# Run main.py when the container launches
CMD ["python3", "-m" , "main"]
