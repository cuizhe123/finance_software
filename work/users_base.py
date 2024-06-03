import mysql.connector
import connect

#* 此处的接口设计均为用户的基本登录、注册等操作设计

'''
    CREATE TABLE users ( -- 用户的个人信息
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(500), -- name是唯一的标识
    password VARCHAR(100),
    question VARCHAR(3000),
    answer VARCHAR(3000),
    UNIQUE(name)
    );
'''

#* DONE index=1 增：用户注册，增添用户信息在用户基础信息表中(user_trade.users)

def user_register(name:str = '', password:str = '111111', question:str = 'are you ok?', answer:str = 'ok', say:int = 0) -> tuple[bool, str]:
    '增添用户信息在用户基础信息表中，name 应为唯一的标识，录入成功返回True，若不允许将该组信息录入，返回值将是False'
    if say:
        print(f"\nCall function: user_register(name = {name}, password = {password}, question = {question}, answer = {answer})")
    # 建立数据库连接
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否已经存在该账号
    sql1 = 'SELECT * FROM users WHERE name = %s'
    mycursor.execute(sql1, (name,)) 
    
    if mycursor.fetchone() is not None:
        if say:
            print(f"-->Error: The name={name} already exists.")
        mycursor.close()
        user_db.close()
        return False, f"Error: The name={name} already exists."
    
    # 插入数据
    try:
        sql2 =  '''
                INSERT INTO users (name, password, question, answer, money)
                VALUES (%s, %s, %s, %s, %s)
                '''
        mycursor.execute(sql2, (name, password, question, answer, 0))
    except Exception as e:
    # 处理异常情况
        if say:
            print(f"-->Error: An error occurred:{e}")
        mycursor.close()
        user_db.close()
        return False, f"Error: An error occurred:{e}"
    
    # 提交事务
    user_db.commit()

    # 关闭游标和连接
    mycursor.close()
    user_db.close()
    if say:
        print(f"-->Successful: User's information:name = {name}, password = {password}, question = {question}, answer = {answer}")
    return True, f"Successfully"


#* DONE index = 2 查：用户正常登录，要根据用户名进行数据查询，查询用户的用户名是否存在，如果存在返回包括密码在内的数据(user_trade.users)

def user_search(name:str = '', password:str = '', say:int = 0) -> tuple[dict, str]:
    "根据用户名进行数据查询，查询用户的用户名是否存在，如果存在返回包括密码在内的数据在tuple[dict, str]里，若不存在则返回tuple[none, str]，dict = {'id', 'name', 'password', 'question', 'answer', 'money'}"
    if say:
        print(f"\nCall function: search_user(name = {name}, password = {password})")
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该账号
    sql1 = 'SELECT * FROM users WHERE name = %s AND password = %s'
    mycursor.execute(sql1, (name, password))
    user = mycursor.fetchone()
    ## 不存在该账号
    if user is None:
        if say:
            print(f"-->Error: The name={name} and password={password} user doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: The name={name} and password={password} user doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: User's information:{user}")
        mycursor.close()
        user_db.close()
        re_user = {'id':user[0], 'name':user[1], 'password':user[2], 'question':user[3], 'answer':user[4], 'money':user[5]}
        return re_user, f"Successfully"
    

#* DONE index = 3 改：用户登录之后，可以进行密码修改、密保问题和答案修改(user_trade.users)

def user_modify(name:str = '', old_password:str = '111111' ,new_password:str = '222222', question:str = 'are you ok?', answer:str = 'ok', say:int = 0) -> tuple[bool, str]:
    '用户登录之后，可以进行密码修改、密保问题和答案修改，修改成功会返回True，修改不成功则返回False'
    if say:
        print(f"\nCall function: user_modify(name = {name}, old_password = {old_password},\
new_password = {new_password}, question = {question}, answer = {answer})")

    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    mycursor = user_db.cursor()
    state, mess = user_search(name, old_password, say = 0)

    if state is None:
        if say:
            print(f"-->{mess}")
        mycursor.close()
        user_db.close()
        return False, f"Error: The name={name} and password={old_password} user doesn\'t exist."
    
    sql = """
            UPDATE users
            SET password = %s, question = %s, answer = %s
            WHERE name = %s
          """
            # 执行更新语句
    mycursor.execute(sql, (new_password, question, answer, name))

    # 提交事务
    user_db.commit()

    # 关闭游标和连接
    mycursor.close()
    user_db.close()
    if say:
        print(f"-->Successfully update:")
        print(f"-->init: {state}")
        print(f"-->latest: name = {name}, password = {new_password}, question = {question}, answer = {answer}")
    return True, f"Successfully"


