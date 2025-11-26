# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Define environment variable for Chainlit to listen on all interfaces
ENV CHAINLIT_HOST=0.0.0.0
ENV CHAINLIT_PORT=7860

# Run app.py when the container launches
CMD ["chainlit", "run", "app.py", "--headless"]
