import mysql.connector
import connect

#* DONE index = 1 根据market_code进行数据查询股票实时数据
def market_search_by_code(market_code:str = 'sh000001', say:int = 0) -> tuple[tuple, str]:
    '根据market_code（必须有市场标识）进行大盘指数数据查询，market_code = sh000001，查询该大盘指数实时数据，如果存在返回该指数的数据tuple[tuple, str]里，若不存在则返回tuple[none, str]'
    database_name = 'market'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM market WHERE market_code = %s'
    mycursor.execute(sql1, (market_code, ))
    stock = mycursor.fetchone()
    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The market_code={market_code} stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: -->Error: The market_code={market_code} stock doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: Stock's information:{stock}")
        mycursor.close()
        user_db.close()
        return stock, f"Successfully"


#* DONE index = 2 根据market_name进行数据查询股票实时数据
def market_search_by_name(market_name:str = '上证指数', say:int = 0) -> tuple[tuple, str]:
    '根据market_name（上证指数、深证成指、北证50、沪深300）进行数据查询，查询该大盘指数数据，如果存在返回该指数的实时数据tuple[tuple, str]里，若不存在则返回tuple[none, str]'
    database_name = 'market'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM market WHERE market_name = %s'
    mycursor.execute(sql1, (market_name, ))
    stock = mycursor.fetchone()
    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The market_name={market_name} stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: -->Error: The market_name={market_name} stock doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: Market's information:{stock}")
        mycursor.close()
        user_db.close()
        return stock, f"Successfully"


#* DONE index = 3 获取数据库中全部的market数据，以列表形式返回4个大盘数据
def market_search_all(say:int = 0) -> list:
    '获取数据库中全部的market的实时数据，以列表形式返回4个大盘数据'
    database_name = 'market'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM market'
    mycursor.execute(sql1)
    stock_all = mycursor.fetchall()
    return stock_all

a = market_search_by_code()
print(a)
a = market_search_by_name()
print(a)
a = market_search_all()
print(a)