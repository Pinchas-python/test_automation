# Use Playwright Docker image
FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

# Set the working directory inside the container
WORKDIR /app

# Install additional system dependencies (if needed)
RUN apt-get update && apt-get install -y xvfb && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the default command to run tests with Playwright
CMD ["xvfb-run", "--auto-servernum", "--server-args=-screen 0 1280x720x24", "pytest", "-v", "--alluredir=/app/allure-results"]

