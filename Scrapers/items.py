# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()   # name of the product
    description = scrapy.Field()   # description of product
    meta_description = scrapy.Field()   # short meta description
    meta_title = scrapy.Field()  # meta title
    tags = scrapy.Field()  # Array of strings describing product
    attributes = scrapy.Field()   # Array of Object describing brand, color,  features of product
    enabled = scrapy.Field()  # enabled to be shown in UI boolean
    discontinued = scrapy.Field()   # if product is no longer present boolean 
    slug = scrapy.Field()   # slug for getting human readble text
    sku = scrapy.Field()   # string information
    code = scrapy.Field()  # product code
    tax_class = scrapy.Field()  # tax class
    related_product_ids = scrapy.Field()  # array of product ids
    prices = scrapy.Field()  # list of prices
    cost_price = scrapy.Field()  # float value
    regular_price = scrapy.Field()  # float value
    sale_price = scrapy.Field()  # selling price of product
    quantity_inc = scrapy.Field()  # integer product quant
    quantity_min = scrapy.Field()  # integer min product
    weight = scrapy.Field()  # weight of product
    stock_quantity = scrapy.Field()  # stock quant of product integer
    position = scrapy.Field()  # integer
    date_stock_expected = scrapy.Field()  # date of stock
    date_sale_from = scrapy.Field()  # sale date
    date_sale_to = scrapy.Field()  # end sale date
    stock_tracking = scrapy.Field()  # boolean value
    stock_preorder = scrapy.Field()  # boolean value
    stock_backorder	= scrapy.Field()  # boolean value
    category_id = scrapy.Field()  # string value
    dimensions = scrapy.Field()
    external_url = scrapy.Field()  # external Product url
    external_images = scrapy.Field()  # array of images
    created_at = scrapy.Field()  # created date
    updated_at = scrapy.Field()