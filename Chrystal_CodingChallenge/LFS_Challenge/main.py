#!/usr/bin/python3

import time
import base64
import sys
import csv
from faker import Faker

HEADERS = ['first_name', 'last_name', 'address', 'date_of_birth']


def write_csv(file_name, data):
    print(f'Writing {file_name}')
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(data)


def generate(no_of_customers, output_dir):
    data = []
    faker = Faker()
    for _ in range(0, int(no_of_customers)):
        data.append({'first_name': faker.unique.first_name(), 'last_name': faker.unique.last_name(
        ), 'address': faker.address(), 'date_of_birth': faker.date()})
    write_csv(f'{output_dir}/{time.strftime("%Y%m%d-%H%M%S")}.csv', data)


def process(file, output_dir):
    with open(file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
        for d in data:
            d.update((k, anonymise(v))
                     for k, v in d.items() if k not in ["date_of_birth"])
        print(data)
    if (output_dir != None):
        write_csv(
            f'{output_dir}/{time.strftime("%Y%m%d-%H%M%S")}_anonymised.csv', data)


def anonymise(str):
    return base64.b64encode(str.encode('utf-8')).decode('utf-8')


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "generate" and len(sys.argv) == 4:
        generate(sys.argv[2], sys.argv[3])
    elif command == "process" and len(sys.argv) == 3 or len(sys.argv) == 4:
        process(sys.argv[2], None if len(sys.argv) == 3 else sys.argv[3])
    else:
        print("ERROR: unknown command")
