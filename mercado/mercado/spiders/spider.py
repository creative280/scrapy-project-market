import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mercado.items import MercadoItem
from scrapy.exceptions import CloseSpider


class MercadoSpider(CrawlSpider):
    name = 'mercado'
    item_count = 0
    allowed_domains = ['www.mercadolibre.com.mx']
    start_urls = ['https://listado.mercadolibre.com.mx/celulares#D[A:celulares]']

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__button andes-pagination__button--next"]'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="ui-search-item__title"]')),
             callback = 'parse_item', follow = False)
    }

    def parse_item(self, response):
        ml_item = MercadoItem()
        
        # Informacion del producto
        ml_item['titulo'] = response.xpath('//h1/text()').get()