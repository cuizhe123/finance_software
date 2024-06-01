import users_base as ub

#? 测试用户信息录入
a = ub.user_register('屈航','111111','are you ok?','ok!')
print(f"return: {a}")

#? 测试用户信息读取
a =  ub.user_search('屈航', '111111')
print(f"return: {a}")

# ? 测试用户信息修改
a = ub.user_modify('屈航', '111111', '222222','あなたは私が好きですか','私はあなたが好きです')
print(f"return: {a}")

#? 测试用户账号的级联删除
a = ub.user_delete('屈航', '222222')
print(a)

