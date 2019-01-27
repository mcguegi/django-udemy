import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


## Fake POPULATION SCRIPT

import random
from AppTwo.models import User
from faker import Faker 

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        #Generate fake data for the user
        fake_name = fakegen.name()
        
        fake_fname = fake_name.split( )[0]
        fake_lname = fake_name.split( )[1]
        fake_email = fakegen.email()


        #Create the entry
        user = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname, email=fake_email)[0]



if __name__ == '__main__':
    print("ejecutando script de populating")
    populate(20)
    print("Job done!")