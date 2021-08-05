import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chickenfood.settings")
django.setup()

from products.models import *

CSV_PATH_LOCATION = "product.csv"

def insert_brand():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Brand.objects.create(
                name  = row[0],
                image = row[1]
            )

def insert_type():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Type.objects.create(
                name  = row[0]
            )

def insert_product():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            brand = Brand.objects.get(name=row[2])
            type  = Type.objects.get(name=row[3])

            Product.objects.create(
                name  = row[0],
                price = row[1],
                brand = brand,
                type  = type,
                like_number = int(row[4]),
                thumbnail = row[5],
                detail_image = row[6],
                element = row[7],
                weight = row[8]
            )

insert_product()