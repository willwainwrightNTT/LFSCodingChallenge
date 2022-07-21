FROM python:3.7

RUN mkdir -p /app/output/
RUN chown -R 0777:0655 /app/output/
WORKDIR /app

COPY ./app/* /app/

CMD ["python", "./fwf_parser_test.py"]
