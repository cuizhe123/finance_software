import requests
import json

file = open('data2.txt',mode='w',encoding='utf-8')
api_key = '6IXMK48DD4XH608T'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json()
file.write(json.dumps(data, indent=4))
# print(json.dumps(data, indent=4))

# 中国交易的股票代码样本 - 上海证券交易所
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo'
file = open('data3.txt',mode='w',encoding='utf-8')
r = requests.get(url)
data = r.json()
file.write(json.dumps(data, indent=4))