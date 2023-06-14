from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from selenium.webdriver.support.ui import Select


PATH = '/Users/eduardomedina/Documents/GuruTools_manual/hotel/chromedriver_mac_arm64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
options.add_argument('accept-encoding=gzip, deflate, br')
options.add_argument('accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
# options.add_argument('referer=https://www.expedia.com/')
options.add_argument('upgrade-insecure-requests=1')





date_now = datetime.datetime.now()
print(date_now.day, date_now.month, date_now.year)

l = []
o  = {}

target_url= "https://www.hotelluca.mx"

driver=webdriver.Chrome(PATH, options=options)
driver.get(target_url)
time.sleep(6)


date_picker = driver.find_element("xpath",'//*[@id="searchengine"]/div/div[1]/div/div[1]')
date_picker.click()
time.sleep(3)


cal_ckin = driver.find_elements("xpath",'//*[@id="radix-:ra:"]/div/div[3]/div[1]/div/button')
# time.sleep(3)
print(date_now.day+1)
for i in cal_ckin:
    print(i.text)
    if i.text == str(date_now.day+1):
        i.click()
        
    # break

search_button = driver.find_element("xpath",'//*[@id="searchengine"]/div/div[2]/button')
search_button.click()
time.sleep(10)

room_list = driver.find_elements("xpath", '//*[@id="checkout"]/div/div[4]/div/div[2]/div[2]/a')
print(room_list)


#Inicio del usso de bf4

resp = driver.page_source

driver.close()

soup = BeautifulSoup(resp, 'lxml')

"""
html = soup.prettify("utf-8")
with open("output1.html", "wb") as file:
    file.write(html)
"""

# Basado en expedia_v2
allRooms = soup.find("div",{"id":"checkout"})
print(allRooms)
Rooms = allRooms.find("a")

for Room in Rooms:
    price_arr=Room.find_all("div",{"class":"sc-bdfBwQ dCKBDk"})
    try:
        o["room-type"]=Room.find("p",{"class":"sc-bdfBwQ sc-gsTCUz sc-dlfnbm dCKBDk bhdLno dNGjwZ"}).find("span",{"class":"sc-bdfBwQ dCKBDk"}).text
    except:
        o["room-type"]=None
    l.append(o)

print(l)