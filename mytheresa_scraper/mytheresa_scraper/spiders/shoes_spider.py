import scrapy
from scrapy_playwright.page import PageMethod

class MyTheresaSpider(scrapy.Spider):
    name = "mytheresa"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "a.item__link"),
                ],
            },
            callback=self.parse,
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        # Click "Show more" repeatedly until it's gone
        while await page.query_selector("a.button.button--active"):
            await page.click("a.button.button--active")
            await page.wait_for_timeout(1500)  # wait for new items to load

        html = await page.content()
        response = response.replace(body=html)

        # Extract product URLs
        links = response.css("a.item__link::attr(href)").getall()
        product_links = ["https://www.mytheresa.com" + l for l in links if l.startswith("/")]

        for url in product_links:
            yield {"url": url}

        await page.close()
