# Latitude Coding Challenge

## Features

- Generate CSV file for a configurable amount of customers
- Process customer data and anonymise sensitive data
- Generate anonymised CSV file

## Requirements

Python 3 is required to run this application.

## Installation

```
pip3 install Faker
```

This application uses Faker to generate random data. In a real world scenariom, we would likely be fetching this data from a database.

## Usage

```
python3 main.py generate 1000
```

This 3rd argument denotes how many customers to generate data for

```
python3 main.py process ./file.csv [./output]
```

This will process csv data from the local file system. The last argument is optional and denotes where we would like to output our anonymised data (in csv format)

## TODO:

- Setup venv to manage Python environment (e.g. version and dependencies)
- Represent User data as an object
