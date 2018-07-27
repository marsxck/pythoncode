# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.selector import Selector, HtmlXPathSelector
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        #print(response.text)
        #hxs=Selector(response=response).xpath('//div[@class="bili-wrapper"]//p//@title')
        #for i in hxs:
            #print(i)
        print(response.request.headers['User-Agent'])
        print(response.text)