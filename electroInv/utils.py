#!/usr/bin/env python
#Tools for parsing 
import csv
import StringIO
import json
import pprint

#Read in csv file and return a list represenging the row data
def parseDigikeyCSV(strdata):   
    
    data = []

    f = StringIO.StringIO(strdata)
    dr = csv.DictReader(f,delimiter=',')
  
    for d in dr:
        
        row = {}
        row['description'] = d['Description']
        row['vendor_sku'] = d['Part Number'].upper()
        row['qty'] = int(d['Quantity'])
        row['price'] = float(d['Unit Price USD'].replace("$",''))
       
        data.append(row)
        
    return data


#Read in cmp file and return a list representing the data
def parseKiCadCMP(strdata):
    
    data = []
    return data
    



