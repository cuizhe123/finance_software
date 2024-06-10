import requests
import json

file = open('stock_list.json',mode='w',encoding='utf-8')

license = '5e90797dd137345fd1'
url = f'http://api.mairui.club/hslt/list/{license}'
r = requests.get(url)
data = r.json()

file.write(json.dumps(data, indent=4,ensure_ascii=False))
