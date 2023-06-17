from bs4 import BeautifulSoup
import requests
import lxml
import time
import datetime
from datetime import timedelta, date



l=[]
g=[]
o={}
k={}
cycle = 0
room_and_price_gen = {}


target_url = "https://hotelcasasantamaria.mx/es/availability?checkout=2023-07-17&currency=MXN&occupancy=2&checkin=2023-07-16"


headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')

h2 = soup.find_all("h2")
for room in h2:
    l.append(room.text)
del l[0]
# print(l)

p = soup.find_all("p", class_='text-2xl font-bold')
for price in p:
    g.append(price.text[4:])
# print(g)

room_and_price = {l:g for (l,g) in zip(l,g)}
room_and_price_gen["2023-07-23"] = room_and_price

print(room_and_price_gen)
