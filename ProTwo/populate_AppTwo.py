import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

# Fake Pop_Script
import random
from AppTwo.models import User
from faker import Faker

fakedata = Faker()

def add_user(N=5):
    for entry in range(N):
        fake_name = fakedata.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakedata.email()

        RandUser = User.objects.get_or_create(first_name=fake_firstname, last_name=fake_lastname, email= fake_email)[0]

if __name__=='__main__':
    print('Populating Script!')
    add_user(10)
    print('Populated!')