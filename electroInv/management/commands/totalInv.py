
#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command
import json
import IPython
from electroInv.models import Part, Log


class Command(BaseCommand):

    def handle(self, *args, **options):

        total = 0.0
        for p in Part.objects.all():
            value = p.qty * p.price
            if value >= 100:
                print "Part {} is valued at {}".format(p.part_number, value)
            total += value

        print "Total is ${}".format(total)



