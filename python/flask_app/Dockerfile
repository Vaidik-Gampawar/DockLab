# base image
FROM python:3.11

# working directory
WORKDIR /app

# code for container
COPY . .

# libraries
RUN pip install -r requirements.txt

# run
CMD ["python3.11", "app.py"]
