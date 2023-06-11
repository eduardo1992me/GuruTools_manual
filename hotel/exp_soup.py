import requests
from bs4 import BeautifulSoup
import lxml


headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

target_url = "https://www.expedia.mx/Playa-Del-Carmen-Hoteles-La-Pasion-Hotel-Boutique-By-Bunik.h5151337.Informacion-Hotel?chkin=2023-08-15&chkout=2023-08-16"

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml') # html.parser

rooms= []

targetId=[]


try:
    name_raw = soup.get("uitk-heading uitk-heading-6")
    print(name_raw)
except:
    name_raw = None


try:
    room = name_raw.find_all("h3",{"class":"uitk-heading uitk-heading-6"})
        
    # print(id)

except:
    room = None
"""
if( rooms is not None):
    rooms.append(room)
"""
print("Names are ",len(rooms))
print(rooms)