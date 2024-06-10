import mysql.connector
import connect
import json


#* DONE 1 更新数据库当中的上海、深圳证券交易所的股票实时数据
def update_stock_sh_now(say:int = 0) -> tuple[bool, str]:
    '用于更新上海证券交易所 和 深圳证券交易所 股票的实时数据'
    
    # 创建数据库连接
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    # 创建游标
    mycursor = user_db.cursor()

    # 字典数据
    
    sh_file = open('stock_sh_now.json','r',encoding='utf-8')
    sh_flag = 'sh'

    sz_file = open('stock_sz_now.json','r',encoding='utf-8')
    sz_flag = 'sz'

    all_rowcount = 0

    all_rowcount += update_core(user_db, mycursor, sh_file, sh_flag)
    if say:
        print("sh 上交所数据处理完毕")
    all_rowcount += update_core(user_db, mycursor, sz_file, sz_flag)
    if say:
        print("sz 深交所数据处理完毕")
    
    mycursor.close()
    user_db.close()

    if all_rowcount == 0:
        return False,f"Error: nothing had been updated"
    return True,f"Successfully"    




def update_core(user_db ,mycursor, file, flag:str = 'sh',say:int = 0) -> int:
    '核心代码：用于更新上海证券交易所 和 深圳证券交易所 股票的实时数据'
    # file = open('stock_sh_now.json','r',encoding='utf-8')
    data_list = json.load(file) # it is a list [{}, {}, {}]
    all_rowcount = 0

    for data in data_list:
        if data['最新价'] is None:
            continue
        sql = """INSERT INTO current_stock (stock_code, stock_name, exchange, price, up_down,
                price_range, trade_num, trade_money, amplitude, high_price, low_price, today_open, 
                yester_price, quantity_ratio, turnover_ratio, pe_ratio, pb_ratio, total_value, 
                circle_value, increase_ratio, five_up_down, zdf60, zdfnc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                exchange = VALUES(exchange),
                price = VALUES(price),
                up_down = VALUES(up_down),
                price_range = VALUES(price_range),
                trade_num = VALUES(trade_num),
                trade_money = VALUES(trade_money),
                amplitude = VALUES(amplitude),
                high_price = VALUES(high_price),
                low_price = VALUES(low_price),
                today_open = VALUES(today_open),
                yester_price = VALUES(yester_price),
                quantity_ratio = VALUES(quantity_ratio),
                turnover_ratio = VALUES(turnover_ratio),
                pe_ratio = VALUES(pe_ratio),
                pb_ratio = VALUES(pb_ratio),
                total_value = VALUES(total_value),
                circle_value = VALUES(circle_value),
                increase_ratio = VALUES(increase_ratio),
                five_up_down = VALUES(five_up_down),
                zdf60 = VALUES(zdf60),
                zdfnc = VALUES(zdfnc)
            """
        # stock_code, stock_name, exchange, price, up_down,
        #  price_range, trade_num, trade_money, amplitude, high_price, low_price, today_open, 
        #  yester_price, quantity_ratio, turnover_ratio, pe_ratio, pb_ratio, total_value, 
        #  circle_value, increase_ratio, five_up_down, zdf60, zdfnc
        # 定义要插入的值
        val = (data['代码'], data['名称'], flag, data['最新价'], data['涨跌幅'], data['涨跌额'], data['成交量'],\
            data['成交额'], data['振幅'], data['最高'], data['最低'], data['今开'], data['昨收'], data['量比'],\
            data['换手率'], data['市盈率-动态'], data['市净率'], data['总市值'], data['流通市值'], data['涨速'],\
            data['5分钟涨跌'], data['60日涨跌幅'], data['年初至今涨跌幅'])
        # 执行 SQL 语句
        mycursor.execute(sql, val)
        # mycursor.executemany(sql, val)
        
        all_rowcount += mycursor.rowcount
        if say:
            print(mycursor.rowcount, flag, "记录插入/更新成功。")

    # 提交到数据库执行 
    '''
    将多个插入或更新操作包装在一个事务中，确保它们要么全部成功，要么全部失败。
    这样可以减少事务提交的次数，提高效率，并且在发生错误时可以回滚事务。
    '''
    user_db.commit()
    return all_rowcount
    
a = update_stock_sh_now(1)
print(a)


