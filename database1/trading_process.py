# 用户交易过程整体逻辑
# 目前已知用户id
import time

class TradingHistory:
    def __init__(self, user_id):
        self.user_id = user_id
        self.history = []

    def add_trade(self, trade_number, stock_code, price, volume, trade_type):
        self.history.append({
            "trade_number": trade_number,
            "stock_code": stock_code,
            "price": price,
            "volume": volume,
            # 0卖出，1买入
            "trade_type": trade_type
        })

# 示例用法
user_id = "12345"
trading_record = TradingHistory(user_id)
trading_record.add_trade(1, "000631", 150.25, 100, "1")
trading_record.add_trade(2, "000644", 250.60, 50, "0")

    


# 根据用户输入，获取股票代码、交易类型、交易数量
def Trading_Process(userid, code, trading_type, trading_amount, stock_price):
    
    # userid 为用户id
    # code 为股票代码，是六位数字
    # trading_type 为交易类型，1是买入，0是卖出
    # trading_amount 为买卖的股票数量，整数
    # stock_price 为股票价格，浮点数
    
    # 用户交易的历史数据为列表
    trading_history = TradingHistory(user_id)   
    
    # 判断交易时间段
    current_time = time.time()
    # 如果当前时间在工作日的9：15-11：30或13：00-15：00之间，可以进行交易
    # 将时间功能ban掉，因为不利于测试
    user_holding = {}
    # Step1 获取用户当前持仓信息和资金信息
    user_money = get('user_money', userid)
    # 持仓信息为字典，键为代码，值为持股数 
    user_holding = get('user_holding', userid)
    # Step2 判断交易类型
    if trading_type == 1:
        # 买入
        # Step3 判断用户资金是否足够
        
        if user_money < stock_price * trading_amount:
            return '资金不足，交易失败'
        # Step4 更新用户资金信息
        user_money -= stock_price * trading_amount
        # Step5 更新用户持仓信息
        if code in user_holding:
            user_holding[code] += trading_amount
        else:
            user_holding[code] = trading_amount    
        # 存入该用户的交易历史
       
    elif trading_type == 0:
        # 卖出
        # Step3 判断用户是否持有该股票
        if code not in user_holding:
            return '用户未持有该股票，交易失败'
        # Step4 判断用户持有股票数量是否足够
        if user_holding[code] < trading_amount:
            return '用户持有股票数量不足，交易失败'
        # Step5 更新用户资金信息 
        user_money += stock_price * trading_amount
        # Step6 更新用户持仓信息
        user_holding[code] -= trading_amount
        
    trading_history.add_trade(trading_history[-1]['trade_number']+1, code, stock_price, trading_amount, trading_type)
    # 将新的用户信息存入数据库
        
        
        