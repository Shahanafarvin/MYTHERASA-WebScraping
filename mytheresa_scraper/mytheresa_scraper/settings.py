BOT_NAME = "mytheresa_scraper"

SPIDER_MODULES = ["mytheresa_scraper.spiders"]
NEWSPIDER_MODULE = "mytheresa_scraper.spiders"

# Don't obey robots.txt
ROBOTSTXT_OBEY = False

# Reduce logging
LOG_LEVEL = 'INFO'

# Set a user agent (Mytheresa blocks default Scrapy UA)
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}