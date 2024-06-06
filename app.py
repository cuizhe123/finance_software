from flask import Flask,request,jsonify
from users_base import user_register,  user_search, user_modify, user_money_modify
from stock_base import user_stock_fetch, stock_search_by_code,user_record_fetch


app = Flask(__name__)

#注册界面，收到传入的username，password等，如果根据这些信息进行注册，注册成功返回True，注册失败返回false
#返回给前端的数据，成功：{'result':True,'message':successful} 失败：{'result':False,'message': "Error: The name={name} already exists."}
@app.route('/user/register',methods = ['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    question = data.get('question')
    answer  = data.get('anwser')
    result,message = user_register(username,password,question,answer)
    return jsonify({'result':result,'message':message})


#[user\None，message]
@app.route('/user/login',methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    result, message = user_search(username,password)
    return jsonify({'user':result,'message':message})

#[False,'message']
@app.route('/user/change', methods = ['POST'])
def change():
    data = request.get_json()
    name = data.get('username')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    question = data.get('question')
    answer = data.get('anwser')
    result,message = user_modify(name,old_password,new_password,question,answer)
    return jsonify({'result':result,'message':message})

@app.route('/user/charge',methods = ['POST'])
def charge():
    data = request.get_json()
    name = data.get('username')
    password = data.get('password')
    money = data.get('cash')
    result,message = user_money_modify(name,password,money)
    return jsonify({'result':result,'message':message})
    
@app.route('/user/mystock',methods = ['POST'])
def mystock():
    data = request.get_json()
    name = data.get('username')
    my_stock,message = user_stock_fetch(name)
    # my_stock:[{'id':, 'name':, 'stock_code':, 'stock_name':, 'num':},{....},{....}]
    stock = []
    for i in my_stock:
        price,mess = stock_search_by_code(i.get('stock_code'))
        i_stock = {'name':i.get('stock_name'),'code':i.get('stock_code'),'price':price.get('price'),'quantity':i.get('num')}
        stock.append(i_stock)
    return jsonify({'result':stock,'message':message})

# @app.route('/user/history',methods = ['POST'])
# def history():
#     data = request.get_json()
#     name = data.get('username')
#     history,message = user_record_fetch(name)
#     my_history = []
#     for i in history:



# @app.route('/user/find_password',methods = ['POST'])
# def find():
#     data = request.get_json()
#     name = data.get('name')
#     question = data.get('question')
#     anwser = data.get('anwser')
#     user = user_by_name('name')
#     if user['anwser'] == anwser:
#         return jsonify([True])
#     else:
#         return jsonify([False])

# @app.route('/user/self_stock',method = ['POST'])
# def self_stock():
#     data = request.get_json()
#     name = data.get('name')
#     password = data.get('password')
#     user = user_search(name,password)
    
#     if user.get('stock'):
#         my_stock = user.get('stock')
#         for i in stock:


    
    
    



if __name__ == "__main__":
    app.run(port=5000, debug=True)