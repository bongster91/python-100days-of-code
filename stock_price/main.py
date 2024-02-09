import requests

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_API_KEY = ''
NEWS_API_KEY = ''

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOITN = 'https://newsapi.org/v2/everything'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = abs( float(yesterday_closing_price) - float(day_before_yesterday_closing_price) )

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOITN, params=news_params)
    articles = news_response.json()['articles']
    
    three_articles = articles[:3]
    formatted_articles = [articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    for article in formatted_articles:
        message = client.message.create(
            body=article,
            
        )
    