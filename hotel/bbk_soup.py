import requests
from bs4 import BeautifulSoup
from datetime import timedelta, date


class Monitoreo_booking:
    def __init__(self, url, cycle):
        self.url = url
        self.cycle = cycle

    def monitoreo_bbk(self):
        l=[]
        g=[]
        price_local = []
        k={} #<-- room
        rooms_and_price_gen = {}
        room_list = []
        price_list = []
        room_and_price_temp = {}
        cycle = 0

        for i in range(4):
            if i == 0:
                # print(f"Vamos en ciclo: {i}")
                date_chkin = date.today() + timedelta(days=1)
                date_chkout = date.today() + timedelta(days=2)
                # target_url = self.url_convert(self.url)
                posicion = 0

                for i in self.url:
                    if i == "?":
                        date_chkin = date.today() + timedelta(days=1)
                        date_chkout = date.today() + timedelta(days=2)
                        target_url = self.url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
                    posicion += 1



                # print(f"La url con la que se esta trabajando es {target_url}")
                headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

                resp = requests.get(target_url, headers=headers)
                soup = BeautifulSoup(resp.text, 'lxml')

                ids = []

                try:
                    tr = soup.find_all("tr")
                except:
                    tr = None

                for y in range(0,len(tr)):
                    try:
                        id = tr[y].get('data-block-id')
                    except:
                        id = None

                    if id is not None:
                        ids.append(id)

                # print("ids are ",len(ids))

                for m in range(0,len(ids)):
                    try:
                        allData = soup.find("tr",{"data-block-id":ids[m]})
                        try:
                            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                        except:
                            rooms=None

                        if rooms is None:
                            last_room = rooms.text.replace("\n","")
                        try:
                            k = rooms.text.replace("\n","")
                            room_list.append(k)
                            # print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                        except:
                            k = last_room
                            room_list.append(k)
                        if price_local is not None:
                            price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                            price_local.append(price.text[6:].replace("\n",""))
                        # print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room list tiene un largo de {len(room_list)}")

                    except:
                        k = None
                        k = None

                room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

                cycle += 1
                # print(f"Room and price es: {room_and_price}")

                rooms_and_price_gen[str(date_chkin)] = room_and_price
                # print(f"Lo que tiene room_and_price_gen es: {rooms_and_price_gen}")
                room_list = []
                price_local = []
                room_and_price = {}

                l.append(g)
                
                l = []
                g = []

            elif i == 1:
               # print(f"Vamos en ciclo: {i}")
                date_chkin = date.today() + timedelta(days=7)
                # target_url = self.url_convert(self.url)
                posicion = 0

                for i in self.url:
                    if i == "?":
                        date_chkin = date.today() + timedelta(days=7)
                        date_chkout = date.today() + timedelta(days=8)
                        target_url = self.url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
                    posicion += 1


                headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

                resp = requests.get(target_url, headers=headers)
                soup = BeautifulSoup(resp.text, 'lxml')

                ids = []

                try:
                    tr = soup.find_all("tr")
                except:
                    tr = None

                for y in range(0,len(tr)):
                    try:
                        id = tr[y].get('data-block-id')
                    except:
                        id = None

                    if id is not None:
                        ids.append(id)

                for m in range(0,len(ids)):
                    try:
                        allData = soup.find("tr",{"data-block-id":ids[m]})
                        try:
                            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                        except:
                            rooms=None

                        if rooms is None:
                            last_room = rooms.text.replace("\n","")
                        try:
                            k = rooms.text.replace("\n","")
                            room_list.append(k)
                           # print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                        except:
                            k = last_room
                            room_list.append(k)
                        if price_local is not None:
                            price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                            price_local.append(price.text[6:].replace("\n",""))
                        # print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room list tiene un largo de {len(room_list)}")

                    except:
                        k = None
                        k = None

                room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

                cycle += 1
               # print(f"Room and price es: {room_and_price}")

                rooms_and_price_gen[str(date_chkin)] = room_and_price
                room_list = []
                price_local = []
                room_and_price = {}

            elif i == 2:
                date_chkin = date.today() + timedelta(days=30)
              #  print(f"Vamos en ciclo: {i}")

                # target_url = self.url_convert(self.url)
                posicion = 0

                for i in self.url:
                    if i == "?":
                        date_chkin = date.today() + timedelta(days=30)
                        date_chkout = date.today() + timedelta(days=31)
                        target_url = self.url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
                    posicion += 1




                headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

                resp = requests.get(target_url, headers=headers)
                soup = BeautifulSoup(resp.text, 'lxml')

                ids = []

                try:
                    tr = soup.find_all("tr")
                except:
                    tr = None

                for y in range(0,len(tr)):
                    try:
                        id = tr[y].get('data-block-id')
                    except:
                        id = None

                    if id is not None:
                        ids.append(id)

                for m in range(0,len(ids)):
                    try:
                        allData = soup.find("tr",{"data-block-id":ids[m]})
                        try:
                            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                        except:
                            rooms=None

                        if rooms is None:
                            last_room = rooms.text.replace("\n","")
                        try:
                            k = rooms.text.replace("\n","")
                            room_list.append(k)
                       #     print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                        except:
                            k = last_room
                            room_list.append(k)
                        if price_local is not None:
                            price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                            price_local.append(price.text[6:].replace("\n",""))
                      #  print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room list tiene un largo de {len(room_list)}")

                    except:
                        k = None
                        k = None

                room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

                cycle += 1
              #  print(f"Room and price es: {room_and_price}")

                rooms_and_price_gen[str(date_chkin)] = room_and_price
                room_list = []
                price_local = []
                room_and_price = {}

            elif i == 3:
              #  print(f"Vamos en ciclo: {i}")
                date_chkin = date.today() + timedelta(days=90)
                
                # target_url = self.url_convert(self.url)
                posicion = 0

                for i in self.url:
                    if i == "?":
                        date_chkin = date.today() + timedelta(days=90)
                        date_chkout = date.today() + timedelta(days=91)
                        target_url = self.url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
                    posicion += 1


                headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

                resp = requests.get(target_url, headers=headers)
                soup = BeautifulSoup(resp.text, 'lxml')

                ids = []

                try:
                    tr = soup.find_all("tr")
                except:
                    tr = None

                for y in range(0,len(tr)):
                    try:
                        id = tr[y].get('data-block-id')
                    except:
                        id = None

                    if id is not None:
                        ids.append(id)
                        
                for m in range(0,len(tr)):
                    try:
                        allData = soup.find("tr",{"data-block-id":ids[m]})
                        try:
                            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                        except:
                            rooms=None

                        if rooms is None:
                            last_room = rooms.text.replace("\n","")
                        try:
                            k = rooms.text.replace("\n","")
                            room_list.append(k)
                          #  print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                        except:
                            k = last_room
                            room_list.append(k)
                        if price_local is not None:
                            price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                            price_local.append(price.text[6:].replace("\n",""))
                        # print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room list tiene un largo de {len(room_list)}")

                    except:
                        k = None
                        k = None

                room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

                cycle += 1
               # print(f"Room and price es: {room_and_price}")

                rooms_and_price_gen[str(date_chkin)] = room_and_price
                room_list = []
                price_local = []
                room_and_price = {}
        
        return rooms_and_price_gen

    @classmethod
    def url_convert(cls, url):
        ciclo_convert = cls.cycle
        posicion = 0

        for i in url:
            if i == "?" and ciclo_convert == 0:
                date_chkin = date.today() + timedelta(days=1)
                date_chkout = date.today() + timedelta(days=2)
                url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
            elif i == "?" and ciclo_convert == 1:
                date_chkin = date.today() + timedelta(days=7)
                date_chkout = date.today() + timedelta(days=8)
                url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
            elif i == "?" and ciclo_convert == 2:
                date_chkin = date.today() + timedelta(days=30)
                date_chkout = date.today() + timedelta(days=31)
                url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
            elif i == "?" and ciclo_convert == 3:
                date_chkin = date.today() + timedelta(days=90)
                date_chkout = date.today() + timedelta(days=91)
                url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
            posicion += 1
        return url

"""url = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
cycle = 0

monitoreo = monitoreo_booking(url, cycle)
resultado = monitoreo.monitoreo_bbk()
print(f"Lo que retorna la clase es: {resultado}")
"""