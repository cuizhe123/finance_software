# %%
import tushare as ts
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import statsmodels.api as sm
from tqdm import tqdm
import calendar


import warnings
warnings.filterwarnings('ignore')
# start_date 2005-01-31 end_date 2017-04-28

#%%
# 获取沪深300成份股
data = pd.DataFrame()
hs300 = pro.index_weight(index_code='399300.SZ', start_date='20050131', end_date='20170428')
hs300_list = hs300['con_code'].unique()
print(len(hs300_list))

#%%

# 拉取数据
fields = ["ts_code", "ann_date", "end_date", "profit_dedt", "bps", "revenue_ps", "profit_dedt",
          "cfps", "ocfps", "bps", "roe", "roa", "roe_yearly", "roe_yoy", "roa_yearly",
          "q_profit_yoy", "q_sales_yoy", "ocf_yoy", "q_gsprofit_margin", 'ocf_to_profit',
          "grossprofit_margin", "netprofit_margin", "q_netprofit_margin", 
          "assets_turn", "q_ocf_to_or", "ocf_to_opincome", "tangibleasset_to_debt", 
          "tbassets_to_totalassets", "longdeb_to_debt", "noncurrent_exint", 
          "networking_capital", "fcff", "invest_capital"
        ]

express_fields = ["ts_code", "ann_date", "end_date", "n_income", "open_net_assets", "revenue", "total_assets"]

bak_fields = ["ts_code", "trade_date",  "pe", "pe_ttm", "total_mv", "turnover_rate", "total_share"]

dividend_fields = ["ts_code","pay_date","cash_div_tax"]

def cal_end_date(date):
    date = date.to_pydatetime()
    _, last_day = calendar.monthrange(date.year, date.month)
    end_of_month = datetime(date.year, date.month, last_day)

    # 计算当前日期到月底的天数
    days_until_end_of_month = (end_of_month - date).days
    return int(days_until_end_of_month)

def ema(data, period):
    """ 计算指数移动平均 """
    return data.ewm(span=period, adjust=False).mean()

def macd(data, short_period=12, long_period=26, signal_period=9):
    """ 计算MACD, DIF, DEA """
    short_ema =ema(data, short_period)
    long_ema = ema(data, long_period)
    dif = short_ema - long_ema
    dea = ema(dif, signal_period)
    macd = 2 * (dif - dea)
    return dif, dea, macd

def rsi(data, period=14):
    """ 计算RSI """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def psy(data, period=12):
    """ 计算PSY """
    up_days = data.diff().apply(lambda x: 1 if x > 0 else 0)
    psy = up_days.rolling(window=period).sum() / period * 100
    return psy

def bias(data, period=6):
    """ 计算BIAS """
    ma = data.rolling(window=period).mean()
    bias = (data - ma) / ma * 100
    return bias

def rolling_regression(X, y, window):
    """
    滚动回归函数
    :param X: 自变量数据，pandas DataFrame格式。
    :param y: 因变量数据，pandas Series格式。
    :param window: 滚动窗口大小。
    :return: 每个窗口的回归系数和截距项。
    """
    assert len(X) == len(y), "X和y的长度必须相同"
    if len(y) == 0:
        return pd.Series([]), pd.Series([])
    # 添加截距项
    index = X.index
    X = sm.add_constant(X)

    # 存储每个窗口的结果
    alpha = []
    beta = []
    indexs = []

    # 滚动窗口回归
    for start in range(len(X) - window + 1):
        end = start + window
        if y[start:end].isna().any() or X[start:end]['pct_chg'].isna().any():
            alpha.append(np.nan)
            beta.append(np.nan)
        else:
            model = sm.OLS(y[start:end], X[start:end]).fit()
            alpha.append(model.params[0])
            beta.append(model.params[1])
        indexs.append(index[end-1])

    return pd.Series(alpha, index=indexs), pd.Series(beta, index=indexs)

# 获取基本面数据
df_features = pd.DataFrame()
start_date = '2010-01-01'
start_date_daily = (pd.to_datetime(start_date) - pd.Timedelta(days=720)).strftime('%Y-%m-%d')
start_date_month = (pd.to_datetime(start_date) - pd.Timedelta(days=1800)).strftime('%Y-%m-%d')
end_date = '2022-04-28'

