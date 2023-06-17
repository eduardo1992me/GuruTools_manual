from django.test import TestCase
import datetime
from datetime import timedelta, date

# Create your tests here.

#day = datetime(days=1)
date_now = datetime.datetime.today()
print(date_now)
date_now = date_now + timedelta(days=20)

date_tom = datetime.datetime.today()
date_tom = date_tom + timedelta(days=2)




date_tom = str(date_tom.year) + '-' + str(date_tom.month) + '-' + str(date_tom.day)
date_now = str(date_now.year) + '-' + str(date_now.month) + '-' + str(date_now.day)
print(f"Checkin: {date_now}")
print(f"Checkout: {date_tom}")

for i in range(4):
    print(i)

otro_dic = {'prueba':1, 'test':2}

diccionario = {}

for i in range(4):
    diccionario[i] = otro_dic

print(diccionario)


#https://hotelcasasantamaria.mx/es/availability?checkout=2023-07-17&currency=MXN&occupancy=2&checkin=2023-07-16
#https://hotelcasasantamaria.mx/es/availability?checkout=2023-7-17&currency=MXN&occupancy=2&checkin=2023-7-16