import requests
from bs4 import BeautifulSoup

PRODUCT_URL = 'https://www.amazon.com/ALIENWARE-AW2521HF-24-5-Gaming-Monitor/dp/B087N4LQPN/ref=sr_1_7?dchild=1' \
              '&keywords=monitor&qid=1625253367&refinements=p_n_size_browse-bin%3A3547806011&rnid=2633086011&s=pc&sr' \
              '=1-7 '
REQ_HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36 ",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',
    'Connection': 'close'
}

res = requests.get(url=PRODUCT_URL, headers=REQ_HEADER)
soup = BeautifulSoup(res.text, 'html.parser')
price = soup.find(id='price_inside_buybox')
price_str = price.text.strip('\n')
price_float = float(price_str[1:])

if price_float < 270.00:
    print(f"Currently selling at a discount: {price_str} Buy now!")
    # send email
else:
    print("something went wrong.")



