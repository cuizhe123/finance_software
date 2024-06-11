import akshare as ak
import pandas as pd
import sys

#* 沪交所的股票数据
def fetch_sh_stock_now(say:int = 0) ->tuple[bool, str]:
    '沪交所的股票数据并存入stock_sh_now.json'
    try:
        stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
    except Exception as e:
        if say:
            print(f"-->Error: {e}")
        return False,f"Error: {e}"
    df = pd.DataFrame(stock_sh_a_spot_em_df)

    # 将 sh股票 写入 json 文件
    df.to_json('stock_sh_now.json',orient='records', force_ascii=False, indent=4)
    if say:
        print(stock_sh_a_spot_em_df)
    return True,f"Successfully"

 #* 深交所的股票数据
def fetch_sz_stock_now(say:int = 0)->tuple[bool, str]:
    '深交所的股票数据并存入stock_sz_now.json'
    try:
        stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
    except Exception as e:
        if say:
            print(f"-->Error: {e}")
        return False, f"Error: {e}"
    df = pd.DataFrame(stock_sz_a_spot_em_df)

    # 将 sz股票 写入 json 文件
    df.to_json('stock_sz_now.json',orient='records', force_ascii=False, indent=4)
    if say:
        print(stock_sz_a_spot_em_df)
    return True,f"Successfully"

a = fetch_sh_stock_now()

b = fetch_sz_stock_now()