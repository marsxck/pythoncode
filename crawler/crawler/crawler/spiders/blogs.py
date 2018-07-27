# -*- coding: utf-8 -*-
import scrapy


class BlogsSpider(scrapy.Spider):
    name = 'blogs'
    allowed_domains = ['blogs.com']
    start_urls = ['http://blogs.com/']

    def parse(self, response):
        pass
