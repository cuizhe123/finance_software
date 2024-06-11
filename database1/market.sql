-- Active: 1717640791000@@127.0.0.1@3306@market
CREATE DATABASE market;
DROP DATABASE market;
USE market;

DROP TABLE market;
DROP TABLE sh000001;
DROP TABLE sz399001;
DROP TABLE bj899050;
DROP TABLE sh000300;

CREATE TABLE market(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 上证指数的代码
    market_name VARCHAR(500), -- 上证指数的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT, -- 52周最低
    UNIQUE(market_code)
);


-- 一系列大盘上证指数，沪深300指数之类的实时数据
CREATE TABLE sh000001(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 上证指数的代码
    market_name VARCHAR(500), -- 上证指数的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT, -- 52周最低
    UNIQUE(market_code)
);

CREATE TABLE sz399001(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 深证成指的代码
    market_name VARCHAR(500), -- 深证成指的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT, -- 52周最低
    UNIQUE(market_code)
);

CREATE TABLE bj899050(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 北证50的代码
    market_name VARCHAR(500), -- 北证50的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT, -- 52周最低
    UNIQUE(market_code)
);

CREATE TABLE sh000300(
    id INT PRIMARY KEY auto_increment,
    market_code VARCHAR(500), -- 沪深300的代码
    market_name VARCHAR(500), -- 沪深300的名称
    price FLOAT, -- 现价
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    price_fluctuation FLOAT, -- 涨跌幅（%）
    amplitude FLOAT, -- 振幅（%）
    yesterday_end FLOAT, -- 昨收
    today_open FLOAT, -- 今开
    trade_money FLOAT, -- 成交额（元）
    high52 FLOAT, -- 52周最高
    low52 FLOAT, -- 52周最低
    UNIQUE(market_code)
);