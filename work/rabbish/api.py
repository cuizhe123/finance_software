import requests
import json
import sys
import time
'''
将大量数据存入数据库时，通常会先使用文本文件来读取数据。
这是因为文本文件是一种常见的数据交换格式，可以方便地被各种数据处理工具读取和写入。
'''

# TODO 将my_stock_code.json的股票代码和公司名称读取，便于后期迭代查询股票数据
# TODO 针对每一只股票，通过api读取数据，并存入数据库

my_stock_code_path = 'D:\A课程文件夹\大二下课程文件\work\my_stock_list.json'
stock_base = json.load(open(my_stock_code_path,'r',encoding='utf-8')) # [{},{},{}]

file = open('my_stock_data.json',mode='w',encoding='utf-8')
stock_data = []
licence = '5e90797dd137345fd1'
licence = 'e13457187a461bcf07'

data_num = int(len(stock_base)/4)
# print(len(stock_base)/4)
# sys.exit()
# data_num = 2
for i in range(0, data_num):
    if (i+1) % 5 == 0:
        time.sleep(1)
    print(i)
    it = stock_base[i]
    stock_code = it['dm']
    stock_name = it['mc']
    exchange = it['jys']

    url = f"http://api.mairui.club/hsrl/ssjy/{stock_code}/{licence}"
    r = requests.get(url)
    data2 = r.json()

    print(type(it))
    print(it)
    print(type(data2))
    print(data2)
    
    data = {**it, **data2}
    stock_data.append(data)

file.write(json.dumps(stock_data, indent=4,ensure_ascii=False))




'''
import mysql.connector
from mysql.connector import Error

def modify_or_insert(name: str, new_value: str):
    try:
        # 连接到MySQL数据库
        connection = mysql.connector.connect(user='user',
                                             password='password',
                                             host='localhost',
                                             database='mydatabase')
        if connection.is_connected():
            # 创建游标对象
            cursor = connection.cursor()
            # 编写SQL更新语句
            sql = """
            UPDATE users
            SET record = %s
            WHERE name = %s
            """
            # 执行更新语句
            cursor.execute(sql, (new_value, name))
            # 获取受影响的行数
            rows_affected = cursor.rowcount
            # 如果受影响的行数大于0，说明找到了匹配的行并成功更新
            if rows_affected > 0:
                print(f"User '{name}' updated successfully.")
            else:
                # 如果没有找到匹配的行，则执行INSERT语句
                sql = """
                INSERT INTO users (name, record)
                VALUES (%s, %s)
                """
                cursor.execute(sql, (name, new_value))
                print(f"User '{name}' created successfully.")
            # 提交事务
            connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        # 关闭游标和连接
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# 调用函数修改或创建用户
modify_or_insert('ok', 'new_record_value')
'''