FROM ubuntu:latest
COPY calculator.py /app/calculator.py
# CMD sed -i 's/\r$//' /app/calculator.py
COPY testing.py /app/testing.py

