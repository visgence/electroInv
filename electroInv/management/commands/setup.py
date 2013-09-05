
#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('syncdb', interactive=False)
        # self.stdout.write('Successfully BLAHHHED' )#DEBUG
                 
        #Comment or uncomment fixtures as needed for loading.
        #ORDER OF FIXTURES MATTERS!! Some have dependencies on others.
        print "Loading test data fixtures"

        fixtures = [
            [
                'electroInv/fixtures/user.json',
                'electroInv/fixtures/vendor.json'
            ]
        ]

        #Load fixtures
        for apps in fixtures:
            for fixture in apps:
                call_command('loaddata', fixture, verbosity=1)

