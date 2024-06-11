import stock_base as sb

history,message = sb.user_record_fetch('adsds')
if history != None:
    my_history = []
    for i in history:
        piece = { 'time':i['time'] , 'number':i['id'] , 'code': i['stock_code'], 'price': i['price'] ,'buysell':'买入','quantity': 100,'gain':0 }
        #,'buysell':'买','quantity': 100,'gain':0 
        if i['num']<0:
            piece['quantity'] = -1*i['num']
            piece['buysell'] = '卖出'
        else:
            piece['quantity'] = i['num']
            piece['buysell'] = '买入'
            now_price,mess = sb.stock_search_by_code(piece['code'])
            piece['gain'] = now_price['price']*piece['quantity'] - piece['quantity']*piece['price']
        my_history.append(piece)
    print(my_history)
