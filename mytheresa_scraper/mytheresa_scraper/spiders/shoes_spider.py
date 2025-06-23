import scrapy

class MytheresaSpider(scrapy.Spider):
    name = "mytheresa"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def parse(self, response):
        # Print response status
        print(f"\nResponse status code: {response.status}")

        # Print raw HTML (first 5000 characters)
        print("\n--- RESPONSE HTML (truncated) ---")
        print(response.text[:5000])

        # Extract product URLs
        links = response.css('a.link__item::attr(href)').getall()
        product_links = ["https://www.mytheresa.com" + link for link in links if link.startswith("/")]

        # Print product URLs
        print("\n--- PRODUCT LINKS ---")
        for url in product_links:
            print(url)

        print(f"\nTotal product links scraped: {len(product_links)}")
