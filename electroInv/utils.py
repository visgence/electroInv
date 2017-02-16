#!/usr/bin/env python
# Tools for parsing
import csv
import StringIO
import json
import pprint


# Read in csv file and return a list represenging the row data
def parseDigikeyCSV(strdata):

    data = []
    errors = []
    f = StringIO.StringIO(strdata)
    dr = csv.DictReader(f, delimiter=',')
    try:
        for d in dr:
            row = {}
            row['description'] = d['Description']
            row['vendor_sku'] = d['Part Number'].upper()
            row['qty'] = int(d['Quantity'])
            row['price'] = float(d['Unit Price'].replace("$", ''))

            data.append(row)
    except Exception, e:
        errors.append(d)

    return data, errors


# Read in cmp file and return a list representing the data
def parseKiCadCMP(strdata):

    data = []
    return data
