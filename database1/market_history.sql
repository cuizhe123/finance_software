-- Active: 1717640791000@@127.0.0.1@3306@market_history
CREATE DATABASE market_history;

DROP DATABASE market_history;

USE market_history;

CREATE TABLE sh000001(
    id INT PRIMARY KEY auto_increment,
    time VARCHAR(100), -- 交易时间
    market_code VARCHAR(500), -- 指数的代码
    market_name VARCHAR(500), -- 指数的名称
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