from scrapy import Spider, Request
from scrapy.selector import Selector
import asyncio
import json
from mytheresa_scraper.playwright_helper import fetch_page_with_playwright_async

class ProductDataSpider(Spider):
    name = "product_data"

    async def start(self):
        with open("products.json") as f:
            urls = json.load(f)

        for item in urls[:3]:
            yield Request(url=item["product_url"], callback=self.parse, dont_filter=True)

    async def parse(self, response):
        html = await fetch_page_with_playwright_async(response.url)
        sel = Selector(text=html)

        # EXTRACTING BREADCRUMBS
        breadcrumbs = sel.css("div.breadcrumb__item *::text").getall()
        breadcrumbs = [b.strip() for b in breadcrumbs if b.strip()]
        #EXTRACTING IMAGE URL
        image_url=sel.css("div.photocarousel__items > div > div > div.swiper-slide.swiper-slide-active::attr(src)").get(default="not found")
        # EXTRACTING BRAND AND PRODUCT NAME
        brand = sel.css("a.product__area__branding__designer__link::text").get(default="not found")
        product_name = sel.css("div.product__area__branding__name::text").get(default="not found")
        #EXTRACTING LISTING PRICE
        listing_price = sel.css("span.pricing__prices__value pricing__prices__value--original::text").get(default="not found")
        #EXTRACTING OFFEER pRICE
        offer_price = sel.css("span.pricing__prices__value pricing__prices__value--discount::text").get(default="not found")
        #EXTRACTING DISCOUNT PERCENTAGE
        discount_percentage = sel.css("span.pricing__info__percentage::text").get(default="o% Off")
        #EXTRACTING PRODUCT ID
        product_id = sel.css("div.product__area__branding__id::text").get(default="not found")
        #EXTRACTING SIZES
        sizes = sel.css("div.product__area__size__select__option::text").getall()
        sizes = [size.strip() for size in sizes if size.strip()]
        #EXTRACTING DESCRIPTION
        description = sel.css("div.accordion__body__content::text").get()
        #EXTRACTING OTHER IMAGE URLS
        other_image_urls = sel.css("div.photocarousel__items > div > div > div.swiper-slide::attr(src)").getall()
        other_image_urls = [url for url in other_image_urls if url]

        yield {
            "url": response.url,
            "breadcrumbs": breadcrumbs,
            "image_url": image_url,
            "brand": brand,
            "product_name": product_name,
            "listing_price": listing_price,
            "offer_price": offer_price,
            "discount_percentage": discount_percentage,
            "product_id": product_id,
            "sizes": sizes,
            "description": description,
            "other_image_urls": other_image_urls
        }
