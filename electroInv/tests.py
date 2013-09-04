from django.test import TestCase
from django.test.client import Client
from IPython import embed
import os,sys,json
FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'
#Local Include
from electroInv.utils import parseDigikeyCSV 


class DigikeyImportTest(TestCase):

    def setUp(self):
        pass

    def testParseCSV(self):
        csvtxt = open(FILE_PATH + 'csv/digikey.csv').read()
        
        data =parseDigikeyCSV(csvtxt)

        print json.dumps(data,indent=4)
