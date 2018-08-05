from datetime import datetime as dt
import scrapy
import uuid
from django.utils.text import slugify
from Scrapers.items import Product

class MirrawSpider(scrapy.Spider):
    name = "mirraw_sarees"
    brandId = "49569765-88da-4ab8-99ad-5bad5b2e8d06"
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
        item["id"] = uuid.uuid4()
        item["name"] = extract_with_css('h1::text')
        item["storeUrl"] = response.url
        item["old_price"] = float(extract_with_css('div.old_price_label::text').replace("Rs",""))
        item["price"] = float(extract_with_css('h3.new_price_label::text').replace("Rs",""))

        if item["price"] is None:
            yield None
        item["description"] = extract_with_css('div.key_specifications::text')
        item["meta_description"] = item["description"][:50]+"..."
        item["category"] = "4b628369-cf33-449b-a814-08debaeb02ba"
        item["images"] = extract_with_css('#design_gallery a::attr(data-image)')
        item["slug"] = f'{slugify(item["name"])}-{item["id"].__hash__()%100000}'
        item["sender"] = self.name
        item["brand"] = self.brandId
        
        yield item
        