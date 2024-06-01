import mysql.connector

def connect_db(database:str = "" , host:str = "127.0.0.1",  port:str = "3306", user:str = "root",  password:str = "Qh20040805"):
    try:
        user_db = mysql.connector.connect(
            host=host,  # 数据库主机地址
            port=port,  # 数据库端口号
            user=user,  # 数据库用户名
            password=password,  # 数据库密码
            database=database  # 数据库名称
        )
    except Exception as e:
        print("An error occurred:", e)
        return None
    return user_db
