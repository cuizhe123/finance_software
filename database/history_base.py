import akshare as ak
import connect

'''
股票历史数据结构
CREATE TABLE sh600519(
    id INT PRIMARY KEY auto_increment,
    time VARCHAR(100), -- 交易时间
    stock_code VARCHAR(500), -- 股票的代码
    stock_name VARCHAR(500), -- 股票的名称
    exchange VARCHAR(10), -- 交易所标识
    open_price FLOAT, -- 开盘价（元）
    close_price FLOAT, -- 收盘价（元）
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    trade_num FLOAT, -- 成交量（手）
    trade_money FLOAT, -- 成交额（元）
    amplitude FLOAT, -- 振幅（%）
    up_down FLOAT, -- 涨跌幅（%）
    price_range FLOAT, -- 涨跌额（元）
    turnover_ratio FLOAT, -- 换手率
    UNIQUE(time)
);
'''
'''
大盘指数历史数据结构
CREATE TABLE sh000001(
    id INT PRIMARY KEY auto_increment,
    time VARCHAR(100), -- 交易时间
    market_code VARCHAR(500), -- 指数的代码
    market_name VARCHAR(500), -- 指数的名称
    exchange VARCHAR(10), -- 交易所标识
    open_price FLOAT, -- 开盘价（元）
    close_price FLOAT, -- 收盘价（元）
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    trade_num FLOAT, -- 成交量（手）
    trade_money FLOAT, -- 成交额（元）
    amplitude FLOAT, -- 振幅（%）
    up_down FLOAT, -- 涨跌幅（%）
    price_range FLOAT, -- 涨跌额（元）
    turnover_ratio FLOAT, -- 换手率
    UNIQUE(time)
);
'''
#* DONE index = 1 获取股票的历史数据
def history_stock_search(stock_code:str = 'sh600089', say:int = 0)->tuple[list[dict], str]:
    "获取股票的历史数据，传入参数股票代码stock_code，例如sh600089或者600089，返回历史数据,dict = {'id', 'time', 'market_code', 'market_name', 'exchange', 'open_price', 'close_price', 'high_price', 'low_price', 'trade_num', 'trade_money', 'amplitude', 'up_down', 'price_range', 'turnover_ratio'}"
    database_name = 'stock_history'
    user_db = connect.connect_db(database_name)
    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    if len(stock_code) == 6:
        stock_code_2 = 'sh'+stock_code
        sql1 = f'SELECT * FROM {stock_code_2}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            return stock,f'Successfully'
        
        stock_code_2 = 'sz'+stock_code
        sql1 = f'SELECT * FROM {stock_code_2}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            return stock,f'Successfully'
        
    else:
        sql1 = f'SELECT * FROM {stock_code}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            re_stock = []
            for one in stock:
                dict = {'id':one[0], 'time':one[1], 'market_code':one[2], 'market_name':one[3], 'exchange':one[4], 'open_price':one[5], 'close_price':one[6], 'high_price':one[7], 'low_price':one[8], 'trade_num':one[9], 'trade_money':one[10], 'amplitude':one[11], 'up_down':one[12], 'price_range':one[13], 'turnover_ratio':one[14]}
                re_stock.append(dict)
            return re_stock,f'Successfully'
        return None, f"This stock's history data doesn\'t exist"


# a,b = history_stock_search('600088')
# if a is not None:
#     print(a[0])
# else:
#     print(b)

#* DONE index = 2 获取大盘指数的历史数据
def history_market_search(market_code:str = 'sh000001', say:int = 0)->tuple[list[dict], str]:
    "获取大盘指数的历史数据，传入大盘指数代码market_code，sh000001、sz399001、bj899050、sh000300，必须有市场标识如sh、sz、bj，返回历史数据,dict = {'id', 'time', 'market_code', 'market_name', 'exchange', 'open_price', 'close_price', 'high_price', 'low_price', 'trade_num', 'trade_money', 'amplitude', 'up_down', 'price_range', 'turnover_ratio'}"
    database_name = 'market_history'
    user_db = connect.connect_db(database_name)
    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = f'SELECT * FROM {market_code}'
    try:
        mycursor.execute(sql1)
    except Exception as e:
        return None, f"This market's history data doesn\'t exist"
    
    stock = mycursor.fetchall()
    if stock != []:
        re_stock = []
        for one in stock:
            dict = {'id':one[0], 'time':one[1], 'market_code':one[2], 'market_name':one[3], 'exchange':one[4], 'open_price':one[5], 'close_price':one[6], 'high_price':one[7], 'low_price':one[8], 'trade_num':one[9], 'trade_money':one[10], 'amplitude':one[11], 'up_down':one[12], 'price_range':one[13], 'turnover_ratio':one[14]}
            re_stock.append(dict)
        return re_stock,f'Successfully'
    return None, f"This market's history data doesn\'t exist"


a,b = history_market_search('sh000001')
if a is not None:
    print(a[0])
else:
    print(b)



a, b = history_stock_search('sh600089')
if a is not None:
    print(a[0])
else:
    print(b)