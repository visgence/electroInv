#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command
import json
import IPython
from electroInv.models import Part, Log


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "from electroInv.models import Part, Log"
        IPython.embed()
