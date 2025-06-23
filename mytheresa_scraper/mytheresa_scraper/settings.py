BOT_NAME = "mytheresa_scraper"

SPIDER_MODULES = ["mytheresa_scraper.spiders"]
NEWSPIDER_MODULE = "mytheresa_scraper.spiders"

# Don't obey robots.txt
ROBOTSTXT_OBEY = False

# Reduce logging
LOG_LEVEL = 'INFO'

# Set a user agent (Mytheresa blocks default Scrapy UA)
DEFAULT_REQUEST_HEADERS = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Origin": "https://www.mytheresa.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": '"Chromium";v="123", "Not:A-Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    'Cookie': 'bm_s=YAAQrWQwFz5NMYiXAQAA30I/mwMaTNCE+BbH8n5kFx4ER16TCF5hmICW9UQnu4uRuPyPbXRWz7vXPeC8Mg5lT5MLuctMOttRCKLtWq7fJDZ7jBZik4nMwLjsBHZGMGynctejlyANmRUfgYHc6dUo0MPBeTICszb4xjsl1IFEQRIrQFdqd5y7p62RNlA1WW3kCSA/7CWVEASokt6W5w3J2qyLPyZMwH5ApF3XhxXqMD60eM8fIgMtDKK2DF+7bxLwyKKk83bUFUhCxLxAwUY+myj3/QDdyY5GPvaum2lE+/3sLnn1ilvS0Ar+sAqqaVJs9dqCIng9Np4m06hJG8IYsEUmmj2pAMjhvwZt5GOF1R6M5jXPHK4+WNWethoBQzk3pW9nzO2/g2YNuZwO6V6/1axWzJ29So6WXr0g78sgP7oQTAR14mMxYEm0z1sC4CcqfcHMIU3gCqDyAWW6ZcGNg/ALP7LqhX2iJcTuqqfbT+tmRtUR0YStgik5HFJVHE3LizHzLnrLl6rxRFjjqCmOLt8ud7I3jFIW4cbDFYS/KHAZ7pwPCTnpFOzgeg==; bm_so=D6FE769B2701C419D5AF46BFBF294AF22ECAC05245D273ADF7F1CFA1EE1CBE14~YAAQrWQwFz9NMYiXAQAA30I/mwSU+tTFOn1wEHxSSDyJC0q+ZDksBlhUEtFVNJOSdwH09JrZYnFXBZNtAsx08RTRx0W+bYn1Vg+ZVcHKRtWOsBuQoFg+AlLoFlxivckyCjfFnZKWWnTCL2i2b5J4ZhNeexUWAYqEPbu/P/psxPLv1Y04lCZ3I4sptEK2g7mXhmn+2inMqoZFr0wfVl3PtGbeP/oMNPGtEeIn07LyBEgAmiFO0qcQCqRx5we8ig2ma+fsCPjAHnlFvnlhSd4pqee9mNuQ98+SD9mAscfFI5PACWobKBxt9U0yNmMA3JRU+PawdSL/vA+s+XJwCQR9AKqcq1A/WnHGraPWF+C/FKqHJDSG5tUksVHiiPXyvsotJXQ2Ki5u+lDfpaBtmkwV3cVyvq4ZYPgU30Y5bdhdf0KutKo7IUk9E2HOjOQwKi3kHtpIi8KVSd4Wmp88IhK7Ig==; bm_ss=ab8e18ef4e; mt.v=5.17979398.1750656302633; mt_cdf=000; mt_city=ASHBURN; mt_csf=000; mt_department=men; mt_department_last=men; mt_gate_wall=false; mt_geo=US; mt_polymere=unknown; mt_polymere_crit=unknown; mt_polymere_sha=unknown; mt_sid=mc8nk81t1d4nmeflu; mt_view=en-int%7CIL; mt_zip=20146%252020149; mytuuid=4c9a0533-607b-4a41-9101-3d94a6b4c9cc'
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
]

DOWNLOADER_MIDDLEWARES = {
    'mytheresa_scraper.middlewares.RotateUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # disable default
}


HTTP_PROXY = "scraperapi:458fa92f5567092c5d9d9f6e863ed38d@proxy-server.scraperapi.com:8001"