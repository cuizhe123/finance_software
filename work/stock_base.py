import mysql.connector
import connect

#* 根据stock_code进行数据查询股票实时数据
def stock_search_by_code(stock_code:str = 'sh600087', say:int = 0) -> tuple[tuple, str]:
    '根据stock_code进行数据查询，stock_code = sh600087 或者600087均可，查询该股票实时数据，如果存在返回该股票的数据tuple[tuple, str]里，若不存在则返回tuple[none, str]'
    if len(stock_code) > 6:
        stock_code = stock_code[2:]

    if say:
        print(f"\nCall function: stock_search_by_code(stock_code = {stock_code})")
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock WHERE stock_code = %s'
    mycursor.execute(sql1, (stock_code, ))
    stock = mycursor.fetchone()
    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The stock_code={stock_code} stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: -->Error: The stock_code={stock_code} stock doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: Stock's information:{stock}")
        mycursor.close()
        user_db.close()
        return stock, f"Successfully"

#* 根据stock_name进行数据查询股票实时数据
def stock_search_by_name(stock_name:str = '贵州茅台', say:int = 0) -> tuple[tuple, str]:
    '根据stock_name进行数据查询，查询该股票数据，如果存在返回该股票的实时数据tuple[tuple, str]里，若不存在则返回tuple[none, str]'
    if say:
        print(f"\nCall function: stock_search_by_code(stock_name = {stock_name})")
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock WHERE stock_name = %s'
    mycursor.execute(sql1, (stock_name, ))
    stock = mycursor.fetchone()
    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The stock_name={stock_name} stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: -->Error: The stock_name={stock_name} stock doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: Stock's information:{stock}")
        mycursor.close()
        user_db.close()
        return stock, f"Successfully"

#* 获取数据库中全部的stock数据，以列表形式返回大约5000只股票数据
def stock_search_all(say:int = 0) -> list:
    '获取数据库中全部的stock的实时数据，以列表形式返回大约5000只股票数据'
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock'
    mycursor.execute(sql1)
    stock_all = mycursor.fetchall()
    return stock_all

# a = stock_search_by_code('sh600519')
# print(a)

# b = stock_search_by_name('贵州茅台')
# print(b)

# c = stock_search_all()
# print(len(c))

#* 修改用户的持仓信息
def user_stock_modify():
    '修改用户的持仓信息，只需要用户名即可，股票代码，股票名称，交易数量，持有减少还是增加'

    # try:
    #     # 尝试执行插入操作
    #     affected_rows = mycursor.execute(sql_insert, (用户名, 股票代码, stock_name_to_insert, 持有数量))
    #     # 如果执行成功，则提交事务
    #     mydb.commit()
    #     print(f"成功插入记录，受影响的行数：{affected_rows}")
    # except mysql.connector.Error as err:
    #     # 如果发生错误，打印错误信息
    #     print(f"插入记录时发生错误：{err}")
    #     # 回滚事务
    #     mydb.rollback()
    
    pass

