# Use a lightweight Python image
FROM python:3.11.2-alpine3.17

# Set the working directory inside the container
WORKDIR /googly_eyes

# Copy the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

CMD ["flask", "--app", "service/src/googly_service", "run"]
