import scrapy
from scrapy import Selector


class BookingTestSpider(scrapy.Spider):
    name = "booking_test"
    allowed_domains = ["www.booking.com"]
    start_urls = ["https://www.booking.com/hotel/mx/galerias-inn.es.html?aid=304142&label=gen173nr-1FCAsooAFCFmZyYW5jaWEtYWd1YXNjYWxpZW50ZXNIClgEaKABiAEBmAEKuAEHyAEV2AEB6AEB-AECiAIBqAIDuALp-uqjBsACAdICJDkxZTYxMDA0LWVhZTctNGU2Zi05YzkwLWQ1NTRjNzUzYjBjZdgCBeACAQ&sid=f67404d152aa1ab42bb715f01a8a3653&checkin=2023-09-22&checkout=2023-09-23&dest_id=-1649885&dest_type=city&dist=0&group_adults=2&group_children=0&no_rooms=1&sb_price_type=total&type=total&ucfac=151&"]
    # print("Ingresa la URL del Hotel: ")
    # start_urls[0] = input()
    

    def parse(self, response):
        rooms_raw = response.xpath('//div/div/a/span/text()').getall()
        # Otra opción con xptah: //span[@class'prco-valign-middle-helper']
        # price_raw = response.xpath('//span[@class'prco-valign-middle-helper']').getall()
        # 
        
        yield {
            # 'price_raw':price_raw,
            'rooms_raw':rooms_raw
        }

        