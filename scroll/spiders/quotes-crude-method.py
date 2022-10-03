import scrapy
from scrapy.utils.response import open_in_browser
from scrapy_playwright.page import PageMethod


class QuotesScrolCrudeSpider(scrapy.Spider):
    name = 'scroll_crude'

    def start_requests(self):

        yield scrapy.Request(
            url='http://quotes.toscrape.com/scroll',
            meta={
                'playwright': True,
                'playwright_page_methods': [
                    PageMethod('evaluate', 'window.scrollBy(0, document.body.scrollHeight)'),
                    PageMethod('wait_for_selector', f'.quote:nth-child(11)'),
                    PageMethod('evaluate', 'window.scrollBy(0, document.body.scrollHeight)'),
                    PageMethod('wait_for_selector', f'.quote:nth-child(21)'),
                    PageMethod('evaluate', 'window.scrollBy(0, document.body.scrollHeight)'),
                    PageMethod('wait_for_selector', f'.quote:nth-child(31)'),
                    PageMethod('evaluate', 'window.scrollBy(0, document.body.scrollHeight)'),
                    PageMethod('wait_for_selector', f'.quote:nth-child(41)'),
                ]
            })

    def parse(self, response):
        for q in response.css('.quote'):
            yield {
                'author': q.css('.author ::text').get(),
                'quote': q.css('.text ::text').get()
            }

