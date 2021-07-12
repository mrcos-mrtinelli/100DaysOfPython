from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time

REQ_HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36 ",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',
    'Connection': 'close'
}
RESEARCH_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSertDRcVd5EZ8V5J9Y5vcK9vPrnsKTDFKp_YF80P0d3RjUjEA/viewform' \
                '?usp=sf_link'
ZILLOW_RESULTS = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
                 '%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22' \
                 '%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C' \
                 '%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22' \
                 '%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22' \
                 '%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C' \
                 '%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B' \
                 '%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D' \
                 '%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D '

APTS = 'li article.list-card'
APT_ADDRESS = 'address.list-card-addr'
APT_PRICE = 'div.list-card-price'
APT_LINK = 'a.list-card-link'

# r = requests.get(url=f'{ZILLOW_RESULTS}', headers=REQ_HEADER)

with open("page.html", mode="r") as f:
    page_str = f.read()


bs_page = BeautifulSoup(page_str, 'html.parser')

listings = bs_page.select(APTS)

clean_listings = []
for listing in listings:
    addr = listing.select(APT_ADDRESS)
    price = listing.select(APT_PRICE)
    link = listing.select(APT_LINK)

    if len(addr) > 0 and len(price) > 0 and len(link):
        result = {
            "address": addr[0].getText(),
            "price": price[0].getText(),
            "link": link[0]['href']
        }
        clean_listings.append(result)

chrome_driver_path = "/Users/marcos/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(RESEARCH_FORM)

for apt in clean_listings:
    time.sleep(1)
    prop_addr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prop_addr.send_keys(apt['address'])

    price_mo = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_mo.send_keys(apt['price'])

    link_ad = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_ad.send_keys(apt['link'])

    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(1)

    submit_another = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
