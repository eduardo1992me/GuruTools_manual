import requests
from bs4 import BeautifulSoup
import lxml
import time
from datetime import timedelta, date

website = 'https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?label=operasoft-dial-344716&sid=543d89504a72ca2f32cdc7cacc53b63b&aid=344716&ucfs=1&arphpl=1&checkin=2023-09-22&checkout=2023-09-23&dest_id=-1649885&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=809e097ab6f00031&srepoch=1685755255&all_sr_blocks=7827405_91294473_2_2_0&highlighted_blocks=7827405_91294473_2_2_0&matching_block_id=7827405_91294473_2_2_0&sr_pri_blocks=7827405_91294473_2_2_0__84645&from_sustainable_property_sr=1&map_fdco=1&from=searchresults#hotelTmpl'

target_url = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"



def monitoreo_bbk(main_url):
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
            
            date_chkin = date.today() + timedelta(days=1)
            date_chkout = date.today() + timedelta(days=2)
            # print(main_url)
            target_url = url_convert(main_url, i)
            print(f"La url con la que se esta trabajando es {target_url}")
            
            headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

            resp = requests.get(target_url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml') # html.parser
            # o["name"]=soup.find("h2",{"class":"pp-header__title"}).text # <--- Recupera el nombre del hotel
            ids= [] # <--- Ids de las habitaciones

            targetId=[] 
            try:
                tr = soup.find_all("tr")
                # print(tr)
            except:
                tr = None

            for y in range(0,len(tr)):
                try:
                    id = tr[y].get('data-block-id')
                    # print(id)

                except:
                    id = None

                if(id is not None):
                    ids.append(id)

            print("ids are ",len(ids))


            for m in range(0,len(ids)):

                try:
                    allData = soup.find("tr",{"data-block-id":ids[m]})
                    try:
                        rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                    except:
                        rooms=None

                    if(rooms is None):
                        last_room = rooms.text.replace("\n","")
                    try:
                        k=rooms.text.replace("\n","")
                        room_list.append(k)
                        print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                    except:
                        k=last_room
                        room_list.append(k)
                    if (price_local is not None):
                        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                        price_local.append(price.text[6:].replace("\n",""))
                    print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room ñlist tiene un largo de {len(room_list)}")

        
                    
                    #g.append(k)
                    #k={}

                except:
                    k=None
                    k=None

            room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

            #room_and_price_temp = room_and_price
            cycle += 1
            print(f"Room and price es:{room_and_price}")

            rooms_and_price_gen[str(date_chkin)] = room_and_price
            print(f"Lo que tiene room_and_price_gen es: {rooms_and_price_gen}")
            room_list = []
            price_local = []
            room_and_price = {}

                                
            l.append(g) #<-- Precio
            #room_and_price = {g:o for (g,o) in zip(g,o)}
            
            
            l = []
            g = []

            #print(rooms_and_price_gen)
            

        elif i == 1:
            date_chkin = date.today() + timedelta(days=7)
            target_url = url_convert(main_url, i)
            print(f"La url con la que se esta trabajando es {target_url}")
            headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

            resp = requests.get(target_url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml') # html.parser

            ids= [] # <--- Ids de las habitaciones
            targetId=[] 
            
            try:
                tr = soup.find_all("tr")
                # print(tr)
            except:
                tr = None

            for y in range(0,len(tr)):
                try:
                    id = tr[y].get('data-block-id')
                    # print(id)

                except:
                    id = None

                if( id is not None):
                    ids.append(id)

            # print("ids are ",len(ids))

            for m in range(0,len(ids)):

                try:
                    allData = soup.find("tr",{"data-block-id":ids[m]})
                    try:
                        rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                    except:
                        rooms=None

                    if(rooms is None):
                        last_room = rooms.text.replace("\n","")
                    try:
                        k=rooms.text.replace("\n","")
                        room_list.append(k)
                        print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                    except:
                        k=last_room
                        room_list.append(k)
                    if (price_local is not None):
                        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                        price_local.append(price.text[6:].replace("\n",""))
                    print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room ñlist tiene un largo de {len(room_list)}")

        
                    
                    #g.append(k)
                    #k={}

                except:
                    k=None
                    k=None

            room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

            #room_and_price_temp = room_and_price
            cycle += 1
            print(f"Room and price es:{room_and_price}")

            rooms_and_price_gen[str(date_chkin)] = room_and_price
            room_list = []
            price_local = []
            room_and_price = {}
            #print(rooms_and_price_gen)
        
        elif i == 2:
            date_chkin = date.today() + timedelta(days=30)
            print(f"Vamos en ciclo: {i}")
            target_url = url_convert(main_url, i)
            print(f"La url con la que se esta trabajando es {target_url}")
            headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

            resp = requests.get(target_url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml') # html.parser
            ids= [] # <--- Ids de las habitaciones
            targetId=[] 
            
            try:
                tr = soup.find_all("tr")
                # print(tr)
            except:
                tr = None

            for y in range(0,len(tr)):
                try:
                    id = tr[y].get('data-block-id')
                    # print(id)

                except:
                    id = None

                if( id is not None):
                    ids.append(id)

            # print("ids are ",len(ids))

            for m in range(0,len(ids)):

                try:
                    allData = soup.find("tr",{"data-block-id":ids[m]})
                    try:
                        rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                    except:
                        rooms=None

                    if(rooms is None):
                        last_room = rooms.text.replace("\n","")
                    try:
                        k=rooms.text.replace("\n","")
                        room_list.append(k)
                        print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                    except:
                        k=last_room
                        room_list.append(k)
                    if (price_local is not None):
                        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                        price_local.append(price.text[6:].replace("\n",""))
                    print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room ñlist tiene un largo de {len(room_list)}")

        
                    
                    #g.append(k)
                    #k={}

                except:
                    k=None
                    k=None

            room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

            #room_and_price_temp = room_and_price
            cycle += 1
            print(f"Room and price es:{room_and_price}")

            rooms_and_price_gen[str(date_chkin)] = room_and_price
            room_list = []
            price_local = []
            room_and_price = {}
        
        elif i == 3:
            date_chkin = date.today() + timedelta(days=90)
            print(f"Vamos en ciclo: {i}")
            target_url = url_convert(main_url, i)
            print(f"La url con la que se esta trabajando es {target_url}")
            headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

            resp = requests.get(target_url, headers=headers)
            soup = BeautifulSoup(resp.text, 'lxml') # html.parser

            ids= [] # <--- Ids de las habitaciones
            targetId=[] 
            try:
                tr = soup.find_all("tr")
                # print(tr)
            except:
                tr = None

            for y in range(0,len(tr)):
                try:
                    id = tr[y].get('data-block-id')
                    # print(id)

                except:
                    id = None

                if( id is not None):
                    ids.append(id)
                    
            for m in range(0,len(tr)):

                try:
                    allData = soup.find("tr",{"data-block-id":ids[m]})
                    try:
                        rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
                    except:
                        rooms=None

                    if(rooms is None):
                        last_room = rooms.text.replace("\n","")
                    try:
                        k=rooms.text.replace("\n","")
                        room_list.append(k)
                        print(f"Esto contiene la variable room list {room_list} en el ciclo {m}")
                    except:
                        k=last_room
                        room_list.append(k)
                    if (price_local is not None):
                        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
                        price_local.append(price.text[6:].replace("\n",""))
                    print(f"Esto es lo que contiene price_local fuera del TRY {price_local} y room ñlist tiene un largo de {len(room_list)}")

        
                    
                    #g.append(k)
                    #k={}

                except:
                    k=None
                    k=None

            room_and_price = {room_list:price_local for (room_list,price_local) in zip(room_list,price_local)}

            #room_and_price_temp = room_and_price
            cycle += 1
            print(f"Room and price es:{room_and_price}")

            rooms_and_price_gen[str(date_chkin)] = room_and_price
            room_list = []
            price_local = []
            room_and_price = {}
            print(f"El diccionario final queda como: {rooms_and_price_gen}")


def url_convert(url, cycle):
    posicion = 0
    encontrado = False
    encontrado_fin_url = False
    for i in url:
        if i == "?" and cycle == 0:
            date_chkin = date.today() + timedelta(days=1)
            date_chkout = date.today() + timedelta(days=2)
            url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
           # print(f"Fecha en ciclo 0 es:: {date_chkin}")
        elif i == "?" and cycle == 1:
            date_chkin = date.today() + timedelta(days=7)
            date_chkout = date.today() + timedelta(days=8)
            url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
           # print(f"Fecha en 1: {date_chkin}")
        elif i == "?" and cycle == 2:
            date_chkin = date.today() + timedelta(days=30)
            date_chkout = date.today() + timedelta(days=31)
            url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
           # print(f"Fecha en 2: {date_chkin}")
        elif i == "?" and cycle == 3:
            date_chkin = date.today() + timedelta(days=90)
            date_chkout = date.today() + timedelta(days=91)
            url = url[0:posicion] + f"?checkin={date_chkin}&checkout={date_chkout}&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
           # print(f"Fecha en 3: {date_chkin}")
        posicion += 1
    return url
        


monitoreo_bbk(target_url)