#* DONE index = 4 删：用户登录之后，可以选择注销用户，根据 key = name删除(user_trade.users以及其他关联表)

def user_delete(name:str = '', password:str = '111111', say:int = 0) -> tuple[bool, str]:
    '用户登录之后，可以选择注销用户，根据 key = name删除(user_trade.users以及其他关联表), 删除成功则返回True, 失败则返回Fasle'
    if say:
        print(f"\nCall function: user_modify(name = {name}, password = {password})")

    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    mycursor = user_db.cursor()
    state, mess = user_search(name, password, say = 0)

    if state is None:
        if say:
            print(f"-->{mess}")
        mycursor.close()
        user_db.close()
        return False, f"Error: The name={name} and password={password} user doesn\'t exist."
    
    # 执行更新语句
    sql = "DELETE FROM users WHERE name = %s"
    mycursor.execute(sql, (name, ))

    # 提交事务
    user_db.commit()

    # 关闭游标和连接
    mycursor.close()
    user_db.close()
    if say:
        print(f"-->Successfully delete:")
        print(f"-->init: {state}")
        print(f"-->other affected table: users_stock, self_choose, trade_record")
    return True, f"Successfully"

#* DONE index = 5 查： 用户要找回密码，此时只根据用户的name则返回所有的用户基本数据

def user_search_by_name(name:str = '', say:int = 0) -> tuple[dict, str]:
    "用户要找回密码，根据用户名进行数据查询，查询用户的用户名是否存在，如果存在返回包括密码在内的数据在tuple[dict, str]里，若不存在则返回tuple[none, str]，dict = {'id', 'name', 'password', 'question', 'answer', 'money'}"
    if say:
        print(f"\nCall function: search_user_by_name(name = {name})")
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return None, f"Error: The database \'{database_name}\' doesn\'t exist."
    # 创建游标
    mycursor = user_db.cursor()

    # 查看是否存在该账号
    sql1 = 'SELECT * FROM users WHERE name = %s'
    mycursor.execute(sql1, (name, ))
    user = mycursor.fetchone()
    ## 不存在该账号
    if user is None:
        if say:
            print(f"-->Error: The name={name} user doesn\'t exist.")
        mycursor.close()
        user_db.close()
        return None, f"Error: The name={name} user doesn\'t exist."
    ## 存在该账号
    else:
        if say:
            print(f"-->Successful: User's information:{user}")
        mycursor.close()
        user_db.close()

        re_user = {'id':user[0], 'name':user[1], 'password':user[2], 'question':user[3], 'answer':user[4], 'money':user[5]}
        return re_user, f"Successfully"

#* DONE index = 6: 改 实现用户的充值 账户的钱数 += money

def user_money_modify(name:str = '', password:str = '111111', money:float = 0, decrease:int = 0,say:int = 0) -> tuple[bool, str]:
    '用户登录之后，可以实现用户的充值，账户的钱数 += money，修改成功会返回True，修改不成功则返回False'
    database_name = 'user_trade'
    user_db = connect.connect_db(database_name)

    if user_db is None:
        if say:
            print(f"-->Error: The database \'{database_name}\' doesn\'t exist.")
        return False, f"Error: The database \'{database_name}\' doesn\'t exist."
    
    mycursor = user_db.cursor()
    state, mess = user_search(name, password, say = 0)

    if state is None:
        if say:
            print(f"-->{mess}")
        mycursor.close()
        user_db.close()
        return False, f"Error: The name={name} and password={password} user doesn\'t exist."
    
    # state 的类型是dict
    
    sql = """
            UPDATE users
            SET money = %s
            WHERE name = %s
          """
            # 执行更新语句
    if decrease == 0:
        mycursor.execute(sql, (state['money'] + money, name))
    else:
        mycursor.execute(sql, (state['money'] - money, name))
        
    # 提交事务
    user_db.commit()

    # 关闭游标和连接
    mycursor.close()
    user_db.close()
    return True, f"Successfully"