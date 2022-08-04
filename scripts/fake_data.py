import os 
import random
from unicodedata import name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easy_store.settings')

import django
django.setup()


from product.models import Manufacturer
from faker import Faker


def set_manufacturer():
    fake = Faker(['en-US'])
    f_name = fake.company()
    slug = f_name.lower()
   
    manufacturer = Manufacturer(
        name = f_name,
        slug= slug,
    )
    manufacturer.save()
    
