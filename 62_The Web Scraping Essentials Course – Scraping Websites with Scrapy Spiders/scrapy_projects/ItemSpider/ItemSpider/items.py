# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyDetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_price_intraday = scrapy.Field()
    company_symbol = scrapy.Field()
    company_symbol_link = scrapy.Field()
