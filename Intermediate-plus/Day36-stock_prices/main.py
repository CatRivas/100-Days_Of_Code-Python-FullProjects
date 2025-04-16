import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
import pandas as pd


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def main():
    yest_clos_price, day_b_yest_clos_price = get_stock_prices()
    price_variation = calculate_percentage(yest_clos_price, day_b_yest_clos_price)
    if price_variation:
        latest_news = get_news_related()
        send_message(price_variation, latest_news)
    else:
        print('Your stock is fine, go to sleep 😴.')
        

## STEP 1: Use https://www.alphavantage.co
def get_stock_prices():
    load_dotenv()
    PRICES_API_KEY= os.getenv("AV_API_KEY")

    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey':PRICES_API_KEY,
        'outputsize':'compact',
    }

    url = "https://www.alphavantage.co/query"

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()
        data = response.json()
       

    except requests.exceptions.RequestException as e:
        print("Error durante la solicitud:", e)

    # unpacking the response data
    _, daily_data = data

    #convert to dataframe  
    df = pd.DataFrame.from_dict(data[daily_data], orient='index')
    #clean up columns names
    df_cols = [i.split('. ')[1] for i in df.columns]
    df.columns = df_cols
    df = df.reset_index(0)
    df.rename(columns= {'index': 'Date'}, inplace=True)

    # retornando los precios de cierre 
    yesterday_closing_price = df.loc[0]['close']
    day_before_yesterday_closing_price= df.loc[1]['close']
    
    return yesterday_closing_price, day_before_yesterday_closing_price


# When STOCK price increase/decreases by 0.5% between yesterday and the day before yesterday then print("Get News").
def calculate_percentage(y_data, b_y_data):
    y_data = float(y_data)
    b_y_data = float(b_y_data)
    difference = y_data - b_y_data
    if difference < 0:
        stock_variation = "🔻"
    else:
        stock_variation = "🔺"

    percentage_difference =  abs(round((difference / b_y_data) * 100))
    if percentage_difference > 0.5:
        return f"{stock_variation} {percentage_difference}%"
    
    return None


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_related():
    load_dotenv()
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
 
    parameters = {
        'q': COMPANY_NAME,
        'apiKey':NEWS_API_KEY,
        'language': 'en',
    }

    endpoint = "https://newsapi.org/v2/everything"

    try:
        response = requests.get(endpoint, params=parameters)
        response.raise_for_status()
        data = response.json()
    
    except requests.exceptions.RequestException as e:
        print("Error durante la solicitud:", e)

    three_articles = data.get('articles')[:3] 
    news_related_formatted = [f"Headline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]

    return news_related_formatted


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message(stock_difference, articles_list):
    load_dotenv()
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

        
    for article in articles_list:
        message = client.messages.create(

            body= f"{STOCK}: {stock_difference} \n{article}",
            from_="+17623202360",
            to="+51965813852",
        )

        print(message.body)   


if __name__ == '__main__':
    main()

