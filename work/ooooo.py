from datetime import datetime
import json
import akshare as ak
import pandas as pd

# 获取今天的日期
today = datetime.today().date()
print(type(today))
print(str(today))
today = str(today).replace("-", "")
print(today)

def stock_history_fetch(symbol:str = "600519", start_date:str = "20220101", end_date:str = "20240531",say:int = 0) -> tuple[bool,str]:
    "获取symbol的历史数据并存入文件"
    try:
        # stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol=symbol, start_date=start_date, end_date=end_date, adjust="")
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start_date, end_date=end_date, adjust="")
    except Exception as e:
        if say:
            print(f"-->Error: {e}")
        return False,f"Error: {e}"
    
    df = pd.DataFrame(stock_zh_a_hist_df)

    # 格式化日期列为指定格式
    df['日期'] = pd.to_datetime(df['日期'])
    df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
    
    if say:
        print(df)

    # 将获取的数据存入json文件中
    if df.empty:
        return False,f"Error: dataframe is empty"
    
    df.to_json('stock_history2.json',orient='records', force_ascii=False, indent=4)
    return True,f"Successfully"

a = stock_history_fetch(end_date=today)
print(a)