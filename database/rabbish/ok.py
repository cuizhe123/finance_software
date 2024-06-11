import mysql.connector

# 建立数据库连接
mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    # port="3306",  # 数据库端口号
    user="root",  # 数据库用户名
    password="Qh20040805",  # 数据库密码
    database="world"  # 数据库名称
)

# 创建游标
mycursor = mydb.cursor()

# 执行查询
mycursor.execute("SELECT * FROM city")

# 获取查询结果
result = mycursor.fetchall()

# 输出查询结果
for row in result:
    print(row)

# 关闭游标和数据库连接
mycursor.close()
mydb.close()