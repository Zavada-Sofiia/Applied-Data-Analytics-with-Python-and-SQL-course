# Importing Modules
import scrapy
from scrapy.crawler import CrawlerRunner # To Run our spider

# Setting up crochet
import crochet
crochet.setup()

# Building the Spider
class BookSpider(scrapy.Spider):
    name='BookSpider' # used to invoke spider

    # Used to start the requests
    start_urls=['http://books.toscrape.com/catalogue/page-1.html',
                'http://books.toscrape.com/catalogue/page-2.html',
                'http://books.toscrape.com/catalogue/page-3.html']

    """
    Invoked by scrapy engine for every url
    Here we wil use selectors to scrap the website
    """
    def parse(self, response):
        book_list=response.css('article.product_pod>h3>a::attr(title)').getall()

        for i in book_list:
            print(i)

# Crawling with spider
process = CrawlerRunner({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})
process.crawl(BookSpider)
