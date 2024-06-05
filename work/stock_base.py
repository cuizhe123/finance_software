import mysql.connector
import connect

#* DONE index = 1 根据stock_code进行数据查询股票实时数据
def stock_search_by_code(stock_code:str = 'sh600089', say:int = 0) -> tuple[dict, str]:
    "根据stock_code进行数据查询，stock_code = sh600089 或者600089均可，查询该股票实时数据，如果存在返回该股票的数据tuple[dict, str]里，若不存在则返回tuple[none, str]，dict = {'id', 'stock_code', 'stock_name', 'exchange', 'price', 'up_down', 'price_range', 'trade_num', 'trade_money', 'amplitude', 'high_price', 'low_price', 'today_open', 'yester_price', 'quantity_ratio', 'turnover_ratio', 'pe_ratio', 'pb_ratio', 'total_value', 'circle_value', 'increase_ratio', 'five_up_down', 'zdf60', 'dfnc'}"
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
        re_stock = {'id':stock[0], 'stock_code':stock[1], 'stock_name':stock[2], 'exchange':stock[3], 'price':stock[4], 'up_down':stock[5], 'price_range':stock[6], 'trade_num':stock[7], 'trade_money':stock[8], 'amplitude':stock[9], 'high_price':stock[10], 'low_price':stock[11], 'today_open':stock[12], 'yester_price':stock[13], 'quantity_ratio':stock[14], 'turnover_ratio':stock[15], 'pe_ratio':stock[16], 'pb_ratio':stock[17], 'total_value':stock[18], 'circle_value':stock[19], 'increase_ratio':stock[20], 'five_up_down':stock[21], 'zdf60':stock[22], 'dfnc':stock[23]}
        return re_stock, f"Successfully"


#* DONE index = 2 根据stock_name进行数据查询股票实时数据
def stock_search_by_name(stock_name:str = '贵州茅台', say:int = 0) -> tuple[dict, str]:
    "根据stock_name进行数据查询，查询该股票数据，如果存在返回该股票的实时数据tuple[dict, str]里，若不存在则返回tuple[none, str],dict = {'id', 'stock_code', 'stock_name', 'exchange', 'price', 'up_down', 'price_range', 'trade_num', 'trade_money', 'amplitude', 'high_price', 'low_price', 'today_open', 'yester_price', 'quantity_ratio', 'turnover_ratio', 'pe_ratio', 'pb_ratio', 'total_value', 'circle_value', 'increase_ratio', 'five_up_down', 'zdf60', 'dfnc'}"
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
        re_stock = {'id':stock[0], 'stock_code':stock[1], 'stock_name':stock[2], 'exchange':stock[3], 'price':stock[4], 'up_down':stock[5], 'price_range':stock[6], 'trade_num':stock[7], 'trade_money':stock[8], 'amplitude':stock[9], 'high_price':stock[10], 'low_price':stock[11], 'today_open':stock[12], 'yester_price':stock[13], 'quantity_ratio':stock[14], 'turnover_ratio':stock[15], 'pe_ratio':stock[16], 'pb_ratio':stock[17], 'total_value':stock[18], 'circle_value':stock[19], 'increase_ratio':stock[20], 'five_up_down':stock[21], 'zdf60':stock[22], 'dfnc':stock[23]}
        return re_stock, f"Successfully"


#* DONE index = 3 获取数据库中全部的stock数据，以列表形式返回大约5000只股票数据
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

#* DONE index = 4 查看用户的持仓信息
def user_stock_fetch(name:str = '',say:int = 0) -> tuple[list[dict], str]:
    "查看用户的持仓信息,dict = {'id', 'name', 'stock_code', 'stock_name', 'num'}"
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该用户的持仓信息
    sql1 = 'SELECT * FROM users_stock WHERE name = %s'
    mycursor.execute(sql1, (name, ))
    stock = mycursor.fetchall()
    if stock == []:
        mycursor.close()
        user_db.close()
        return None, f"Error: the user don\'t have any stock"
    stock_list = []
    for one in stock:
        dict = {'id': one[0], 'name': one[1], 'stock_code': one[2], 'stock_name': one[3], 'num': one[4]}
        stock_list.append(dict)
    return stock_list,f'Successfully'


