from datetime import datetime as dt
import scrapy
from Scrapers.items import Product

class NeetiSpider(scrapy.Spider):
    name = "clothing"
    start_urls = [
        'https://www.neeticollections.com/Kurtis',
    ]

    def parse(self, response):
        # follow links to author pages
        for product in response.css('.quickview'):
            href_link = product.css("a::attr('href')").extract_first()
            yield response.follow(href_link, self.parse_author)

        # follow pagination links
        #for href in response.css('li.next a::attr(href)'):
            #yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()
        item = Product()
        item["name"] = extract_with_css('h1::text')
        item["storeUrl"] = response.url
        item["old_price"] = float(extract_with_css('span.price::text').replace("₹",""))
        item["price"] = float(extract_with_css('span.price::text').replace("₹",""))
        item["description"] = extract_with_css('p.form-group::text')
        item["category"] = "d05a20dac39f4c63a135d1de6c7a5577"
        item["images"] = extract_with_css('div.large-image img::attr(src)')
        yield item