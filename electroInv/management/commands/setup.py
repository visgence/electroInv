
#system imports
from django.core.management.base import BaseCommand
from django.core.management import call_command
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        # self.stdout.write('Successfully BLAHHHED' )#DEBUG
        call_command('migrate', fake=True)
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

        with open('electroInv/fixtures/parts.json') as file:
            data = json.load(file)
            newobj = []
            names = []
            count = 0
            for i in data['data']:
                newobj.append(
                    {
                        "pk": i['pk'],
                        "model": "electroInv.vendor",
                        "fields": {
                            "name": "Digi-Key",
                            "website": i['__unicode__']
                        }
                    }
                )
                newFixture = 'electroinv/fixtures/data{}.json'.format(count)
                count += 1
                names.append(newFixture)
                with open(newFixture, 'w') as outfile:
                    json.dump(newobj, outfile)

        for fix in names:
            call_command('loaddata', fix, verbosity=1)

