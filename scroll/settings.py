
BOT_NAME = 'scroll'

SPIDER_MODULES = ['scroll.spiders']
NEWSPIDER_MODULE = 'scroll.spiders'

ROBOTSTXT_OBEY = True

PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": False}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