# hs300_list = ["600027.SH"]

for code in tqdm(hs300_list):
    print(code)
    df_basic_stock = pro.fina_indicator(ts_code=code, start_date=start_date, end_date=end_date, fields=fields)
    df_express_stock = pro.express(ts_code=code, start_date=start_date, end_date=end_date, fields=express_fields)
    df_bak_stock = pro.daily_basic(ts_code=code, start_date=start_date_daily, end_date=end_date, fields= bak_fields )
    df_trade_stock = pro.monthly(ts_code=code, start_date=start_date_month, end_date=end_date, fields='ts_code,trade_date,open,high,low,close,vol,amount')
    df_trade_stock_daily = ts.pro_bar(ts_code=code, asset= 'E', adj = 'qfq', start_date=start_date_daily, end_date=end_date)
    df_trade_sh = ts.pro_bar(ts_code='000001.SH', asset='I', start_date=start_date_daily, end_date=end_date)
    df_basic_stock.index = pd.to_datetime(df_basic_stock['end_date'])
    df_basic_stock = df_basic_stock.resample('M').first().ffill()
    
    df_express_stock.index = pd.to_datetime(df_express_stock['end_date'])
    df_express_stock = df_express_stock.resample('M').last().ffill()
    df_express_stock = df_express_stock.reindex(df_basic_stock.index)
    df_bak_stock.index = pd.to_datetime(df_bak_stock['trade_date'])
    df_bak_stock_daily = df_bak_stock.copy().sort_index()
    df_bak_stock = df_bak_stock.resample('M').last().ffill()
    df_bak_stock = df_bak_stock.reindex(df_basic_stock.index)
    
    df_trade_stock_daily.index = pd.to_datetime(df_trade_stock_daily['trade_date'])
    df_trade_stock_daily = df_trade_stock_daily.sort_index()
    df_trade_sh.index = pd.to_datetime(df_trade_sh['trade_date'])
    df_trade_sh = df_trade_sh.sort_index()
    df_trade_stock_daily = df_trade_stock_daily.reindex(df_trade_sh.index)
    
    df_trade_stock.index = pd.to_datetime(df_trade_stock['trade_date'])
    
    df_trade_stock['return_1m'] = df_trade_stock['close'].pct_change(1)
    df_trade_stock['return_3m'] = df_trade_stock['close'].pct_change(3)
    df_trade_stock['return_6m'] = df_trade_stock['close'].pct_change(6)
    df_trade_stock['return_12m'] = df_trade_stock['close'].pct_change(12)
    
    wgt_return_1m = (df_bak_stock_daily['turnover_rate'].reindex(df_trade_stock_daily.index)*df_trade_stock_daily['pct_chg']).rolling(30).mean()
    wgt_return_3m = (df_bak_stock_daily['turnover_rate'].reindex(df_trade_stock_daily.index)*df_trade_stock_daily['pct_chg']).rolling(90).mean()
    wgt_return_6m = (df_bak_stock_daily['turnover_rate'].reindex(df_trade_stock_daily.index)*df_trade_stock_daily['pct_chg']).rolling(180).mean()
    wgt_return_12m = (df_bak_stock_daily['turnover_rate'].reindex(df_trade_stock_daily.index)*df_trade_stock_daily['pct_chg']).rolling(360).mean()
    
    exp_wgt_return_1m = (df_bak_stock_daily['turnover_rate']*(df_bak_stock_daily.index.to_series().apply(lambda x: np.exp(-4*cal_end_date(x))))*df_trade_stock_daily['pct_chg']).rolling(30).mean()
    exp_wgt_return_3m = (df_bak_stock_daily['turnover_rate']*(df_bak_stock_daily.index.to_series().apply(lambda x: np.exp(-4*cal_end_date(x)/3)))*df_trade_stock_daily['pct_chg']).rolling(90).mean()
    exp_wgt_return_6m = (df_bak_stock_daily['turnover_rate']*(df_bak_stock_daily.index.to_series().apply(lambda x: np.exp(-4*cal_end_date(x)/6)))*df_trade_stock_daily['pct_chg']).rolling(180).mean()
    exp_wgt_return_12m = (df_bak_stock_daily['turnover_rate']*(df_bak_stock_daily.index.to_series().apply(lambda x: np.exp(-4*cal_end_date(x)/12)))*df_trade_stock_daily['pct_chg']).rolling(360).mean()

    std_1m = df_trade_stock_daily['pct_chg'].rolling(30).std()
    std_3m = df_trade_stock_daily['pct_chg'].rolling(90).std()
    std_6m = df_trade_stock_daily['pct_chg'].rolling(180).std()
    std_12m = df_trade_stock_daily['pct_chg'].rolling(360).std()
    
    turn_1m = df_bak_stock_daily['turnover_rate'].rolling(30).mean()
    turn_3m = df_bak_stock_daily['turnover_rate'].rolling(90).mean()
    turn_6m = df_bak_stock_daily['turnover_rate'].rolling(180).mean()
    turn_12m = df_bak_stock_daily['turnover_rate'].rolling(360).mean()
    
    base_turn  = df_bak_stock_daily['turnover_rate'].rolling(720).mean()
    bias_turn_1m =  df_bak_stock_daily['turnover_rate'].rolling(30).mean() / base_turn 
    bias_turn_3m =  df_bak_stock_daily['turnover_rate'].rolling(90).mean() / base_turn 
    bias_turn_6m =  df_bak_stock_daily['turnover_rate'].rolling(180).mean() / base_turn 
    bias_turn_12m =  df_bak_stock_daily['turnover_rate'].rolling(360).mean() / base_turn 
    
    dif, dea, macd_ =  macd(df_trade_stock_daily['close'], 10, 30, 15)
    
    Halpha, beta = rolling_regression(df_trade_stock_daily['pct_chg'].ffill(), df_trade_sh['pct_chg'].ffill(), 60)
    
    df_sh_m = df_trade_sh.reindex(df_basic_stock.index)
    df_t_m = df_trade_stock_daily.reindex(df_basic_stock.index)
    df_t_m['ret'] = df_t_m['close'].pct_change().shift(-1)
    df_sh_m['ret'] = df_sh_m['close'].pct_change().shift(-1)
    
    
    df_features_stock = df_basic_stock[['ts_code', 'end_date']]
    
    
    # 构建基本面因子
    # 估值
    df_features_stock['EP'] = df_express_stock['n_income'] / df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['EPcut'] = df_basic_stock['profit_dedt'] / df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['BP'] = df_basic_stock['bps']* df_bak_stock['total_share'] / df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['SP'] = df_express_stock['revenue'] / df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['NCFP'] = df_basic_stock['cfps']* df_bak_stock['total_share']/df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['OCFP'] = df_basic_stock['ocfps']* df_bak_stock['total_share']/df_bak_stock['total_mv'].replace(0, np.nan) 
    df_features_stock['G/PE'] = df_basic_stock['q_profit_yoy'] / df_bak_stock['pe_ttm'].replace(0, np.nan) 
    
    
    #成长
    df_features_stock['Sales_G_q'] = df_basic_stock['q_sales_yoy']
    df_features_stock['Profit_G_q'] = df_basic_stock['q_profit_yoy']
    df_features_stock['OCF_G_q'] = df_basic_stock['ocf_yoy']
    df_features_stock['Profit_G_q'] = df_basic_stock['q_sales_yoy']
    df_features_stock['ROE_G_q'] = df_basic_stock['roe_yoy']
    
    #财务质量
    df_features_stock['ROE_q'] = df_basic_stock['roe']
    df_features_stock['ROE_ttm'] = df_basic_stock['roe_yearly']
    df_features_stock['ROA_q'] = df_basic_stock['roa']
    df_features_stock['ROA_ttm'] = df_basic_stock['roa_yearly']
    df_features_stock['grossprofitmargin_q'] = df_basic_stock['q_gsprofit_margin']
    df_features_stock['grossprofitmargin_ttm'] = df_basic_stock['grossprofit_margin']
    
    df_features_stock['profitmargin_q'] = df_basic_stock['q_netprofit_margin']
    df_features_stock['profitmargin_ttm'] = df_basic_stock['netprofit_margin']
    
    df_features_stock['assetturnover_q'] = df_basic_stock['assets_turn']
    df_features_stock['assetturnover_ttm'] = df_basic_stock['assets_turn'].rolling(12).mean() # 是否rolling
    
    df_features_stock['operationcashflowratio_q'] = df_basic_stock['ocf_to_profit']
    df_features_stock['operationcashflowratio_ttm'] = df_basic_stock['ocf_to_profit'].rolling(12).mean() # 是否rolling
    
    df_features_stock['financial_leverage'] = df_express_stock['total_assets']/ (df_basic_stock['bps']* df_bak_stock['total_share']).replace(0, np.nan) 
    df_features_stock['debtequityratio'] = df_basic_stock["noncurrent_exint"]/ (df_basic_stock['bps']* df_bak_stock['total_share']).replace(0, np.nan) 
    
    df_features_stock['ln_capital'] = np.log(df_bak_stock['total_mv'])
    
    df_features_stock['Halpha'] = Halpha.reindex(df_features_stock.index)
    df_features_stock['beta'] = beta.reindex(df_features_stock.index)
    
    df_features_stock['return_1m'] = df_trade_stock['return_1m']
    df_features_stock['return_3m'] = df_trade_stock['return_3m']
    df_features_stock['return_6m'] = df_trade_stock['return_6m']
    df_features_stock['return_12m'] = df_trade_stock['return_12m']
    
    df_features_stock['wgt_return_1m'] = wgt_return_1m.reindex(df_features_stock.index)
    df_features_stock['wgt_return_3m'] = wgt_return_3m.reindex(df_features_stock.index)
    df_features_stock['wgt_return_6m'] = wgt_return_6m.reindex(df_features_stock.index)
    df_features_stock['wgt_return_12m'] = wgt_return_12m.reindex(df_features_stock.index)
    
    df_features_stock['exp_wgt_return_1m'] = exp_wgt_return_1m.reindex(df_features_stock.index)
    df_features_stock['exp_wgt_return_3m'] = exp_wgt_return_3m.reindex(df_features_stock.index)
    df_features_stock['exp_wgt_return_6m'] = exp_wgt_return_6m.reindex(df_features_stock.index)
    df_features_stock['exp_wgt_return_12m'] = exp_wgt_return_12m.reindex(df_features_stock.index)
    
    
    df_features_stock['std1m'] = std_1m.reindex(df_features_stock.index)
    df_features_stock['std3m'] = std_3m.reindex(df_features_stock.index)
    df_features_stock['std6m'] = std_6m.reindex(df_features_stock.index)
    df_features_stock['std12m'] = std_12m.reindex(df_features_stock.index)
    
    df_features_stock['ln_price'] = np.log(df_trade_stock['close'])
    
    df_features_stock['turn_1m'] = turn_1m.reindex(df_features_stock.index)
    df_features_stock['turn_3m'] = turn_3m.reindex(df_features_stock.index)
    df_features_stock['turn_6m'] = turn_6m.reindex(df_features_stock.index)
    df_features_stock['turn_12m'] = turn_12m.reindex(df_features_stock.index)
    
    df_features_stock['macd'] = macd_.reindex(df_features_stock.index)
    df_features_stock['dif'] = dif.reindex(df_features_stock.index)
    df_features_stock['dea'] = dea.reindex(df_features_stock.index)
    
    df_features_stock['rsi'] = rsi(df_trade_stock_daily['close'], 20).reindex(df_features_stock.index)
    df_features_stock['psy'] = psy(df_trade_stock_daily['close'], 20).reindex(df_features_stock.index)
    df_features_stock['bias'] = bias(df_trade_stock_daily['close'], 20).reindex(df_features_stock.index)
    
    df_features_stock['ret_1m_after'] = (df_t_m['ret'] - df_sh_m['ret']).reindex(df_features_stock.index).shift(-1) 

    df_features = pd.concat([df_features, df_features_stock])

df_features.name = 'date'
df_features.drop(columns=['end_date'])
df_features.to_csv('data/features_2010_2022.csv')

