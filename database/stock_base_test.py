import stock_base as sb
import users_base as ub
#? 测试 index = 1 根据stock_code进行数据查询股票实时数据
a = sb.stock_search_by_code()
print(a)

#? 测试 index = 2 根据stock_name进行数据查询股票实时数据
a = sb.stock_search_by_name()
print(a)

#? 测试 index = 3 获取数据库中全部的stock数据，以列表形式返回大约5000只股票数据
a = sb.stock_search_all()
print(a[0])

#? 测试 index = 5 修改用户的持仓信息
a = ub.user_register('李华','111111','are you ok?','ok!')
print(f"return: {a}")
a = sb.user_stock_modify(num=100)
print(a)

#? 测试 index = 4 查看用户的持仓信息
a = sb.user_stock_fetch()
print(a)
# 删除持仓
a = sb.user_stock_modify(num=50, decrease=1)
print(a)
a = sb.user_stock_fetch()
print(a)

#? 测试 index = 6 DONE 清除持仓记录中num = 0的股票持有记录
sb.user_stock_clear()
a = sb.user_stock_fetch()
print(a)

#? 测试 index = 7  修改用户的自选个股信息
# a = sb.user_choose_modify()
# print(a)
a = sb.user_choose_modify(decrease=1)
print(a)


#? 测试 index = 9 查看用户的自选个股信息
a = sb.user_choose_fetch()
print(a)

#? 测试 index = 8 实现用户的交易记录的存储
a = sb.user_stock_record()
print(a)

#? 测试 index = 10 查看用户的交易记录信息
a = sb.user_record_fetch()
print(a)