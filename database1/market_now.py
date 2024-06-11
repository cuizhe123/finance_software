import akshare as ak
import pandas as pd
import json

import mysql.connector
import connect

def market_now(say:int = 0):
    dict_all = {'上证指数':[], '深证成指':[], '北证50':[], '沪深300':[]} 
    try:
        df = ak.stock_individual_spot_xq(symbol='SH000001',timeout=1)
        df_dict = df.to_dict(orient='records')
        dict_all['上证指数'] = df_dict

        df = ak.stock_individual_spot_xq(symbol='SZ399001',timeout=1)
        df_dict = df.to_dict(orient='records')
        dict_all['深证成指'] = df_dict

        df = ak.stock_individual_spot_xq(symbol='BJ899050',timeout=1)
        df_dict = df.to_dict(orient='records')
        dict_all['北证50'] = df_dict

        df = ak.stock_individual_spot_xq(symbol='SH000300',timeout=1)
        df_dict = df.to_dict(orient='records')
        dict_all['沪深300'] = df_dict

        file = open('market_now.json','w',encoding='utf-8')
        json.dump(dict_all,fp=file,ensure_ascii=False,indent=4)

    except Exception as e:
        if say:
            print(f"-->Error: {e}")
        return False, f"Error: {e}"
    return True,f'Successfully'

'''
CREATE TABLE market(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 上证指数的代码
    market_name VARCHAR(500), -- 上证指数的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT -- 52周最低
);
'''
def market_now_save() -> tuple[bool, str]:
    database_name = 'market'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()


    file = open('market_now.json','r',encoding='utf-8')
    history_dict = json.load(fp=file)
    # print(history_dict)

    market_now_core(mycursor, market=history_dict['上证指数'], symbol='sh000001',name='上证指数')
    market_now_core(mycursor, market=history_dict['深证成指'], symbol='sz399001',name='深证成指')
    market_now_core(mycursor, market=history_dict['北证50'], symbol='bj899050',name='北证50')
    market_now_core(mycursor, market=history_dict['沪深300'], symbol='sh000300',name='沪深300')

    user_db.commit()
    return True,f'Successfully'

# a = market_now()
# print(a)
def market_now_core(mycursor, market, symbol, name):
    sql = f'''INSERT INTO market (market_code, market_name, price, high_price, low_price, price_fluctuation, amplitude, yesterday_end, today_open, trade_money, high52, low52)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    market_code = VALUES(market_code),
    market_name = VALUES(market_name),
    price = VALUES(price),
    high_price = VALUES(high_price),
    low_price = VALUES(low_price),
    price_fluctuation = VALUES(price_fluctuation),
    amplitude = VALUES(amplitude),
    yesterday_end = VALUES(yesterday_end),
    today_open = VALUES(today_open),
    trade_money = VALUES(trade_money),
    high52 = VALUES(high52),
    low52 = VALUES(low52)
    '''
    val = (symbol, name, market[6]['value'], market[7]['value'], market[11]['value'], market[3]['value'], market[5]['value'], market[17]['value'], market[24]['value'], market[15]['value'], market[1]['value'], market[20]['value'])
    mycursor.execute(sql, val)



market_now()
market_now_save()