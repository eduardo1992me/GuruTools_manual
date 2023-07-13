from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # <--- Navegador oculto, podría causar errores
import time
from datetime import timedelta, date
#from models import Monitoreos, ControlMonitoreos


PATH = '/Users/eduardomedina/Documents/GuruTools_manual/hotel/chromedriver_mac_arm64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
options.add_argument('accept-encoding=gzip, deflate, br')
options.add_argument('accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
options.add_argument('referer=https://www.expedia.com/')
options.add_argument('upgrade-insecure-requests=1')
options.headless = True # <--- Navegador oculto, podría causar errores


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

target_url= "https://www.expedia.mx/Playa-Del-Carmen-Hoteles-Grand-Velas-Riviera-Maya-All-Inclusive.h2406344.Informacion-Hotel?chkin=2023-07-05&chkout=2023-07-06&x_pwa=1&rfrr=HSR&pwa_ts=1687358143606&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5teC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=601751&destination=Playa+del+Carmen%2C+Quintana+Roo%2C+México&destType=MARKET&latLong=20.629571%2C-87.073173&trackingData=AAAAAQAAAAEAAAAQ4qf01Y8r0o2gOQgXXj0KEzRUHzRddpOI5GcD1i7H3XXfCpUzmz0ZO3q4myp4hx2mrz_38jYZWTSvps0_N2rQWJf3y1csihBYIue3x_Tv2r1eh6apcjzZr8M6CWZ8elmogXNaAyZmiIlsCqsA1KyhbZvuWDA1FWyP0bvhCXXlwhk1VuuiNA4pZQuyknHG4FbzKmVy0LSO3iQ3oyqL0y9ufeCC0bpK8YhDBiu7xrY9K3h2UwrskW2Fp7u92KWnXQnUhUa4p1bHzgumXsBXp_EKbeu6UtmTBSOVU47R23u13Yul0huDoa-KzjfEKoBkoDt9Q4CfLiqot3hd3TZkljrx6CTNJhsv6MB_-Xr8pXA0LRKR8CG_YZQzlxxlPv0uOpB-1NFqGdgBqauo1rnQelkBHS-yGIrZrcI_eeGI4UJek7yV3tVZrPyPU6HpqwmXBuD2LMlNHpRw98amQC_-5O454EDZ6l7KOX-YlRYiJeKm4EgK46_kpa38BiAR_Xfv-q2784P2ARbsVrRTyKV4vBWWyZIaiM1DmajwneYsr_bg-uvEPKi09w0qg8RNLbC3y059sdv5850_4wgQO7b7Gypbs2krpSThc8vXuhL1QcTIx_O1xy9D34AlVrImZyj2MSSiHWYRr5iYjx6gjo4cm8jzkxGgFdoRoVz0Oc4zwWIKuEBrzW3yGBscifToGvQeb3LFA_XJUAc9MA7QP8zl9Ji6lLvb73hWzPVByoCG-kg-H1E-WAR7xonqeomsTdsXiIqS_-TpY9nJuQPRS5QTJRkXNKdwZZTh0HZ4iLOHk0RvGkJgWYaPysM_SFomiMTzD3OJgtMzARL7GcSqPyA_QCL4ivcwStQ3Yw4DHumdzLdbXZ4k5GUWyHULH5yC29WGuEP98sq5Ov8KWBDC56yVuzyoMc_-OETBMM6_XV7EVPPS4F6p2V2wfcrjmr8W-hsh9to2Gh41RQLt8UDnlZQhVx8JAlT9950PHiRVZGu6vEPeR-F-CJwqEkiXFIY08B8b98fmr4ynpHEQU7w5LuJLK_ja5ic8NJq4qhw2K0baDZX6T8njFfYz6ZUR3vIwAAsBNgYaVXTEcaVgmwnpoXLJZaCcOObF7rNKtuRXJZDMXt1mQ7DVcjtUe88wM4A9V48I32Kq_HcrP9LIBUbSCNVP59D2ie5hHLx-J8T_8Q50vlHBuCIx1J6e-qxqMOa505WMXejPEzDFG8Sn4Z_rVSArDXk_4B3CkuXRRlNe3uhFxkA5KFRlwO93FQZT_0lKZ1rxGXpc7kzm7zIS9HE8cy5g-BDJm6DvxQAi2sAwGDZttGaO_b6ZMmsZAuxZNg8lAhW4wU_DEzDe62v69jixcTZIDFoMH8P0AUcH2oRvLEkRJ3Kh0HU1NiO2ugDZ4kQ2ZBOkBcOexCJJ1dhEF-k7zb7aOGvEI4SOlOu0YX_OqJri_8tbGa90rhR8QtCg-P4RA0GRQ3MXVAoeOw2PrDajjkR_IF5-kWF9WTKvHevhLhlqxZHa1dgWc0TEoU2n_4HiOY6DceSzoU6fEUMF8A9l78O8wFAnshWMLBhbMlKj_ddAPMv6a2IMfZkKN0zvD4TDOBRzkSplAqO9T9c8tMFTbi8PzG10QO32m1xcxrtMVq5cZS4wf9cwFMZfKwIC1za1VQ_Rbko6mLlrl4EhLbJ9MzTbYx-C6nPlZNPeFgYPJTLDAqe1PpsajLyLkbEu5toGjrOmaIqOivEME06pVwUJHV2H5HM3pvo-1gZrYaXw0reY7oGTGPgXeInIIkn9Bsm8tXx4jRRDSAaqQAQDX5TrwGhERdXU7-bz_Jwwulqy2RI7faFr27L2jVNCB0L2gX6tkI9LhHiSwy74MnViq6cbTniWuJbL92FbOikRH-XRz41Im3kN0cPaig3XCtvOJE3jn1SfuNIXzRXs8-mUv6nC22LgsguSwxDLGuqRWgqBY7TJ5TIqyEVcwQ2rEQuEixcfp6WfaomZyfTYfbzXevlFtO352tTfL7DiJFVfQgvwx8oicXzq8GsG0_uZNU3cI8n61gHbad9uIsfcMuaifURLF2dND2BXclKYw9d8xYA2gewnXp8U_juR6ZxELmjmblUXg8A7tduamKb-J5DBcjNdT6E-2fkef5fMNyM9SKvSYztITZsKtMjCbUvqCfTcjpvAsaMPPyLRvGPDMlJP8SS16qqR0qlTtKbggnXHZckEaT0K6v6w4Deb4vaacuVoRJz9ICIAm6yoy1xU52_lwZMTBljdoHtTmPIBJ9ENiFK49npkNqcSOMK_baOcBkVBtnNv_ucdfPQ71wW3RiNaDx6WuKg5FRJD5RiaJ5eDXcDCn-DmE1ywZLes0FFkXON1PrFNvmyhhTNYVg1kP_4udvMBYJD-0xmkeDCmHakEi_kdvw9lk29QUn1ZiXTdmGsoMSm08C1Qp06b14iZVIMB-lEDla-nXaXkeA%3D%3D&rank=1&testVersionOverride=Buttercup%2C45803.145008.1%2C44204.0.0%2C44203.0.0%2C43549.0.0%2C43550.0.0%2C31936.102311.0%2C33775.98848.1%2C38414.114301.0%2C39483.0.0%2C38427.115718.1%2C42444.0.0%2C42589.0.0%2C42876.124673.0%2C42973.0.0%2C42974.0.0%2C42975.0.0%2C42976.0.0%2C42802.125960.1%2C33739.99567.0%2C37898.109354.0%2C37930.0.0%2C37949.0.0%2C37354.0.0%2C43435.128144.0%2C43153.133019.3&slots=&position=1&beaconIssued=&sort=RECOMMENDED&top_dp=16727&top_cur=MXN&userIntent=&selectedRoomType=210311669&selectedRatePlan=222288917&searchId=8aa188bd-a172-46e6-a1fa-fa41b3c1aab7"


def url_convert(url, cycle):
    posicion = 0
    global old_chout
    url_out = url
    print("Entro a URL_convert")
    for i in url:
        if i == "?" and cycle == 0:
            date_chkin = date.today() + timedelta(days=1)
            date_chout = date.today() + timedelta(days=2)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                #print(ch, url_out[posicion], posicion)
                #print(url_out[posicion+1:posicion+6])
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    str(url_out)
                    return url_out
            posicion += 1

        elif i == "?" and cycle == 1:
            print(f"Entro al Elif 1 ")
            date_chkin = date.today() + timedelta(days=7)
            date_chout = date.today() + timedelta(days=8)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                print(f"ch vale: {ch} y posición vale: {posicion}")
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    print("Entro en el if donde detecta chkin")
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    str(url_out)
                    print(f"El conteinido de url_out es: {url_out}")
                    return url_out
                posicion += 1

        elif i == "?" and cycle == 2:
            date_chkin = date.today() + timedelta(days=30)
            date_chout = date.today() + timedelta(days=31)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    return url_out
                posicion += 1

        elif i == "?" and cycle == 3:
            date_chkin = date.today() + timedelta(days=90)
            date_chout = date.today() + timedelta(days=91)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    return url_out
                posicion += 1




def monotoreoExpedia(url):
    target_url = url
    posicion = 0
 

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

            driver.get(target_url)
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
            target_url = url_convert(url,cy)
            str(target_url)
            print(f"El contenido de target URl es: {target_url}")
            driver.get(target_url)
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
            
            target_url = url_convert(url, cy)
            driver.get(target_url)
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

        elif cy == 3:
            driver=webdriver.Chrome(PATH, options=options) # <--- Navegador oculto, podría causar errores(, chrome_options=options)
            target_url = url_convert(url, cy)
            driver.get(target_url)
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



"""def guardarMonitoreoExp():
    control = ControlMonitoreos()
    control.save()
    m = Monitoreos(id_monitoreo=control.id, fecha_chkin = "", canal = "", habitacion = "", precio = "")
    m.save()
"""



        

monotoreoExpedia(target_url)