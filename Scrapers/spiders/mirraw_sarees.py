from datetime import datetime as dt
import scrapy
import uuid
from django.utils.text import slugify
from Scrapers.items import Product

class MirrawSpider(scrapy.Spider):
    name = "mirraw_sarees"
    start_urls = [
        'https://www.mirraw.com/store/sarees',
        'https://www.mirraw.com/store/sarees?min_price=1350&max_price=3825&sort=bstslr&created_at=45&icn=saree_1&ici=bestsellingsarees',
        'https://www.mirraw.com/store/sarees?category_ids=144&min_price=1350&max_price=3825&sort=bstslr'
    ]

    def parse(self, response):
        # follow links to author pages
        for product in response.css('#design-row-block .listings .design_div'):
            href_link = 'https://www.mirraw.com'+product.css("a::attr('href')").extract_first()
            yield response.follow(href_link, self.parse_author)

        # follow pagination links
        #for href in response.css('li.next a::attr(href)'):
            #yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first() 
        item = Product()
        item["id"] = uuid.uuid4().hex
        item["name"] = extract_with_css('h1::text')
        item["storeUrl"] = response.url
        item["old_price"] = float(extract_with_css('div.old_price_label::text').replace("Rs",""))
        item["price"] = float(extract_with_css('h3.new_price_label::text').replace("Rs",""))

        if item["price"] is None:
            yield None
        item["description"] = extract_with_css('div.key_specifications::text')
        item["meta_description"] = item["description"][:50]+"..."
        item["category"] = "50d42760c3ce4a32a31d75a9add01d64"
        item["images"] = extract_with_css('#design_gallery a::attr(data-image)')
        item["slug"] = f'{slugify(item["name"])}-{item["id"][1:6]}'
        yield item