from csv import DictReader

from django.core.management import BaseCommand
from adoptions.models import Humans
from pytz import UTC


ALREDY_LOADED_ERROR_MESSAGE = """
This database has already been loaded man.
"""

class Command(BaseCommand):
    #displays when help is typed
    help = "whats the f*ck do you want?"
    
    def handle(self, *args, **options):
        if Humans.objects.exists():
            print("humans data already loaded...exiting")
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return  
        print("Creating human data")
        for row in DictReader(open("./humans.csv")):
            human = Humans()
            human.first_name = row["first_name"]
            human.last_name = row["last_name"]
            human.email = row["email"]
            human.gender = row["gender"]
            human.address = row["address"]
            human.save()
