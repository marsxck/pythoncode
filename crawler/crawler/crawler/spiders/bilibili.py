# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bili.com']
    start_urls = ['http://bili.com/']

    def parse(self, response):
        pass
