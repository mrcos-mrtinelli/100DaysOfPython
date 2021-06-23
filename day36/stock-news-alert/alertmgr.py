import requests

api_key_alphavantage = ''
api_key_newsapi = ''

daily_data_param = "Time Series (Daily)"
close_price_param = "4. close"


class AlertManager:

    def __init__(self, symbol):
        self.symbol = symbol
        self.latest_prices = self.get_stock_price()
        self.percent_change = self.get_price_fluctuation()

    def get_stock_price(self):
        url = 'https://www.alphavantage.co/query'
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.symbol,
            "apikey": api_key_alphavantage
        }
        response = requests.get(url=url, params=parameters)
        response.raise_for_status()
        json_data = response.json()
        refresh_dates = list(json_data[daily_data_param])[:2]
        last_close = json_data[daily_data_param][refresh_dates[0]][close_price_param]
        previous_close = json_data[daily_data_param][refresh_dates[1]][close_price_param]
        return last_close, previous_close

    def get_price_fluctuation(self):
        today_close = float(self.latest_prices[0])
        yesterday_close = float(self.latest_prices[1])
        print(today_close)
        print(yesterday_close)
        return round((today_close - yesterday_close) / today_close * 100, 2)

    def get_news(self):
        url = 'https://newsapi.org/v2/everything'
        parameters = {
            "q": f"{self.symbol} stock",
            "apiKey": api_key_newsapi
        }
        response = requests.get(url=url, params=parameters)
        response.raise_for_status()
        articles = response.json()
        return articles['articles'][:3]

    def send_alert(self):
        news = self.get_news()
        indicator = "🆙" if self.percent_change > 0 else "🔻"

        for article in news:
            message = f"Subject:{self.symbol} is {indicator} {abs(self.percent_change)}%\n\n" \
                      f"Headline: {article['title']}\n" \
                      f"Brief: {article['description']}\n" \
                      f"Link: {article['url']}"
            print(message)
