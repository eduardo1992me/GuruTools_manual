import scrapy


class ExpediaSpiderSpider(scrapy.Spider):
    name = "expedia_spider"
    allowed_domains = ["www.expedia.mx"]
    start_urls = ["https://www.expedia.mx/Playa-Del-Carmen-Hoteles-La-Pasion-Hotel-Boutique-By-Bunik.h5151337.Informacion-Hotel?chkin=2023-06-15&chkout=2023-06-20"]

    def parse(self, response):
        room_raw = response.xpath('//div/div/div/h3/text()').getall()

        yield {
            'room_raw':room_raw
        }
