from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PATH = '/Users/eduardomedina/Documents/GuruTools_manual/hotel/chromedriver_mac_arm64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
options.add_argument('accept-encoding=gzip, deflate, br')
options.add_argument('accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
options.add_argument('referer=https://www.expedia.com/')
options.add_argument('upgrade-insecure-requests=1')

l = []
o  = {}

target_url= "https://www.hotelluca.mx"

driver=webdriver.Chrome(PATH, options=options)
driver.get(target_url)
time.sleep(3)

search_button = driver.find_element("xpath",'//*[@id="searchengine"]/div/div[2]/button')
search_button.click()
time.sleep(7)