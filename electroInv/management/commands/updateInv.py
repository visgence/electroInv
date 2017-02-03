
#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command
import csv
import json
import delorean
from electroInv.models import Part, Log


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csvfile', nargs='+', type=str)

    def handle(self, *args, **options):

        DATE = delorean.parse("2016-12-31 12:00:00", timezone="US/Mountain").datetime

        self.stdout.write('Update Command args: {}'.format(options))#DEBUG
        csvfile = open(options['csvfile'][0], 'rb')
        update_parts = list(csv.DictReader(csvfile))
        #IPython.embed()

        no_fail = True
        for p in update_parts:
            #Lowercase dict
            p = dict((k.lower(), v) for k, v in p.iteritems())
            part = Part.objects.get(id=int(p['id']))
            if p['part_number'] != part.part_number:
                no_fail = False
                print "'{}' dose not match '{}' for id {}".format(p['part_number'], part.part_number, part.id)
        
        assert no_fail

        for p in update_parts:
            #Lowercase dict
            p = dict((k.lower(), v) for k, v in p.iteritems())
            part = Part.objects.get(id=int(p['id']))
            qty = int(p['qty'])
            
            part.qty = qty
            part.location = p['location']
            part.full_clean()
            print "Updating part: {}".format(part.part_number)
            part._meta.fields[-1].auto_now = False
            #Force lastupdate
            part.lastupdate = DATE
            part.save(note=p['notes'])



