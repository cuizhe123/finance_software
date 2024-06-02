import akshare as ak
import connect


def history_stock_search(stock_id:str = '', say:int = 0)->tuple[list, str]:
    '获取股票的历史数据，传入参数股票代码stock_id，例如sh600087或者600087，返回历史数据'
    database_name = 'stock_history'
    user_db = connect.connect_db(database_name)
    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    if len(stock_id) == 6:
        stock_id_2 = 'sh'+stock_id
        sql1 = f'SELECT * FROM {stock_id_2}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            return stock,f'Successfully'
        
        stock_id_2 = 'sz'+stock_id
        sql1 = f'SELECT * FROM {stock_id_2}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            return stock,f'Successfully'
        
    else:
        sql1 = f'SELECT * FROM {stock_id}'
        try:
            mycursor.execute(sql1)
        except Exception as e:
            return None, f"This stock's history data doesn\'t exist"
        
        stock = mycursor.fetchall()
        if stock != []:
            return stock,f'Successfully'
        return None, f"This stock's history data doesn\'t exist"


# a,b = history_stock_search('600088')
# if a is not None:
#     print(a[0])
# else:
#     print(b)


def history_market_search(market_code:str = 'sh000001', say:int = 0)->tuple[list, str]:
    '获取大盘指数的历史数据，传入大盘指数代码market_code，必须有市场标识如sh、sz、bj，返回历史数据'
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
        return stock,f'Successfully'
    return None, f"This market's history data doesn\'t exist"


# a,b = history_market_search('sh000001')
# if a is not None:
#     print(a[0])
# else:
#     print(b)