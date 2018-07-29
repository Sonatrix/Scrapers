from datetime import datetime as dt
import scrapy
import uuid
from django.utils.text import slugify
from Scrapers.items import Product

class NeetiSpider(scrapy.Spider):
    name = "neeti_kurti"
    brandName = "Neeti Collections"
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
        item["id"] = uuid.uuid4()
        item["name"] = extract_with_css('h1::text')
        item["storeUrl"] = response.url
        item["old_price"] = float(extract_with_css('span.price::text').replace("₹",""))
        item["price"] = float(extract_with_css('span.price::text').replace("₹",""))

        if item["price"] is None:
            return None
        item["description"] = extract_with_css('p.form-group::text')
        item["meta_description"] = item["description"][:30]+"..."
        item["category"] = "ccae8991-605d-479d-929c-899e53ccf18a"
        item["images"] = extract_with_css('div.large-image img::attr(src)')
        item["slug"] = f'{slugify(item["name"])}-{item["id"].__hash__()%100000}'
        item["sender"] = self.name
        item["brand"] = self.brandName
        
        yield item