#* DONE index = 5 修改用户的持仓信息
def user_stock_modify(name:str = '', stock_code:str = '', stock_name:str = '', num:int = 0, decrease:int = 0,say:int = 0) -> tuple[bool, str]:
    '修改用户的持仓信息，只需要用户名，股票代码，股票名称，交易数量，decrease默认为0，若置位为1则是实现该股票的持有减少'
    if len(stock_code) > 6:
        stock_code = stock_code[2:]

    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock WHERE stock_code = %s AND stock_name = %s'
    mycursor.execute(sql1, (stock_code, stock_name))
    stock = mycursor.fetchone()
    sql2 = 'SELECT * FROM users WHERE name = %s'
    mycursor.execute(sql2, (name, ))
    user = mycursor.fetchone()
    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return False, f"Error: The stock doesn\'t exist."
    ## 存在该股票
    ## 所有的用户中不存在该用户
    if user is None:
        mycursor.close()
        user_db.close()
        return False, f"Error: The user doesn\'t exist."
    
    ## 既存在用户又存在股票
    sql3 = 'SELECT * FROM users_stock WHERE name = %s AND stock_code = %s AND stock_name = %s'
    mycursor.execute(sql3, (name, stock_code, stock_name))
    row = mycursor.fetchone()
    if row is None:
        sql4 = 'INSERT INTO users_stock (name, stock_code, stock_name, num) VALUES (%s, %s, %s, %s)'
        mycursor.execute(sql4, (name, stock_code, stock_name, num))
    else:
        sql5 = '''UPDATE users_stock 
                SET num = %s
                WHERE name = %s AND stock_code = %s AND stock_name = %s
                '''
        if decrease:
            mycursor.execute(sql5, (row[4] - num, name, stock_code, stock_name))
        else:
            mycursor.execute(sql5, (row[4] + num, name, stock_code, stock_name))
    user_db.commit()
    mycursor.close()
    user_db.close()
    return True, f"Successfully"


#* DONE index = 6 DONE 清除持仓记录中num = 0的股票持有记录
def user_stock_clear() -> None:
    '清除持仓记录中num = 0的股票持有记录'
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)
    # 创建游标
    mycursor = user_db.cursor()
    sql = 'DELETE FROM users_stock WHERE num = 0'
    mycursor.execute(sql)
    user_db.commit()
    mycursor.close()
    user_db.close()


#* DONE index = 7  修改用户的自选个股信息
def user_choose_modify(name:str = '', stock_code:str = '', stock_name:str = '', decrease:int = 0,say:int = 0) -> tuple[bool, str]:
    '修改用户的自选个股信息，只需要用户名，股票代码，股票名称decrease默认为0即收藏股票，若置位为1则是实现该股票收藏的删除'
    if len(stock_code) > 6:
        stock_code = stock_code[2:]

    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock WHERE stock_code = %s AND stock_name = %s'
    mycursor.execute(sql1, (stock_code, stock_name))
    stock = mycursor.fetchone()
    sql2 = 'SELECT * FROM users WHERE name = %s'
    mycursor.execute(sql2, (name, ))
    user = mycursor.fetchone()

    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return False, f"Error: The stock doesn\'t exist."
    
    ## 存在该股票
    ## 所有的用户中不存在该用户
    if user is None:
        mycursor.close()
        user_db.close()
        return False, f"Error:The user doesn\'t exist."
    
    ## 既存在用户又存在股票
    sql3 = 'SELECT * FROM self_choose WHERE name = %s AND stock_code = %s AND stock_name = %s'
    mycursor.execute(sql3, (name, stock_code, stock_name))
    row = mycursor.fetchone()
    if row is None:
        # 不存在
        if decrease:
            # 删除收藏
            return False, f"Error: This stock is not included in the self selected stocks"
        else:
            # 进行收藏
            sql4 = 'INSERT INTO self_choose (name, stock_code, stock_name) VALUES (%s, %s, %s)'
            mycursor.execute(sql4, (name, stock_code, stock_name))
    else:
        # 存在
        sql5 = 'DELETE FROM self_choose WHERE name = %s AND stock_code = %s AND stock_name = %s'
        if decrease:
            mycursor.execute(sql5, (name, stock_code, stock_name))
        else:
            return False, f"Error: This stock has been included in the self selected stocks"
    user_db.commit()
    mycursor.close()
    user_db.close()
    return True, f"Successfully"


