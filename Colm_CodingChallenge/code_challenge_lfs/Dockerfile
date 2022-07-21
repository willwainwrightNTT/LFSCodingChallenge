FROM python:3.7

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir faker && \
    pip install --no-cache-dir pandas
	
RUN mkdir -p /output/data/
RUN chown -R 0777:0655 /output/data/
WORKDIR /output

COPY ./app/* /output/

CMD ["python", "./lfs_script.py"]