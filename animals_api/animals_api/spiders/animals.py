import scrapy, logging, pymongo
from scrapy.utils.log import configure_logging 
from pymongo import MongoClient
# Items
from animals_api.items import AnimalsAToZItem, AnimalsFactsItem

class AnimalsSpider(scrapy.Spider):
    name = "animals"
    allowed_domains = ["a-z-animals.com"]
    start_urls = ["https://a-z-animals.com/animals"]

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='logs/animals.log',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def __init__(self, *args, **kwargs):
        super(AnimalsSpider, self).__init__(*args, **kwargs)
        self.client = MongoClient("mongodb://izzun:1234@0.0.0.0:27017/")
        self.db = self.client["animals_a_z"]
        self.collection = self.db["animals"]

    def parse(self, response):
        animals = response.css('li.list-item.col-md-4.col-sm-6 a::attr(href)')
        for anim in animals:
            yield response.follow(anim, self.parse_animals)

    def parse_animals(self, response):

        # Declare items (models)
        item_anim = AnimalsAToZItem()

        item_anim['name'] = response.css('h1.has-text-align-center.has-custom-size.text-white::text').get()

        facts_list = []
        h2_facts = response.css('h2[id^="h-"]')
        for h2 in h2_facts:
            fact = AnimalsFactsItem()
            fact['fact'] = h2.css('::text').get()

            # descriptions = []
            # # Iterate over following-sibling p elements and extract descriptions
            # for p in h2.xpath('following-sibling::p'):
            #     description = p.xpath('normalize-space(string())').get()
            #     descriptions.append(description)
            # # Add descriptions list to the fact item
            # fact['description'] = descriptions
            # facts_list.append(dict(fact))

            fact['description'] = h2.xpath('following-sibling::p[1]').xpath('normalize-space(string())').get()
            facts_list.append(dict(fact))
            
        # add the facts list to the item
        item_anim['facts'] = facts_list

        # Image URL
        image_url = response.xpath('//meta[@property="og:image"]/@content').get()
        item_anim['image_urls']  = [image_url]

        yield item_anim
