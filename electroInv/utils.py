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
            print json.dumps(d, indent=2)
            row = {}
            if 'Description' in d:
                row['description'] = d['Description']
            else:
                errors.append('Description field is missing')

            if 'DigiKey Part #' in d:
                row['vendor_sku'] = d['DigiKey Part #'].upper()
            else:
                errors.append('Part Number field is missing')

            if 'Quantity' in d:
                row['qty'] = int(d['Quantity'])
            else:
                errors.append('Quantity field is missing')

            if 'Unit Price' in d:
                row['price'] = float(d['Unit Price'].replace(" $", ""))
            else:
                errors.append('Unit Price USD field is missing')

            if 'Manufacturer Part Number' in d:
                row['part_number'] = d['Manufacturer Part Number']

            data.append(row)
    except Exception, e:
        errors.append(e)

    return data, errors


# Read in cmp file and return a list representing the data
def parseKiCadCMP(strdata):

    data = []
    return data
