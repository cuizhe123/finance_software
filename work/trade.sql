-- Active: 1716631946273@@127.0.0.1@3306@user_trade

CREATE DATABASE user_trade;
DROP DATABASE user_trade;

-- alltick.co token 712e4aba24ad130782ba23dc6c3770ca-c-app
USE user_trade;

DROP TABLE users;

DROP TABLE current_stock;

DROP TABLE users_stock;
Drop TABLE self_choose;
Drop TABLE trade_record;

CREATE TABLE users ( -- 用户的个人信息
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(500), -- name是唯一的标识
    password VARCHAR(100),
    question VARCHAR(3000),
    answer VARCHAR(3000),
    money FLOAT,
    UNIQUE(name)
);


CREATE TABLE current_stock( -- 当前的股票的数据，显示当前每一只股票的价格
    id INT PRIMARY KEY auto_increment,
    stock_code VARCHAR(500), -- 股票的编号
    stock_name VARCHAR(500), -- 股票的名称
    exchange VARCHAR(500), -- 交易所的名称 上证，深证
    price FLOAT, -- 最新价格（元）p
    up_down FLOAT, -- 涨跌幅（%）
    price_range FLOAT, -- 涨跌额（元）
    trade_num FLOAT, -- 成交量（手）
    trade_money FLOAT, -- 成交额（元）
    amplitude FLOAT, -- 振幅（%）
    high_price FLOAT, -- 最高价（元）
    low_price FLOAT, -- 最低价（元）
    today_open FLOAT, -- 今开 （元）
    yester_price FLOAT, -- 昨日收盘价（元）
    quantity_ratio FLOAT, -- 量比（%）
    turnover_ratio FLOAT, -- 换手（%）
    pe_ratio FLOAT, -- 市盈率(%) 总市值除以预估全年净利润 
    pb_ratio FLOAT, --  市净率
    total_value FLOAT, -- 总市值（元）
    circle_value FLOAT, -- 流通市值（元）
    increase_ratio FLOAT, -- 涨速（%）
    five_up_down FLOAT, -- 5min 涨跌
    zdf60 FLOAT, -- 60日涨跌幅（%）
    zdfnc FLOAT, -- 年初至今涨跌幅（%）
    UNIQUE(stock_code),
    UNIQUE(stock_name)
);


CREATE TABLE users_stock( -- 用户的持仓信息
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(500), -- name不唯一
    stock_code VARCHAR(500),
    stock_name VARCHAR(500),
    num INT DEFAULT 0,
    CONSTRAINT fk_stock_user_name FOREIGN KEY (name) 
    REFERENCES users(name) ON DELETE CASCADE ON UPDATE CASCADE, -- 设置外键，这个和users的用户name相关联
    CONSTRAINT fk_stock_current_stockid FOREIGN KEY (stock_code) 
    REFERENCES current_stock(stock_code) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT k_stock_current_stockname FOREIGN KEY (stock_name) 
    REFERENCES current_stock(stock_name) ON DELETE CASCADE ON UPDATE CASCADE
);



CREATE TABLE self_choose( -- 用户的自选个股
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(500), -- name不唯一
    stock_code VARCHAR(500),
    stock_name VARCHAR(500),
    CONSTRAINT fk_choose_user_name FOREIGN KEY (name) 
    REFERENCES users(name) ON DELETE CASCADE ON UPDATE CASCADE, -- 设置外键，这个和users的用户name相关联
    CONSTRAINT fk_choose_current_stockid FOREIGN KEY (stock_code) 
    REFERENCES current_stock(stock_code) ON DELETE CASCADE ON UPDATE CASCADE, -- 设置外键，这个和current_stock的用户stock_code相关联
    CONSTRAINT fk_choose_current_stockname FOREIGN KEY (stock_name) 
    REFERENCES current_stock(stock_name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE trade_record( -- 用户的交易记录
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(500), -- name不唯一
    -- record INT, -- 用户的第record次交易，好把用户的同一次交易信息统合在一起
    stock_code VARCHAR(500),  -- 用户的第record次交易的某一个股票代码
    stock_name VARCHAR(500),
    num INT, -- 第record次交易的某一个股票的数量
    price FLOAT, -- 当时交易的价格
    CONSTRAINT fk_record_user_name FOREIGN KEY (name) 
    REFERENCES users(name) ON DELETE CASCADE ON UPDATE CASCADE, -- 设置外键，这个和users的用户name相关联
    CONSTRAINT fk_record_current_stockid FOREIGN KEY (stock_code) 
    REFERENCES current_stock(stock_code) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_record_current_stockname FOREIGN KEY (stock_name) 
    REFERENCES current_stock(stock_name) ON DELETE CASCADE ON UPDATE CASCADE
);



-- INSERT INTO users (name, password)
-- VALUES ('屈航', '111111');

-- INSERT INTO trade_record (name)
-- VALUES ('屈航');

-- DELETE FROM users WHERE name = '屈航';


