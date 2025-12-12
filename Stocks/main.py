import requests
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCKS = "Your api key"
API_KEY_NEWS = "Your api key"

account_sid = "Your account id"
auth_token = "Your auth token"
twillio_number = "your twillio phone number"
my_number = "phone number to send msg to"

now = datetime.now()
yesterday = now - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")

stock_parameters = {

    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCKS,
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday_str,
    "sortBy": "popularity",
    "language": "en",
    "apiKey": API_KEY_NEWS,
    }


stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

closing_prices = [float(price["4. close"]) for price in stock_data["Time Series (Daily)"].values()]
print(closing_prices)

yesterday_price = closing_prices[0]
two_day_closing_price = closing_prices[1]

difference = abs(yesterday_price - two_day_closing_price)
rounded_difference = round(difference, 2)
print(rounded_difference)

percent_difference = (difference / two_day_closing_price) * 100
rounded_percent = round(percent_difference, 2)

if rounded_difference> 1:
    print(rounded_percent)

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"]
    top_three_articles = news_articles[:3]
    print (top_three_articles)
    
    formatted_articles = [f"Headline: {article['title']} \n Brief: {article['description']}" for article in top_three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_= twillio_number,
            to=my_number,
        )
