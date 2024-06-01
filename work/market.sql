-- Active: 1716631946273@@127.0.0.1@3306@stock_history
CREATE DATABASE market;
DROP DATABASE market;

-- 一系列大盘上证指数，沪深300指数之类的按时间的数据
CREATE TABLE SZ00001(
    id INT PRIMARY KEY auto_increment,
    time VARCHAR(100), -- 交易时间
    market_id VARCHAR(500), -- 上证指数的代码
    market_name VARCHAR(500), -- 上证指数的名称
    open_price FLOAT, -- 开盘价（元）
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    end_price FLOAT, -- 收盘价（元）
    trade_num INT, -- 成交量（手）
    trade_money FLOAT, -- 成交额（元）
    amplitude FLOAT, -- 振幅（%）
    turnover_ratio FLOAT, -- 换手率（%）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    price_range FLOAT -- 涨跌额（元）
);