FROM ubuntu:latest
COPY calculator.py /app/calculator.py
# CMD sed -i 's/\r$//' /app/calculator.py
COPY testing.py /app/testing.py
#testing for git scm
RUN apt-get update -y && \
    apt-get install -y python3

#testing for gitscm 2
