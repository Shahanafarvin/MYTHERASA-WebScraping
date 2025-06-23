import scrapy

class MytheresaSpider(scrapy.Spider):
    name = "mytheresa"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def parse(self, response):
        print(f"\n🔍 Response status code: {response.status}")

        # Debug: Print a slice of the HTML to detect bot blocks
        print("\n--- HTML Preview ---")
        print(response.text[:3000])

        # Extract product URLs from anchor tags
        links = response.css('a.item__link::attr(href)').getall()
        product_links = [
            "https://www.mytheresa.com" + link
            for link in links
            if link.startswith("/")
        ]

        print("\n✅ Product Links:")
        for url in product_links:
            print(url)

        print(f"\n🔢 Total links scraped: {len(product_links)}")
