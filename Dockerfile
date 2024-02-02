FROM ubuntu:latest
CMD sed -i 's/\r$//' calculator.sh
COPY calculator.sh /app/calculator.sh
