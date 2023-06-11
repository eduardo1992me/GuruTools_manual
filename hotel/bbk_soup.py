import requests
from bs4 import BeautifulSoup
import lxml
import time

website = 'https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?label=operasoft-dial-344716&sid=543d89504a72ca2f32cdc7cacc53b63b&aid=344716&ucfs=1&arphpl=1&checkin=2023-09-22&checkout=2023-09-23&dest_id=-1649885&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=809e097ab6f00031&srepoch=1685755255&all_sr_blocks=7827405_91294473_2_2_0&highlighted_blocks=7827405_91294473_2_2_0&matching_block_id=7827405_91294473_2_2_0&sr_pri_blocks=7827405_91294473_2_2_0__84645&from_sustainable_property_sr=1&map_fdco=1&from=searchresults#hotelTmpl'


l=list()
g=list()
o={}
k={}
# fac=[]
# fac_arr=[]
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

target_url = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml') # html.parser

o["name"]=soup.find("h2",{"class":"pp-header__title"}).text # <--- Recupera el nombre del hotel
"""
o["address"]=soup.find("span",{"class":"hp_address_subtitle"}).text.strip("\n")
o["rating"]=soup.find("div",{"class":"d10a6220b4"}).text
"""
"""fac=soup.find_all("div",{"class":"important_facility"})
for i in range(0,len(fac)):
    fac_arr.append(fac[i].text.strip("\n"))
"""

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

print("ids are ",len(ids))


for i in range(0,len(ids)):

    try:
        allData = soup.find("tr",{"data-block-id":ids[i]})
        try:
            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
        except:
            rooms=None


        if(rooms is not None):
            last_room = rooms.text.replace("\n","")
        try:
            k["room"]=rooms.text.replace("\n","")
        except:
            k["room"]=last_room

        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
        k["price"]=price.text.replace("\n","")


        
        
        
        g.append(k)
        k={}

    except:
        k["room"]=None
        k["price"]=None


l.append(g)
l.append(o)
# l.append(fac_arr)
print(l)