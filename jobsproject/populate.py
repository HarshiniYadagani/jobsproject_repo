import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()

from firstapp.models import Banglorejobs,Hydjobs,Punejobs
from faker import Faker
from random import *
fake=Faker()

def phnnum():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n,location_model):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        frole=fake.random_element(elements=('SDE','MTS','Full Stack Developer','App Developer','Data Engineer'))
        feleg=fake.random_element(elements=('B.Tech','M.Tech','PhD','MCA','Degree'))
        floc=fake.address()
        femail=fake.email()
        fphn=phnnum()
        location_model.objects.get_or_create(
            date=fdate,
            company=fcompany,
            role=frole,
            eligibility=feleg,
            location=floc,
            email=femail,
            contactnumber=fphn,
        )

n=int(input("Enter number of records: "))
populate(n, Banglorejobs)  # For Bangalore jobs
populate(n, Hydjobs)       # For Hyderabad jobs
populate(n, Punejobs)      # For Pune jobs

print(f'{n} records inserted successfully')
