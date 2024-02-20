FROM ubuntu:latest
COPY calculator.py /app/calculator.py
# CMD sed -i 's/\r$//' /app/calculator.py
COPY testing.py /app/testing.py
#testing for git scm
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \


