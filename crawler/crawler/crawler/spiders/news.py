# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.selector import Selector, HtmlXPathSelector
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        #print(response.url)
        #print(response.text)
        #content=str(response.body,encoding='utf-8')
        #找到a标签
        #hxs=Selector(response=response).xpath('//a')
        #for i in hxs:
        #    print(i)
        hxs=Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]/div[@class="news-content"]')
        for i in hxs:
            a=i.xpath('.//div[@class="part1"]/a/text()').extract_first()
            print(a.strip())
