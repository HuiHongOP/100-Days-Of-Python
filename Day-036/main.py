import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = '************'
TIME_SERIES = 'TIME_SERIES_DAILY'

NEWS_API_KEY = '**********'

parameters = {
    'function': TIME_SERIES,
    'symbol': STOCK_NAME,
    'apikey': API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']

today_date = dt.datetime.today().strftime('%Y-%m-%d')
yesterday_date = (dt.datetime.today() - dt.timedelta(days=1)).strftime('%Y-%m-%d')

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_SP = float(stock_data[yesterday_date]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price
today_SP = float(stock_data[today_date]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
pos_diff = abs(yesterday_SP-today_SP)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = (pos_diff / today_SP) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 5:
    print('Get News')
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']


    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

