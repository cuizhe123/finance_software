from flask import Flask,request,jsonify,make_response
from users_base import user_register, user_search, user_modify, user_money_modify,user_search_by_name
from stock_base import user_stock_fetch, stock_search_by_code,user_record_fetch,user_stock_modify,user_stock_record,user_stock_clear
from market_base import market_search_all,market_search_by_name,market_search_by_code
from history_base import history_market_search,history_stock_search
# from history_base import history_stock_search,history_market_search
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#注册界面，收到传入的username，password等，如果根据这些信息进行注册，注册成功返回True，注册失败返回false
#返回给前端的数据，成功：{'result':True,'message':successful} 失败：{'result':False,'message': "Error: The name={name} already exists."}


@app.route('/user/register',methods = ['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    question = data.get('question')
    answer  = data.get('answer')
    result,message = user_register(username,password,question,answer)
    return jsonify({'result':result,'message':message}),200


#[user\None，message]
@app.route('/user/login',methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    result, message = user_search(username,password)
    return jsonify({'user':result,'message':message})

@app.route('/user/by_name',methods = ['POST'])
def by_name():
    data = request.get_json()
    username = data.get('username')
    result, message = user_search_by_name(username)
    return jsonify({'user':result,'message':message})



#[False,'message']
@app.route('/user/change', methods = ['POST'])
def change():
    data = request.get_json()
    name = data.get('username')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    question = data.get('question')
    answer = data.get('answer')
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
    if my_stock != None:
        stock = []
        for i in my_stock:
            price,mess = stock_search_by_code(i['stock_code'])
            i_stock = {'name':i['stock_name'],'code':i['stock_code'],'price':price['price'],'quantity':i['num']}
            stock.append(i_stock)
        return jsonify({'result':stock,'message':message})
    else:
        return jsonify({'result':None,'message':message})
    
@app.route('/user/my_single_stock',methods = ['POST'])
def my_single_stock():
    data = request.get_json()
    name = data.get('username')
    code = data.get('code')
    my_stock,message = user_stock_fetch(name)
    # my_stock:[{'id':, 'name':, 'stock_code':, 'stock_name':, 'num':},{....},{....}]
    if my_stock != None:
        num = 0
        for i in my_stock:
             if i['stock_code'] == code:
                 num = i['num']
        return jsonify({'result':num,'message':message})
    else:
        return jsonify({'result':0,'message':message})
    
@app.route('/user/history',methods = ['POST'])
def history():
    data = request.get_json()
    name = data.get('username')
    history,message = user_record_fetch(name)
    if history != None:
        my_history = []
        for i in history:
            piece = { 'time':i['time'] , 'name':i['stock_name'] , 'code': i['stock_code'], 'price': i['price'] ,'buysell':'买入','quantity': 100,'gain':0 }
            #,'buysell':'买','quantity': 100,'gain':0 
            if i['num']<0:
                piece['quantity'] = -1*i['num']
                piece['buysell'] = '卖出'
            else:
                piece['quantity'] = i['num']
                piece['buysell'] = '买入'
                now_price,mess = stock_search_by_code(piece['code'])
                piece['gain'] = now_price['price']*piece['quantity'] - piece['quantity']*piece['price']
            my_history.append(piece)
        return jsonify({'result':my_history,'message': message})
    else:
        return jsonify({'result':None,'message': message})

@app.route('/stock/stock_mess',methods = ['POST'])
def stock_mess():
    data = request.get_json()
    code = data.get('code')
    market = ['sh000001','sz399001','bj899050','sh000300']
    if code in market:
        stock,mess = market_search_by_code(code)
        if stock !=None:
            return jsonify({'result':stock,'message':mess})
        else:
            return jsonify({'result':None,'message':mess})
    else:
        stock,mess = stock_search_by_code(code)
        if stock !=None:
            return jsonify({'result':stock,'message':mess})
        else:
            return jsonify({'result':None,'message':mess})
        # {'id':stock[0], 'stock_code':stock[1], 'stock_name':stock[2], 'exchange':stock[3], 'price':stock[4], 'up_down':stock[5], 'price_range':stock[6], 'trade_num':stock[7], 'trade_money':stock[8], 'amplitude':stock[9], 'high_price':stock[10], 'low_price':stock[11], 'today_open':stock[12], 'yester_price':stock[13], 'quantity_ratio':stock[14], 'turnover_ratio':stock[15], 'pe_ratio':stock[16], 'pb_ratio':stock[17], 'total_value':stock[18], 'circle_value':stock[19], 'increase_ratio':stock[20], 'five_up_down':stock[21], 'zdf60':stock[22], 'dfnc':stock[23]}

@app.route('/trade/buyin',methods = ['POST'])
def buyin():
    data = request.get_json()
    username = data.get('username')
    stock_code = data.get('stock_code')
    stock_name = data.get('stock_name')
    buy_quantity = data.get('buy_quantity')
    price = data.get('price')
    user,mess = user_search_by_name(username)
    my_money = user['money']
    password = user['password']
    if my_money >=price*buy_quantity:
        result_buy,mess2 = user_stock_modify(username,stock_code,stock_name,buy_quantity)
        result_change,mess3 = user_money_modify(username,password,my_money-price*buy_quantity)
        result_record,mess4 = user_stock_record(username,stock_code,stock_name,buy_quantity,price)
        return jsonify({'result':True,"message":'successful'})
    else:
        return jsonify({'result':False,"message":'Money is not enough'})



@app.route('/trade/sellout',methods = ['POST'])
def sellout():
    data = request.get_json()
    username = data.get('username')
    stock_code = data.get('stock_code')
    stock_name = data.get('stock_name')
    sell_quantity = data.get('sell_quantity')
    price = data.get('price')

    user,mess = user_search_by_name(username)
    my_money = user['money']
    password = user['password']

    my_quantity = 0
    my_stock ,mess = user_stock_fetch(username)
    if my_stock != None:
        for i in my_stock:
            if i['stock_code'] == stock_code:
                my_quantity = i['num']
    else:
        my_quantity = 0
    
    if my_quantity >= sell_quantity:
        result_sell,mess2 = user_stock_modify(username,stock_code,stock_name,sell_quantity,1)
        result_change,mess3 = user_money_modify(username,password,my_money+price*sell_quantity)
        result_record,mess4 = user_stock_record(username,stock_code,stock_name,sell_quantity,price,'0',1)
        user_stock_clear()
        return jsonify({'result':True,"message":'successful'})
    else:
        return jsonify({'result':False,"message":'my_quantity is not enough'})
    
@app.route('/stock/history')
def get_history():
    data = request.get_json()
    market = ['sh000001','sz399001','bj899050','sh000300']
    code = data.get('code')
    if code in market:
        stock,mess = history_market_search(code)
        if stock !=None:
            return jsonify({'result':stock,'message':mess})
        else:
            return jsonify({'result':None,'message':mess})
    else:
        stock,mess = history_stock_search(code)
        if stock !=None:
            return jsonify({'result':stock,'message':mess})
        else:
            return jsonify({'result':None,'message':mess})
    
    
    



if __name__ == "__main__":
    app.run(port=5000, debug=True)