import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def scrape_stock_info(stock):
  url = "https://finance.yahoo.com/quote/{}".format(stock)
  response = requests.get(url)

  if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Find the stock price.
    price_el = soup.find("span", attrs={"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
    price = price_el.text.strip() if price_el else None

    # Find the stock's market cap.
    market_cap_el = soup.find("td", attrs={"data-test": "MARKET_CAP-value"})
    market_cap = market_cap_el.text.strip() if market_cap_el else None

    # Find the stock's 52-week range.
    range_el = soup.find("td", attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"})
    range = range_el.text.strip() if range_el else None

    # Find the recent headlines for the stock.
    headlines_el = soup.find_all("h3", attrs={"class": "Mb(5px)"})
    headlines = [headline.text.strip() for headline in headlines_el]

    return {
      "price": price,
      "market_cap": market_cap,
      "range": range,
      "headlines": headlines
    }
  else:
    return None


info = scrape_stock_info("AAPL")
print(info)
# Output: 
# {
#   "price": "123.45",
#   "market_cap": "1.23T",
#   "range": "100.00 - 150.00",
#   "headlines": ["Headline 1", "Headline 2", "Headline 3"]
# }