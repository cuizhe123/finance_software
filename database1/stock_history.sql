-- Active: 1717640791000@@127.0.0.1@3306@world
CREATE DATABASE stock_history;
DROP DATABASE stock_history;

-- 为每一个股票都生产一个table
CREATE TABLE sh600519(
    id INT PRIMARY KEY auto_increment,
    time VARCHAR(100), -- 交易时间
    stock_id VARCHAR(500), -- 股票的代码
    stock_name VARCHAR(500), -- 股票的名称
    exchange VARCHAR(10), -- 交易所标识
    open_price FLOAT, -- 开盘价（元）
    close_price FLOAT, -- 收盘价（元）
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    trade_num FLOAT, -- 成交量（手）
    trade_money FLOAT, -- 成交额（元）
    amplitude FLOAT, -- 振幅（%）
    up_down FLOAT, -- 涨跌幅（%）
    price_range FLOAT, -- 涨跌额（元）
    turnover_ratio FLOAT, -- 换手率
    UNIQUE(time)
);
