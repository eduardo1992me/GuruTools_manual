from django.test import TestCase
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # <--- Navegador oculto, podría causar errores
import time
from datetime import timedelta, date

# options = Options() # <--- Navegador oculto, podría causar errores
# options.headless = True # <--- Navegador oculto, podría causar errores

PATH = '/Users/eduardomedina/Documents/GuruTools_manual/hotel/chromedriver_mac_arm64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
options.add_argument('accept-encoding=gzip, deflate, br')
options.add_argument('accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
options.add_argument('referer=https://www.expedia.com/')
options.add_argument('upgrade-insecure-requests=1')


l = []
o  = {}
l = []
o  = {}
list_room = []
list_price = []
cycle = 0
posicion = 0
currency = ""
room_and_price_gen = {}
old_chkin = ""
old_chout = ""



target_url_1= "https://www.expedia.mx/Aguascalientes-Hoteles-Francia-Aguascalientes.h485253.Informacion-Hotel?chkin=2023-07-27&chkout=2023-07-28&x_pwa=1&rfrr=HSR&pwa_ts=1689231623988&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5teC9Ib3RlbC1TZWFyY2g%3D&useRewards=true&rm1=a2&regionId=315&destination=Aguascalientes%2C+Aguascalientes%2C+México&destType=MARKET&neighborhoodId=6347796&selected=485253&latLong=21.880852%2C-102.296016&showAvailableOnly=true&sort=RECOMMENDED&top_dp=950&top_cur=MXN&userIntent=&selectedRoomType=237760&selectedRatePlan=240344899&searchId=7651dcb0-b0bf-4b3e-a149-49c03e88c372"


def monotoreoExpedia(url):
    target_url = url
    posicion = 0
    pos = 0
 

    for c in target_url:
        if c == "c" and target_url[posicion + 4:posicion + 7] == "USD":
            currency = "USD"
            print("Tipo de moneda encontrado, es USD")
        elif c == "c" and target_url[posicion + 4:posicion + 7] == "MXN":
            currency = "MXN"
            print("Tipo de moneda encontrado, es MXN")
        posicion += 1

    for cy in range(4):
        if cy == 0:
            driver=webdriver.Chrome(PATH, options=options) # <--- Navegador oculto, podría causar errores(, chrome_options=options)
            for i in target_url:
                if i == "?":
                    date_chkin = date.today() + timedelta(days=1)
                    date_chkout = date.today() + timedelta(days=2)
                    date_o_chi = (target_url[pos+7:pos+17])
                    date_o_cho = (target_url[pos+25:pos+35])
                    target_url_a = target_url.replace(str(date_o_chi), str(date_chkin))
                    target_url_a = target_url_a.replace(str(date_o_cho), str(date_chkout))
                pos += 1
            pos = 0

            driver.get(target_url_a)
            time.sleep(5)
            resp = driver.page_source
            driver.close()

            soup = BeautifulSoup(resp, 'lxml')
            allRooms = soup.find("div",{"data-stid":"section-room-list"})
            Rooms = allRooms.find_all("div", {"class":"uitk-layout-grid-item"})
  

            date_chkin = date.today() + timedelta(days=1)
            date_chkout = date.today() + timedelta(days=2)

            for Room in Rooms:
                price_arr=Room.find_all("div",{"data-test-id":"price-summary-message-line"})
                try:
                    list_room.append(Room.find("div",{"class":"uitk-spacing-padding-blockstart-three"}).find("div",{"class":"uitk-spacing-padding-small-blockend-half"}).text)
                except:
                    list_room.append(None)

                try:
                    list_price.append(price_arr[0].find("span").text)
                except:
                    list_price.append(None)
                # cycle += 1

            if currency == "MXN":
                remove_cr = "MXN$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    clear_price = price_raw.replace(remove_cr, '')
                    list_price[a] = clear_price
            elif currency == "USD":
                remove_cr = "$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    clear_price = price_raw.replace(remove_cr, '')
                    list_price[a] = clear_price
                #print(list_price)
            #print(list_price)

            room_and_price = {list_room:list_price for (list_room,list_price) in zip(list_room,list_price)}
            room_and_price_gen[str(date_chkin)] = room_and_price
            print(room_and_price_gen)
            l = []
        
        elif cy == 1:
            driver=webdriver.Chrome(PATH, options=options) # <--- Navegador oculto, podría causar errores(, chrome_options=options)
            for i in target_url:
                if i == "?":
                    date_chkin = date.today() + timedelta(days=7)
                    date_chkout = date.today() + timedelta(days=8)
                    date_o_chi = (target_url[pos+7:pos+17])
                    date_o_cho = (target_url[pos+25:pos+35])
                    target_url_a = target_url.replace(str(date_o_chi), str(date_chkin))
                    target_url_a = target_url_a.replace(str(date_o_cho), str(date_chkout))
                pos += 1
            pos = 0

            driver.get(target_url_a)
            time.sleep(5)
            resp = driver.page_source
            driver.close()

            soup = BeautifulSoup(resp, 'lxml')
            allRooms = soup.find("div",{"data-stid":"section-room-list"})
            Rooms = allRooms.find_all("div", {"class":"uitk-layout-grid-item"})


            date_chkin = date.today() + timedelta(days=7)
            date_chkout = date.today() + timedelta(days=8)

            for Room in Rooms:
                price_arr=Room.find_all("div",{"data-test-id":"price-summary-message-line"})
                try:
                    list_room.append(Room.find("div",{"class":"uitk-spacing-padding-blockstart-three"}).find("div",{"class":"uitk-spacing-padding-small-blockend-half"}).text)
                except:
                    list_room.append(None)

                try:
                    list_price.append(price_arr[0].find("span").text)
                except:
                    list_price.append(None)
                # cycle += 1

            if currency == "MXN":
                remove_cr = "MXN$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    str(price_raw)
                    if price_raw is not None:
                        if price_raw[0:3] == "MXN":
                            clear_price = price_raw.replace(remove_cr, '')
                            list_price[a] = clear_price
            elif currency == "USD":
                remove_cr = "$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    clear_price = price_raw.replace(remove_cr, '')
                    list_price[a] = clear_price
                #print(list_price)
            #print(list_price)

            room_and_price = {list_room:list_price for (list_room,list_price) in zip(list_room,list_price)}
            room_and_price_gen[str(date_chkin)] = room_and_price
            print(room_and_price_gen)

        elif cy == 2:
            driver=webdriver.Chrome(PATH, options=options) # <--- Navegador oculto, podría causar 
            for i in target_url:
                if i == "?":
                    date_chkin = date.today() + timedelta(days=30)
                    date_chkout = date.today() + timedelta(days=31)
                    date_o_chi = (target_url[pos+7:pos+17])
                    date_o_cho = (target_url[pos+25:pos+35])
                    target_url_a = target_url.replace(str(date_o_chi), str(date_chkin))
                    target_url_a = target_url_a.replace(str(date_o_cho), str(date_chkout))
                pos += 1
            pos = 0

            driver.get(target_url_a)
            time.sleep(5)
            resp = driver.page_source
            driver.close()

            soup = BeautifulSoup(resp, 'lxml')
            allRooms = soup.find("div",{"data-stid":"section-room-list"})
            Rooms = allRooms.find_all("div", {"class":"uitk-layout-grid-item"})


            date_chkin = date.today() + timedelta(days=30)
            date_chkout = date.today() + timedelta(days=31)

            for Room in Rooms:
                price_arr=Room.find_all("div",{"data-test-id":"price-summary-message-line"})
                try:
                    list_room.append(Room.find("div",{"class":"uitk-spacing-padding-blockstart-three"}).find("div",{"class":"uitk-spacing-padding-small-blockend-half"}).text)
                except:
                    list_room.append(None)

                try:
                    list_price.append(price_arr[0].find("span").text)
                except:
                    list_price.append(None)
                # cycle += 1

            if currency == "MXN":
                remove_cr = "MXN$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    str(price_raw)
                    if price_raw is not None:
                        if price_raw[0:3] == "MXN":
                            clear_price = price_raw.replace(remove_cr, '')
                            list_price[a] = clear_price
            if currency == "MXN":
                remove_cr = "MXN$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    str(price_raw)
                    if price_raw is not None:
                        if price_raw[0:3] == "MXN":
                            clear_price = price_raw.replace(remove_cr, '')
                            list_price[a] = clear_price
                        
                #print(list_price)
            #print(list_price)

            room_and_price = {list_room:list_price for (list_room,list_price) in zip(list_room,list_price)}
            room_and_price_gen[str(date_chkin)] = room_and_price
            print(room_and_price_gen)

        elif cy == 3:
            driver=webdriver.Chrome(PATH, options=options) # <--- Navegador oculto, podría causar errores(, chrome_options=options)
            for i in target_url:
                if i == "?":
                    date_chkin = date.today() + timedelta(days=90)
                    date_chkout = date.today() + timedelta(days=91)
                    date_o_chi = (target_url[pos+7:pos+17])
                    date_o_cho = (target_url[pos+25:pos+35])
                    target_url_a = target_url.replace(str(date_o_chi), str(date_chkin))
                    target_url_a = target_url_a.replace(str(date_o_cho), str(date_chkout))
                pos += 1
            pos = 0

            driver.get(target_url_a)
            time.sleep(5)
            resp = driver.page_source
            driver.close()

            soup = BeautifulSoup(resp, 'lxml')
            allRooms = soup.find("div",{"data-stid":"section-room-list"})
            Rooms = allRooms.find_all("div", {"class":"uitk-layout-grid-item"})


            date_chkin = date.today() + timedelta(days=90)
            date_chkout = date.today() + timedelta(days=91)

            for Room in Rooms:
                price_arr=Room.find_all("div",{"data-test-id":"price-summary-message-line"})
                try:
                    list_room.append(Room.find("div",{"class":"uitk-spacing-padding-blockstart-three"}).find("div",{"class":"uitk-spacing-padding-small-blockend-half"}).text)
                except:
                    list_room.append(None)

                try:
                    list_price.append(price_arr[0].find("span").text)
                except:
                    list_price.append(None)
                # cycle += 1

            if currency == "MXN":
                remove_cr = "MXN$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    str(price_raw)
                    if price_raw is not None:
                        if price_raw[0:3] == "MXN":
                            clear_price = price_raw.replace(remove_cr, '')
                            list_price[a] = clear_price

            elif currency == "USD":
                remove_cr = "$"
                for a in range (len(list_price)):
                    price_raw = list_price[a]
                    clear_price = price_raw.replace(remove_cr, '')
                    list_price[a] = clear_price
                #print(list_price)
            #print(list_price)

            room_and_price = {list_room:list_price for (list_room,list_price) in zip(list_room,list_price)}
            room_and_price_gen[str(date_chkin)] = room_and_price
            return room_and_price_gen



"""def guardarMonitoreoExp():
    control = ControlMonitoreos()
    control.save()
    m = Monitoreos(id_monitoreo=control.id, fecha_chkin = "", canal = "", habitacion = "", precio = "")
    m.save()
"""



        

monotoreoExpedia(target_url_1)