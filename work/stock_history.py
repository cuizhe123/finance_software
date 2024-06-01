import akshare as ak
import pandas as pd
import json
import sys
from datetime import datetime
import mysql.connector
import connect
import time

#* DONE 1 获取symbol的历史数据并存入文件
def stock_history_fetch(symbol:str = "600519", period="daily" ,start_date:str = "20220101", end_date:str = "20240531",say:int = 0) -> tuple[bool,str]:
    "获取symbol的历史数据并存入文件"
    try:
        # version 1: symbol需要传入市场标识，爬取的腾讯证券的数据，但因为爬取一个股票的数据需要1s，故暂时被舍弃
        # stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol=symbol, start_date=start_date, end_date=end_date, adjust="")
        # version 2:: symbol 不需要市场标识，爬取的东方财富的数据，速度较快，目前使用这个版本，注意目前的数据库结构也是version 2相适应的
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date, adjust="")

    except Exception as e:
        if say:
            print(f"-->Error: {e}")
        return False,f"Error: {e}"
    
    df = pd.DataFrame(stock_zh_a_hist_df)

    # 格式化日期列为指定格式
    # df['date'] = pd.to_datetime(df['date'])
    # df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    if say:
        print(df)

    # 将获取的数据存入json文件中
    if df.empty:
        return False,f"Error: dataframe is empty"
    
    df['日期'] = pd.to_datetime(df['日期'])
    df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

    df.to_json('stock_history.json',orient='records', force_ascii=False, indent=4)
    return True,f"Successfully"


#* DONE 2 将sh,sz的股票历史数据存入数据库
def stock_history_save(say:int = 0)->tuple[bool, str]:
    '将sh,sz的股票历史数据存入数据库'
    database_name = 'stock_history'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    # 创建游标
    mycursor = user_db.cursor()

    # 获取今天的日期
    today = str(datetime.today().date())
    today = today.replace("-", "")

    sh_file = open('stock_sh_now.json','r',encoding='utf-8')
    sh_flag = 'sh'
    
    sz_file = open('stock_sz_now.json','r',encoding='utf-8')
    sz_flag = 'sz'

    history_core(user_db ,mycursor, sh_file, sh_flag, period="daily", start_date='20220101', end_date=today, say=1)
    if say:
        print('sh_file_history is ok')

    history_core(user_db ,mycursor, sz_file, sz_flag, period="daily", start_date='20220101', end_date=today, say=1)
    if say:
        print('sz_file_history is ok')

    return True,f'Successfully'

def history_core(user_db ,mycursor, file, flag:str = 'sh', period="daily", start_date='20220101', end_date='20240531',say:int = 0) ->bool:
    '将sh,sz的股票历史数据存入数据库的核心操作'
    data_list = json.load(file)
    count = 0
    for data in data_list:
        # time.sleep(0.1)
        count += 1
        symbol = data['代码']
        zh_symbol = flag + data['代码']
        name = data['名称']
        if say:
            print(count)
        # print(symbol)

        tf,mess = stock_history_fetch(symbol=symbol,period=period, start_date=start_date, end_date=end_date)
        if tf == False:
            if say:
                print(f"-->{mess}")
            continue
        if tf == True:
            history_file = open('stock_history.json','r',encoding='utf-8')
            history_list = json.load(history_file)

            sql1 = f"""
            CREATE TABLE IF NOT EXISTS {zh_symbol}(
            id INT PRIMARY KEY AUTO_INCREMENT,
            time VARCHAR(100), 
            stock_id VARCHAR(500), 
            stock_name VARCHAR(500),
            exchange VARCHAR(10), 
            open_price FLOAT, 
            close_price FLOAT,
            high_price FLOAT,
            low_price FLOAT,
            trade_num FLOAT,
            trade_money FLOAT, 
            amplitude FLOAT,
            up_down FLOAT, 
            price_range FLOAT,
            turnover_ratio FLOAT,
            UNIQUE(time)
            )"""
            mycursor.execute(sql1)
            # break
            sql2 = f'''INSERT INTO {zh_symbol} (time, stock_id, stock_name, exchange, open_price, close_price,
              high_price, low_price, trade_num, trade_money, amplitude, up_down, price_range, turnover_ratio)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        time = VALUES(time),
                        stock_id = VALUES(stock_id),
                        stock_name = VALUES(stock_name),
                        exchange = VALUES(exchange),
                        open_price = VALUES(open_price),
                        close_price = VALUES(close_price),
                        high_price = VALUES(high_price),
                        low_price = VALUES(low_price),
                        trade_num = VALUES(trade_num),
                        trade_money = VALUES(trade_money),
                        amplitude = VALUES(amplitude),
                        up_down = VALUES(up_down),
                        price_range = VALUES(price_range),
                        turnover_ratio = VALUES(turnover_ratio)
                        '''
            for history_data in history_list:
                val = (history_data['日期'], symbol, name, flag, history_data['开盘'], \
                       history_data['收盘'], history_data['最高'], history_data['最低'], history_data['成交量'], history_data['成交额'],\
                       history_data['振幅'], history_data['涨跌幅'], history_data['涨跌额'], history_data['换手率'])
                mycursor.execute(sql2, val)
            # break
    user_db.commit()
    return True

a = stock_history_save(1)