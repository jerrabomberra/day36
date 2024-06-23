import requests
from datetime import datetime, timedelta
import datetime
import calendar

dt = datetime.date.today()

def is_workday(dt):
    today = dt.weekday()
    if  today == 5:
        yesday = today -2
        today -=1
    elif today == 6:
        yesday = today -3
        today -= 2
    return today, yesday
        

print(is_workday(dt))
# 
# print(is_workday()

# def get_news():
#     url = ('https://newsapi.org/v2/top-headlines?'
#         'country=us&'
#         'apiKey=141cf29006174fbd9518b6271269bd1b')
#     response = requests.get(url)
#     return response.json()

# def get_stock():
#     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
#     r = requests.get(url)
#     data = r.json()
#     yest_day = data['Time Series (Daily)']['2024-06-21']['4. close']
#     return yest_day

# # print(get_news())
# print(get_stock())


# if __name__ == "__main__":
#     print("Hello, World!")
