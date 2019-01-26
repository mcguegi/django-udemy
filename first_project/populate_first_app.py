import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


## Fake POPULATION SCRIPT

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker 

fakegen = Faker()
topics = ["Beauty","News", "Lettering", "Games" , "Marketplace" , "Search"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #Generate fake data for the webpage
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        #Create the entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #Create a fake access record for that website
        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("ejecutando script de populating")
    populate(20)
    print("Job done!")