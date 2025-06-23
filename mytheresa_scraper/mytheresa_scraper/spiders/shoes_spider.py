import scrapy
from scrapy.http import JsonRequest


class ApiSpider(scrapy.Spider):
    name = "api_spider"
    allowed_domains = ["mytheresa.com"]
    start_page = 1
    end_page = 31 

    def start_requests(self):
        for page in range(self.start_page, self.end_page + 1):
            payload = {
                "query": """
                query XProductListingPageQuery($page: Int, $size: Int, $slug: String) {
                  xProductListingPage(page: $page, size: $size, slug: $slug) {
                    products {
                      slug
                    }
                  }
                }
                """,
                "variables": {
                    "page": page,
                    "size": 60,
                    "slug": "/shoes"
                }
            }

            yield JsonRequest(
                url="https://api.mytheresa.com/api",
                method="POST",
                data=payload,
                callback=self.parse
            )

    def parse(self, response):
        products = response.json()["data"]["xProductListingPage"]["products"]
        for product in products:
            slug = product.get("slug")
            if slug:
                yield {
                    "product_url": f"https://www.mytheresa.com/int/en/men{slug}"
                }
