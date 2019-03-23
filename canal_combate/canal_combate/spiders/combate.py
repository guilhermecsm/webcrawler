# -*- coding: utf-8 -*-
import scrapy

class CombateSpider(scrapy.Spider):
    name = 'combate'

    def start_requests(self):
        lista_url = ["http://sportv.globo.com/site/combate/index/feed/pagina-{}.ghtml".format(num) for num in range(1,5)]

        for url in lista_url:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        print(response.xpath("//div[@class='feed-post-body-title gui-color-primary gui-color-hover ']//div//a/text()").extract())
            

