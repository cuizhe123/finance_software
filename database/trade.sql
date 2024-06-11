-- Active: 1717643381529@@127.0.0.1@3306@user_trade

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
    time VARCHAR(100),
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


