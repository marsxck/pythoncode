# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector
from ..items import ChoutiItem
#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']
    
    visited_urls=set();
    def start_requests(self):
         for url in self.start_urls:
                yield Request(url,callback=self.parse)
    def md5(self,url):
        import hashlib
        obj=hashlib.md5()
        obj.update(bytes(url,encoding='utf-8'))
        return obj.hexdigest()
    def parse(self, response):
        #print(response.url)
        #print(response.text)
        #content=str(response.body,encoding='utf-8')
        #找到a标签
        #hxs=Selector(response=response).xpath('//a')
        #for i in hxs:
        #    print(i)
        #提取标题和链接
        hxs1=Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]/div[@class="news-content"]')
        for i in hxs1:
            title=i.xpath('.//div[@class="part1"]/a/text()').extract_first().strip()
            href=i.xpath('.//@href').extract_first().strip()
            item_obj=ChoutiItem(title=title,href=href)
            yield item_obj
        
        hxs=Selector(response=response).xpath('//a[re:test(@href,"/all/hot/recent/\d+")]/@href').extract()
        for url_s in hxs:
            md5_url = self.md5(url_s)
            if md5_url in self.visited_urls:
                pass
            else: 
                self.visited_urls.add(md5_url)
                url="http://dig.chouti.com%s"%url_s
                yield Request(url=url,callback=self.parse)