#* DONE index = 8 实现用户的交易记录的存储
def user_stock_record(name:str = '', stock_code:str = '', stock_name:str = '', num:int = 0, price:float = 0.0, decrease:bool = 0, say:int = 0) ->tuple[bool, str]:
    '实现用户的交易记录的存储，注意num必须要非负数，decrease默认是0，表示买入，decrease如果是1则是卖出'
    if len(stock_code) > 6:
        stock_code = stock_code[2:]
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该股票
    sql1 = 'SELECT * FROM current_stock WHERE stock_code = %s AND stock_name = %s'
    mycursor.execute(sql1, (stock_code, stock_name))
    stock = mycursor.fetchone()
    sql2 = 'SELECT * FROM users WHERE name = %s'
    mycursor.execute(sql2, (name, ))
    user = mycursor.fetchone()

    ## 不存在该股票
    if stock is None:
        if say:
            print(f"-->Error: The stock doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return False, f"Error: The stock doesn\'t exist."
    
    ## 存在该股票
    ## 所有的用户中不存在该用户
    if user is None:
        mycursor.close()
        user_db.close()
        return False, f"Error:The user doesn\'t exist."
    
    ## 既存在用户又存在股票
    
    sql3 = 'INSERT INTO trade_record (name, stock_code, stock_name, num, price) VALUES (%s, %s, %s, %s, %s)'
    # 卖出
    if decrease:
        mycursor.execute(sql3, (name, stock_code, stock_name, -1 * num, price))
    # 买入
    else:
        mycursor.execute(sql3, (name, stock_code, stock_name,num, price))
    user_db.commit()
    mycursor.close()
    user_db.close()
    return True, f"Successfully"
    

#* DONE index = 9 查看用户的自选个股信息
def user_choose_fetch(name:str = '',say:int = 0) -> tuple[list[dict], str]:
    "查看用户的自选个股信息,dict = {'id', 'name', 'stock_code', 'stock_name'}"
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该用户的持仓信息
    sql1 = 'SELECT * FROM users_stock WHERE name = %s'
    mycursor.execute(sql1, (name, ))
    stock = mycursor.fetchall()
    if stock == []:
        mycursor.close()
        user_db.close()
        return None, f"Error: the user don\'t have any stock"
    stock_list = []
    for one in stock:
        dict = {'id': one[0], 'name': one[1], 'stock_code': one[2], 'stock_name': one[3]}
        stock_list.append(dict)
    return stock_list,f'Successfully'


#* DONE index = 9 查看用户的交易记录信息
def user_record_fetch(name:str = '',say:int = 0) -> tuple[list[dict], str]:
    "查看用户的自选个股信息,dict = {'id', 'name', 'stock_code', 'stock_name', 'num', 'price'}, num 是正数代表是买入，负数代表卖出"
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该用户的持仓信息
    sql1 = 'SELECT * FROM trade_record WHERE name = %s'
    mycursor.execute(sql1, (name, ))
    stock = mycursor.fetchall()
    if stock == []:
        mycursor.close()
        user_db.close()
        return None, f"Error: the user don\'t have any stock"
    stock_list = []
    for one in stock:
        dict = {'id': one[0], 'name': one[1], 'stock_code': one[2], 'stock_name': one[3], 'num': one[4], 'price':one[5]}
        stock_list.append(dict)
    return stock_list,f'Successfully'