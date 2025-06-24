import asyncio
from playwright.async_api import async_playwright
import random
import os

# Load user agents from a file
def load_user_agents(file_path="user_agents.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError("user_agents.txt not found.")
    with open(file_path, "r") as file:
        user_agents = [line.strip() for line in file if line.strip()]
    return user_agents

async def scroll_page(page, scroll_delay=1000, scroll_count=5):
    for _ in range(scroll_count):
        await page.mouse.wheel(0, random.randint(1000, 2000))
        await asyncio.sleep(scroll_delay / 1000)

async def fetch_page_with_playwright_async(url):
    user_agents = load_user_agents()
    user_agent = random.choice(user_agents)

    headers = {
    "accept": "*/*",
    "accept-language": "en",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://www.mytheresa.com",
    "referer": "https://www.mytheresa.com/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": user_agent,
    "x-country": "IN",
    "x-geo": "IN",
    "x-nsu": "false",
    "x-region": "KL",
    "x-section": "men",
    "x-store": "INT",
    "x-tracking-variables": "analyticsId=null,browser=Chrome,browserLanguage=en,campaign=unknown,channel=en-int,channel_country=IN,channel_language=en,countOfPageViews=10,countOfSessions=1,cdf=000,csf=000,cdf_1=0,cdf_2=0,cdf_3=0,csf_1=0,csf_2=0,csf_3=0,department=men,devicePlatform=web,deviceSystem=Linux,deviceType=bot,emailHash=null,environment=production,ipAddress=2001:4490:4e75:bbc7:1dea:8ef0:3a6e:b2d,loggedStatus=false,mytuuid=c661f34b-cc35-4a5e-9d2e-ac15cd2609b0,level_0=men,level_1=men_taxon_5076,pageId=men_taxon_5076,pageType=listpage,referral=unknown,sessionId=mc8h80rw26sasr1gd,source=unknown,url=https://www.mytheresa.com/int/en/men/shoes,queryParams=page%3D20,version=4.19.1,experience_globalBlue_closed=false,experience_pocketBanner1_pocketBanner1_seen=true,experience_pocketBanner2_pocketBanner2_seen=true,experience_topLevelBanner_tlb_mw_promo_sale_70_seen=true,experience_pdpDisclaimer_pdpDisclaimer_seen=false,experience_topLevelBanner_tlb_mw_db_nlsignup_seen=false,monetateId=5.311027350.1750572611721'",
    "cookie": 'bm_ss=ab8e18ef4e; bm_mi=5CE1415FB5BA88C44DE882C6D63311C9~YAAQZY3vdYp/RGCXAQAAmBNlnBzHnc0iafVY8Cr1yECtogu9Ahj6A+J5cZ1JrpORpYYXR+1arxLmTaDglRKYe4Ne+nz4inpBWco0Zw0/QttYljSfd35XRYWyGZc8+CWXi2jUfuH2i/chNSm7DWlbkG9Pw68/OOYz/NrkyTJIwaPgNv08WWHBBgeau7pXygsO5hFsWDkcIr+WY9PyL/nU6ZL+b0RIW2acsjwtWdqr7HCX5melPejHvFwjpWgEuiL6OBwF2pAWmuemC26ZNQsbFeAdM8gnK9VKdU90C2TLdiXVCy1GKMD8BsPri7boxyyk9oWigEAE779o6vB852JfZQ==~1; ak_bmsc=3148CA376B83325E0A556B0CA7016127~000000000000000000000000000000~YAAQZY3vddh/RGCXAQAAlyFlnBx6zNdl5H7zaYPYDvOcmQyy+48tv/vbACRwssB1pKHCi4gaJliqWxq/e7Ii6Ai8bSVUYESEeucYmGxllXe6/Ct81rPqDvUwMltrC3HZxTVlrS6rE/L63coYLJHpy3AGh3rs/i5A76UYcFxuT1apl/q5oJv8eaiYuH+euEDk3/oKxY9kO7vLrWd+gkeIKdyD+d2CfXnDJHg2fxcAQRYlcjfqQpPQzTnYuiK2ExAnAQmQA90jfAdjnXGiGMDwObhd95lHgiqvaMC+Qgr5zjMpfbWTCvxi5lJHVR5yYejfDy39cPPvduGql+budfHm7uG8uRRUQHgN5KoqV/kCk2yM2C8b81OZwE+9XGneMsvuiNf5C7oMwyGHkMLNh+jMtxswzt5EDJRhi0DT3R6519kwUwAuHspTuhBy35US/Kzftciy6xFVGfsEWggAT49Kmjh2SzZKbn2NDpidkcOY0AyTTnK6KQj+hMNLiKZWaLnPxFH3751ibmJ+qQo0cfoRxGk=; bm_so=52911C4D438AC8B15DE47D695C65A81A2CB73BB32DAA9D1A21230A2C75828D76~YAAQbo3vdcS9k2CXAQAAlIOZnARTE3qeonft1SWJgCCk1bMv7A7SR0El/+NV+NUyIymUCXm4UwpuHHeXlDNDjoS1UV5x4T57/O91KFlvNRDUfyL/QYfIoP5ZreJbd8EbyfPlDD/2cw4OpSsifOKIlEj/zua4r1WDm91lmVC9fvydcXoH1i5THQOTXi9240z2wCxBueF+pwwq5x21hT4QJGC2yXHRVPvySd4qoMFRJR9e/hcpfrQwrDXlozIM63EL4TY6IxNWxMmuVfmRLyQ34gR015hnPZgofp8K1B8pm9gwzdFzKzpaAgK9eJE7ImdC28WEjsBSPA+7e/S4crt5goXceaBbpzyvN4r3pg/BO7VNTK51WfjezZ72Qdzgl+1s8UqnMzXOq9/jCLOEfiIAmsZFl3O+EncWkSBmFRcNzjIvNEXzklCQzQRJeT0aOwiQuhDRwOlVbePxga+WSHIDrx3horJd3C58F30ys0G9cqzRrUp4Dm8DFaUZ; bm_s=YAAQVYgsMWVNDoCXAQAASc+ZnAP4wV0tyW4FHJIAf7KjV8bXujFlwN7rIeuHc2M9AIIAN4LjI+b04R+CzSXkdAs078q77oHJAo/9j/lBQqP6huUwRVi9qWOYw3XD9yo3k44/swWyOw0kFjXnxI3MWFQvpQZj2eiuACYE50RcanI55H4efo56Dyr1G+GEqT6en3xKpzd5pFrfGgSKiWrKxvrH3iEmwhEGJ2B9WUbMzZmN/PTq10EbRJ9qI6XzzkItPFaGNIxGB2uIoqvuxG6hhHvcJ5jFpucG0XO/xcrqk5Bi7EE1IOwDrNx+JTPkHetz9sghPXnfJb2XBho/8dhmq1mfD3va4QgherACd2RYL/tbwS6WQ0lga5U296Zl5y9wyiThFIrTlGF0q6ieo5n8KG1wJuZkKWO7BazAzYJK9Pu1bnc1Wqx3c57LDwzSjOtUyBVjQpyXKAfcwk1/s7uOFe3Mz5jxd9Sb58NoJo264zsKDYBiF0ovDRKQ4REy7c/2ntdzMrkY6rtTG0tovrWTP2ps9CH2Q4JE9reP6gi0uoMDm8CxT51jaGGiVRwsV4/x3YtInWlTyE68nbuxjj3EaGIJFN2uJMD40OcD2YNsiQreS9nu/+Pcr6iqoAMae82Cj2tadBfe'
}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent=user_agent,
            extra_http_headers=headers,
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        await asyncio.sleep(random.uniform(5, 10))  # Human-like delay

        await page.goto(url, timeout=60000)
        await page.wait_for_load_state("networkidle")

        await scroll_page(page, scroll_delay=random.randint(800, 1200), scroll_count=random.randint(3, 6))

        content = await page.content()
        await browser.close()
        return content
