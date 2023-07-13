from bs4 import BeautifulSoup
import requests
import lxml
import time
import datetime
from datetime import timedelta, date

# target_url = "https://cabinasyafethosa.com"

# "https://hotelcasasantamaria.mx/es/availability?checkout=2023-07-24&currency=MXN&occupancy=2&checkin=2023-07-23" <--- URL completa

class Monitoreo_sito_2023:
    def __init__(self, url, cycle):
        self.url = url
        self.cycle = cycle



    def monitoreoSitio_2023(self):
        l=[]  #<-- Room
        g=[]  #<-- price
        cycle = 0
        room_and_price_gen = {}




        for i in range(4):    
            if cycle == 0:
                date_chkin = date.today() + timedelta(days=1)
                date_chkout = date.today() + timedelta(days=2)


                target_url = self.url + f"/es/availability?checkout={date_chkout}&currency=MXN&occupancy=2&checkin={date_chkin}"


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
                room_and_price_gen[str(date_chkin)] = room_and_price
                cycle += 1
                l = []

                # return(room_and_price)
            
            elif cycle == 1:
                date_chkin = date.today() + timedelta(days=7)
                date_chkout = date.today() + timedelta(days=8)


                target_url = self.url + f"/es/availability?checkout={date_chkout}&currency=MXN&occupancy=2&checkin={date_chkin}"


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
                room_and_price_gen[str(date_chkin)] = room_and_price
                cycle += 1
                l = []

                # return(room_and_price)

            elif cycle == 2:

                date_chkin = date.today() + timedelta(days=30)
                date_chkout = date.today() + timedelta(days=31)


                target_url = self.url + f"/es/availability?checkout={date_chkout}&currency=MXN&occupancy=2&checkin={date_chkin}"


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
                room_and_price_gen[str(date_chkin)] = room_and_price
                cycle += 1
                l = []

                # return(room_and_price)

            elif cycle == 3:
                date_chkin = date.today() + timedelta(days=90)
                date_chkout = date.today() + timedelta(days=91)



                target_url = self.url + f"/es/availability?checkout={date_chkout}&currency=MXN&occupancy=2&checkin={date_chkin}"


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
                room_and_price_gen[str(date_chkin)] = room_and_price
                cycle += 1
                l = []

                # return(room_and_price)
        return room_and_price_gen

            


