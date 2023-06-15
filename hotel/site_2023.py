from bs4 import BeautifulSoup
import requests
import lxml
import time

target_url = "https://hotelcasasantamaria.mx/es/availability?checkout=2023-07-24&currency=MXN&occupancy=2&checkin=2023-07-23"

l=list()
g=list()
o={}
k={}

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')