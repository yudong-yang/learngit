import scrapy

class qiushiSpider(scrapy.Spider):
    name = "qiushi"
    allowed_domains = ["www.qiushibaike.com"]
    start_urls = [
        "https://www.qiushibaike.com/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)