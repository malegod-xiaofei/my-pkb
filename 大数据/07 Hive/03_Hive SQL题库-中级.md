尚硅谷大数据技术之Hive SQL题库-中级

（作者：尚硅谷研究院）

版本：V1.0

# 1 环境准备

## 1.1 用户信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS user_info;

create table user_info(

`user_id`  string COMMENT '用户id',

`gender`   string COMMENT '性别',

`birthday` string COMMENT '生日'

) COMMENT '用户信息表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table user_info

values ('101', '男', '1990-01-01'),

('102', '女', '1991-02-01'),

('103', '女', '1992-03-01'),

('104', '男', '1993-04-01'),

('105', '女', '1994-05-01'),

('106', '男', '1995-06-01'),

('107', '女', '1996-07-01'),

('108', '男', '1997-08-01'),

('109', '女', '1998-09-01'),

('1010', '男', '1999-10-01');

## 1.2 商品信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS sku_info;

CREATE TABLE sku_info(

`sku_id`      string COMMENT '商品id',

`name`        string COMMENT '商品名称',

`category_id` string COMMENT '所属分类id',

`from_date`   string COMMENT '上架日期',

`price`       double COMMENT '商品单价'

) COMMENT '商品属性表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table sku_info

values ('1', 'xiaomi 10', '1', '2020-01-01', 2000),

('2', '手机壳', '1', '2020-02-01', 10),

('3', 'apple 12', '1', '2020-03-01', 5000),

('4', 'xiaomi 13', '1', '2020-04-01', 6000),

('5', '破壁机', '2', '2020-01-01', 500),

('6', '洗碗机', '2', '2020-02-01', 2000),

('7', '热水壶', '2', '2020-03-01', 100),

('8', '微波炉', '2', '2020-04-01', 600),

('9', '自行车', '3', '2020-01-01', 1000),

('10', '帐篷', '3', '2020-02-01', 100),

('11', '烧烤架', '3', '2020-02-01', 50),

('12', '遮阳伞', '3', '2020-03-01', 20);

## 1.3 商品分类信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS category_info;

create table category_info(

`category_id`   string,

`category_name` string

) COMMENT '品类表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table category_info

values ('1','数码'),

('2','厨卫'),

('3','户外');

## 1.4 订单信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS order_info;

create table order_info(

`order_id`     string COMMENT '订单id',

`user_id`      string COMMENT '用户id',

`create_date`  string COMMENT '下单日期',

`total_amount` decimal(16, 2) COMMENT '订单总金额'

) COMMENT '订单表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table order_info

values ('1', '101', '2021-09-27', 29000.00),

('2', '101', '2021-09-28', 70500.00),

('3', '101', '2021-09-29', 43300.00),

('4', '101', '2021-09-30', 860.00),

('5', '102', '2021-10-01', 46180.00),

('6', '102', '2021-10-01', 50000.00),

('7', '102', '2021-10-01', 75500.00),

('8', '102', '2021-10-02', 6170.00),

('9', '103', '2021-10-02', 18580.00),

('10', '103', '2021-10-02', 28000.00),

('11', '103', '2021-10-02', 23400.00),

('12', '103', '2021-10-03', 5910.00),

('13', '104', '2021-10-03', 13000.00),

('14', '104', '2021-10-03', 69500.00),

('15', '104', '2021-10-03', 2000.00),

('16', '104', '2021-10-03', 5380.00),

('17', '105', '2021-10-04', 6210.00),

('18', '105', '2021-10-04', 68000.00),

('19', '105', '2021-10-04', 43100.00),

('20', '105', '2021-10-04', 2790.00),

('21', '106', '2021-10-04', 9390.00),

('22', '106', '2021-10-05', 58000.00),

('23', '106', '2021-10-05', 46600.00),

('24', '106', '2021-10-05', 5160.00),

('25', '107', '2021-10-05', 55350.00),

('26', '107', '2021-10-05', 14500.00),

('27', '107', '2021-10-06', 47400.00),

('28', '107', '2021-10-06', 6900.00),

('29', '108', '2021-10-06', 56570.00),

('30', '108', '2021-10-06', 44500.00),

('31', '108', '2021-10-07', 50800.00),

('32', '108', '2021-10-07', 3900.00),

('33', '109', '2021-10-07', 41480.00),

('34', '109', '2021-10-07', 88000.00),

('35', '109', '2020-10-08', 15000.00),

('36', '109', '2020-10-08', 9020.00),

('37', '1010', '2020-10-08', 9260.00),

('38', '1010', '2020-10-08', 12000.00),

('39', '1010', '2020-10-08', 23900.00),

('40', '1010', '2020-10-08', 6790.00);

## 1.5 订单明细表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS order_detail;

CREATE TABLE order_detail

(

`order_detail_id` string COMMENT '订单明细id',

`order_id`        string COMMENT '订单id',

`sku_id`          string COMMENT '商品id',

`create_date`     string COMMENT '下单日期',

`price`           decimal(16, 2) COMMENT '下单时的商品单价',

`sku_num`         int COMMENT '下单商品件数'

) COMMENT '订单明细表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

INSERT overwrite table order_detail

values ('1', '1', '1', '2021-09-27', 2000.00, 2),

('2', '1', '3', '2021-09-27', 5000.00, 5),

('3', '2', '4', '2021-09-28', 6000.00, 9),

('4', '2', '5', '2021-09-28', 500.00, 33),

('5', '3', '7', '2021-09-29', 100.00, 37),

('6', '3', '8', '2021-09-29', 600.00, 46),

('7', '3', '9', '2021-09-29', 1000.00, 12),

('8', '4', '12', '2021-09-30', 20.00, 43),

('9', '5', '1', '2021-10-01', 2000.00, 8),

('10', '5', '2', '2021-10-01', 10.00, 18),

('11', '5', '3', '2021-10-01', 5000.00, 6),

('12', '6', '4', '2021-10-01', 6000.00, 8),

('13', '6', '6', '2021-10-01', 2000.00, 1),

('14', '7', '7', '2021-10-01', 100.00, 17),

('15', '7', '8', '2021-10-01', 600.00, 48),

('16', '7', '9', '2021-10-01', 1000.00, 45),

('17', '8', '10', '2021-10-02', 100.00, 48),

('18', '8', '11', '2021-10-02', 50.00, 15),

('19', '8', '12', '2021-10-02', 20.00, 31),

('20', '9', '1', '2021-09-30', 2000.00, 9),

('21', '9', '2', '2021-10-02', 10.00, 5800),

('22', '10', '4', '2021-10-02', 6000.00, 1),

('23', '10', '5', '2021-10-02', 500.00, 24),

('24', '10', '6', '2021-10-02', 2000.00, 5),

('25', '11', '8', '2021-10-02', 600.00, 39),

('26', '12', '10', '2021-10-03', 100.00, 47),

('27', '12', '11', '2021-10-03', 50.00, 19),

('28', '12', '12', '2021-10-03', 20.00, 13000),

('29', '13', '1', '2021-10-03', 2000.00, 4),

('30', '13', '3', '2021-10-03', 5000.00, 1),

('31', '14', '4', '2021-10-03', 6000.00, 5),

('32', '14', '5', '2021-10-03', 500.00, 47),

('33', '14', '6', '2021-10-03', 2000.00, 8),

('34', '15', '7', '2021-10-03', 100.00, 20),

('35', '16', '10', '2021-10-03', 100.00, 22),

('36', '16', '11', '2021-10-03', 50.00, 42),

('37', '16', '12', '2021-10-03', 20.00, 7400),

('38', '17', '1', '2021-10-04', 2000.00, 3),

('39', '17', '2', '2021-10-04', 10.00, 21),

('40', '18', '4', '2021-10-04', 6000.00, 8),

('41', '18', '5', '2021-10-04', 500.00, 28),

('42', '18', '6', '2021-10-04', 2000.00, 3),

('43', '19', '7', '2021-10-04', 100.00, 55),

('44', '19', '8', '2021-10-04', 600.00, 11),

('45', '19', '9', '2021-10-04', 1000.00, 31),

('46', '20', '11', '2021-10-04', 50.00, 45),

('47', '20', '12', '2021-10-04', 20.00, 27),

('48', '21', '1', '2021-10-04', 2000.00, 2),

('49', '21', '2', '2021-10-04', 10.00, 39),

('50', '21', '3', '2021-10-04', 5000.00, 1),

('51', '22', '4', '2021-10-05', 6000.00, 8),

('52', '22', '5', '2021-10-05', 500.00, 20),

('53', '23', '7', '2021-10-05', 100.00, 58),

('54', '23', '8', '2021-10-05', 600.00, 18),

('55', '23', '9', '2021-10-05', 1000.00, 30),

('56', '24', '10', '2021-10-05', 100.00, 27),

('57', '24', '11', '2021-10-05', 50.00, 28),

('58', '24', '12', '2021-10-05', 20.00, 53),

('59', '25', '1', '2021-10-05', 2000.00, 5),

('60', '25', '2', '2021-10-05', 10.00, 35),

('61', '25', '3', '2021-10-05', 5000.00, 9),

('62', '26', '4', '2021-10-05', 6000.00, 1),

('63', '26', '5', '2021-10-05', 500.00, 13),

('64', '26', '6', '2021-10-05', 2000.00, 1),

('65', '27', '7', '2021-10-06', 100.00, 30),

('66', '27', '8', '2021-10-06', 600.00, 19),

('67', '27', '9', '2021-10-06', 1000.00, 33),

('68', '28', '10', '2021-10-06', 100.00, 37),

('69', '28', '11', '2021-10-06', 50.00, 46),

('70', '28', '12', '2021-10-06', 20.00, 45),

('71', '29', '1', '2021-10-06', 2000.00, 8),

('72', '29', '2', '2021-10-06', 10.00, 57),

('73', '29', '3', '2021-10-06', 5000.00, 8),

('74', '30', '4', '2021-10-06', 6000.00, 3),

('75', '30', '5', '2021-10-06', 500.00, 33),

('76', '30', '6', '2021-10-06', 2000.00, 5),

('77', '31', '8', '2021-10-07', 600.00, 13),

('78', '31', '9', '2021-10-07', 1000.00, 43),

('79', '32', '10', '2021-10-07', 100.00, 24),

('80', '32', '11', '2021-10-07', 50.00, 30),

('81', '33', '1', '2021-10-07', 2000.00, 8),

('82', '33', '2', '2021-10-07', 10.00, 48),

('83', '33', '3', '2021-10-07', 5000.00, 5),

('84', '34', '4', '2021-10-07', 6000.00, 10),

('85', '34', '5', '2021-10-07', 500.00, 44),

('86', '34', '6', '2021-10-07', 2000.00, 3),

('87', '35', '8', '2020-10-08', 600.00, 25),

('88', '36', '10', '2020-10-08', 100.00, 57),

('89', '36', '11', '2020-10-08', 50.00, 44),

('90', '36', '12', '2020-10-08', 20.00, 56),

('91', '37', '1', '2020-10-08', 2000.00, 2),

('92', '37', '2', '2020-10-08', 10.00, 26),

('93', '37', '3', '2020-10-08', 5000.00, 1),

('94', '38', '6', '2020-10-08', 2000.00, 6),

('95', '39', '7', '2020-10-08', 100.00, 35),

('96', '39', '8', '2020-10-08', 600.00, 34),

('97', '40', '10', '2020-10-08', 100.00, 37),

('98', '40', '11', '2020-10-08', 50.00, 51),

('99', '40', '12', '2020-10-08', 20.00, 27);

## 1.6 登录明细表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS user_login_detail;

CREATE TABLE user_login_detail

(

`user_id`    string comment '用户id',

`ip_address` string comment 'ip地址',

`login_ts`   string comment '登录时间',

`logout_ts`  string comment '登出时间'

) COMMENT '用户登录明细表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

INSERT overwrite table user_login_detail

VALUES ('101', '180.149.130.161', '2021-09-21 08:00:00', '2021-09-27 08:30:00'),

('101', '180.149.130.161', '2021-09-27 08:00:00', '2021-09-27 08:30:00'),

('101', '180.149.130.161', '2021-09-28 09:00:00', '2021-09-28 09:10:00'),

('101', '180.149.130.161', '2021-09-29 13:30:00', '2021-09-29 13:50:00'),

('101', '180.149.130.161', '2021-09-30 20:00:00', '2021-09-30 20:10:00'),

('102', '120.245.11.2', '2021-09-22 09:00:00', '2021-09-27 09:30:00'),

('102', '120.245.11.2', '2021-10-01 08:00:00', '2021-10-01 08:30:00'),

('102', '180.149.130.174', '2021-10-01 07:50:00', '2021-10-01 08:20:00'),

('102', '120.245.11.2', '2021-10-02 08:00:00', '2021-10-02 08:30:00'),

('103', '27.184.97.3', '2021-09-23 10:00:00', '2021-09-27 10:30:00'),

('103', '27.184.97.3', '2021-10-03 07:50:00', '2021-10-03 09:20:00'),

('104', '27.184.97.34', '2021-09-24 11:00:00', '2021-09-27 11:30:00'),

('104', '27.184.97.34', '2021-10-03 07:50:00', '2021-10-03 08:20:00'),

('104', '27.184.97.34', '2021-10-03 08:50:00', '2021-10-03 10:20:00'),

('104', '120.245.11.89', '2021-10-03 08:40:00', '2021-10-03 10:30:00'),

('105', '119.180.192.212', '2021-10-04 09:10:00', '2021-10-04 09:30:00'),

('106', '119.180.192.66', '2021-10-04 08:40:00', '2021-10-04 10:30:00'),

('106', '119.180.192.66', '2021-10-05 21:50:00', '2021-10-05 22:40:00'),

('107', '219.134.104.7', '2021-09-25 12:00:00', '2021-09-27 12:30:00'),

('107', '219.134.104.7', '2021-10-05 22:00:00', '2021-10-05 23:00:00'),

('107', '219.134.104.7', '2021-10-06 09:10:00', '2021-10-06 10:20:00'),

('107', '27.184.97.46', '2021-10-06 09:00:00', '2021-10-06 10:00:00'),

('108', '101.227.131.22', '2021-10-06 09:00:00', '2021-10-06 10:00:00'),

('108', '101.227.131.22', '2021-10-06 22:00:00', '2021-10-06 23:00:00'),

('109', '101.227.131.29', '2021-09-26 13:00:00', '2021-09-27 13:30:00'),

('109', '101.227.131.29', '2021-10-06 08:50:00', '2021-10-06 10:20:00'),

('109', '101.227.131.29', '2021-10-08 09:00:00', '2021-10-08 09:10:00'),

('1010', '119.180.192.10', '2021-09-27 14:00:00', '2021-09-27 14:30:00'),

('1010', '119.180.192.10', '2021-10-09 08:50:00', '2021-10-09 10:20:00');

## 1.7 商品价格变更明细表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS sku_price_modify_detail;

CREATE TABLE sku_price_modify_detail

(

`sku_id`      string comment '商品id',

`new_price`   decimal(16, 2) comment '更改后的价格',

`change_date` string comment '变动日期'

) COMMENT '商品价格变更明细表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table sku_price_modify_detail

values ('1', 1900, '2021-09-25'),

('1', 2000, '2021-09-26'),

('2', 80, '2021-09-29'),

('2', 10, '2021-09-30'),

('3', 4999, '2021-09-25'),

('3', 5000, '2021-09-26'),

('4', 5600, '2021-09-26'),

('4', 6000, '2021-09-27'),

('5', 490, '2021-09-27'),

('5', 500, '2021-09-28'),

('6', 1988, '2021-09-30'),

('6', 2000, '2021-10-01'),

('7', 88, '2021-09-28'),

('7', 100, '2021-09-29'),

('8', 800, '2021-09-28'),

('8', 600, '2021-09-29'),

('9', 1100, '2021-09-27'),

('9', 1000, '2021-09-28'),

('10', 90, '2021-10-01'),

('10', 100, '2021-10-02'),

('11', 66, '2021-10-01'),

('11', 50, '2021-10-02'),

('12', 35, '2021-09-28'),

('12', 20, '2021-09-29');

## 1.8 配送信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS delivery_info;

CREATE TABLE delivery_info

(

`delivery_id` string comment '配送单id',

`order_id`    string comment '订单id',

`user_id`     string comment '用户id',

`order_date`  string comment '下单日期',

`custom_date` string comment '期望配送日期'

) COMMENT '邮寄信息表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table delivery_info

values ('1', '1', '101', '2021-09-27', '2021-09-29'),

('2', '2', '101', '2021-09-28', '2021-09-28'),

('3', '3', '101', '2021-09-29', '2021-09-30'),

('4', '4', '101', '2021-09-30', '2021-10-01'),

('5', '5', '102', '2021-10-01', '2021-10-01'),

('6', '6', '102', '2021-10-01', '2021-10-01'),

('7', '7', '102', '2021-10-01', '2021-10-03'),

('8', '8', '102', '2021-10-02', '2021-10-02'),

('9', '9', '103', '2021-10-02', '2021-10-03'),

('10', '10', '103', '2021-10-02', '2021-10-04'),

('11', '11', '103', '2021-10-02', '2021-10-02'),

('12', '12', '103', '2021-10-03', '2021-10-03'),

('13', '13', '104', '2021-10-03', '2021-10-04'),

('14', '14', '104', '2021-10-03', '2021-10-04'),

('15', '15', '104', '2021-10-03', '2021-10-03'),

('16', '16', '104', '2021-10-03', '2021-10-03'),

('17', '17', '105', '2021-10-04', '2021-10-04'),

('18', '18', '105', '2021-10-04', '2021-10-06'),

('19', '19', '105', '2021-10-04', '2021-10-06'),

('20', '20', '105', '2021-10-04', '2021-10-04'),

('21', '21', '106', '2021-10-04', '2021-10-04'),

('22', '22', '106', '2021-10-05', '2021-10-05'),

('23', '23', '106', '2021-10-05', '2021-10-05'),

('24', '24', '106', '2021-10-05', '2021-10-07'),

('25', '25', '107', '2021-10-05', '2021-10-05'),

('26', '26', '107', '2021-10-05', '2021-10-06'),

('27', '27', '107', '2021-10-06', '2021-10-06'),

('28', '28', '107', '2021-10-06', '2021-10-07'),

('29', '29', '108', '2021-10-06', '2021-10-06'),

('30', '30', '108', '2021-10-06', '2021-10-06'),

('31', '31', '108', '2021-10-07', '2021-10-09'),

('32', '32', '108', '2021-10-07', '2021-10-09'),

('33', '33', '109', '2021-10-07', '2021-10-08'),

('34', '34', '109', '2021-10-07', '2021-10-08'),

('35', '35', '109', '2021-10-08', '2021-10-10'),

('36', '36', '109', '2021-10-08', '2021-10-09'),

('37', '37', '1010', '2021-10-08', '2021-10-10'),

('38', '38', '1010', '2021-10-08', '2021-10-10'),

('39', '39', '1010', '2021-10-08', '2021-10-09'),

('40', '40', '1010', '2021-10-08', '2021-10-09');

## 1.9 好友关系表

- 表结构
注：表中一行数据中的两个user_id，表示两个用户互为好友。

- 建表语句
hive>

DROP TABLE IF EXISTS friendship_info;

CREATE TABLE friendship_info(

`user1_id` string comment '用户1id',

`user2_id` string comment '用户2id'

) COMMENT '用户关系表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table friendship_info

values ('101', '1010'),

('101', '108'),

('101', '106'),

('101', '104'),

('101', '102'),

('102', '1010'),

('102', '108'),

('102', '106'),

('102', '104'),

('102', '102'),

('103', '1010'),

('103', '108'),

('103', '106'),

('103', '104'),

('103', '102'),

('104', '1010'),

('104', '108'),

('104', '106'),

('104', '104'),

('104', '102'),

('105', '1010'),

('105', '108'),

('105', '106'),

('105', '104'),

('105', '102'),

('106', '1010'),

('106', '108'),

('106', '106'),

('106', '104'),

('106', '102'),

('107', '1010'),

('107', '108'),

('107', '106'),

('107', '104'),

('107', '102'),

('108', '1010'),

('108', '108'),

('108', '106'),

('108', '104'),

('108', '102'),

('109', '1010'),

('109', '108'),

('109', '106'),

('109', '104'),

('109', '102'),

('1010', '1010'),

('1010', '108'),

('1010', '106'),

('1010', '104'),

('1010', '102');

## 1.10 收藏信息表

- 表结构
- 建表语句
hive>

DROP TABLE IF EXISTS favor_info;

CREATE TABLE favor_info

(

`user_id`     string comment '用户id',

`sku_id`      string comment '商品id',

`create_date` string comment '收藏日期'

) COMMENT '用户收藏表'

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

- 数据装载
hive>

insert overwrite table favor_info

values ('101', '3', '2021-09-23'),

('101', '12', '2021-09-23'),

('101', '6', '2021-09-25'),

('101', '10', '2021-09-21'),

('101', '5', '2021-09-25'),

('102', '1', '2021-09-24'),

('102', '2', '2021-09-24'),

('102', '8', '2021-09-23'),

('102', '12', '2021-09-22'),

('102', '11', '2021-09-23'),

('102', '9', '2021-09-25'),

('102', '4', '2021-09-25'),

('102', '6', '2021-09-23'),

('102', '7', '2021-09-26'),

('103', '8', '2021-09-24'),

('103', '5', '2021-09-25'),

('103', '6', '2021-09-26'),

('103', '12', '2021-09-27'),

('103', '7', '2021-09-25'),

('103', '10', '2021-09-25'),

('103', '4', '2021-09-24'),

('103', '11', '2021-09-25'),

('103', '3', '2021-09-27'),

('104', '9', '2021-09-28'),

('104', '7', '2021-09-28'),

('104', '8', '2021-09-25'),

('104', '3', '2021-09-28'),

('104', '11', '2021-09-25'),

('104', '6', '2021-09-25'),

('104', '12', '2021-09-28'),

('105', '8', '2021-10-08'),

('105', '9', '2021-10-07'),

('105', '7', '2021-10-07'),

('105', '11', '2021-10-06'),

('105', '5', '2021-10-07'),

('105', '4', '2021-10-05'),

('105', '10', '2021-10-07'),

('106', '12', '2021-10-08'),

('106', '1', '2021-10-08'),

('106', '4', '2021-10-04'),

('106', '5', '2021-10-08'),

('106', '2', '2021-10-04'),

('106', '6', '2021-10-04'),

('106', '7', '2021-10-08'),

('107', '5', '2021-09-29'),

('107', '3', '2021-09-28'),

('107', '10', '2021-09-27'),

('108', '9', '2021-10-08'),

('108', '3', '2021-10-10'),

('108', '8', '2021-10-10'),

('108', '10', '2021-10-07'),

('108', '11', '2021-10-07'),

('109', '2', '2021-09-27'),

('109', '4', '2021-09-29'),

('109', '5', '2021-09-29'),

('109', '9', '2021-09-30'),

('109', '8', '2021-09-26'),

('1010', '2', '2021-09-29'),

('1010', '9', '2021-09-29'),

('1010', '1', '2021-10-01');

# 2 练习题

## 2.1 [课堂讲解]查询累积销量排名第二的商品

### 2.1.1 题目需求

查询订单明细表（order_detail）中销量（下单件数）排名第二的商品id，如果不存在返回null，如果存在多个排名第二的商品则需要全部返回。期望结果如下：

### 2.1.2 代码实现

hive>

select sku_id

from (

select sku_id

from (

select sku_id,

order_num,

dense_rank() over (order by order_num desc) rk

from (

select sku_id,

sum(sku_num) order_num

from order_detail

group by sku_id

) t1

) t2

where rk = 2

) t3

right join --为保证，没有第二名的情况下，返回null

(

select 1

) t4

on 1 = 1;

## 2.2 [课堂讲解]查询至少连续三天下单的用户

### 2.2.1 题目需求

查询订单信息表(order_info)中最少连续3天下单的用户id，期望结果如下：

### 2.2.2 代码实现

hive>

select distinct user_id

from (

select user_id

from (

select user_id

, create_date

, date_sub(create_date, row_number() over (partition by user_id order by create_date)) flag

from (

select user_id

, create_date

from order_info

group by user_id, create_date

) t1 -- 同一天可能多个用户下单，进行去重

) t2 -- 判断一串日期是否连续：若连续，用这个日期减去它的排名，会得到一个相同的结果

group by user_id, flag

having count(flag) >= 3 -- 连续下单大于等于三天

) t3;

## 2.3 [课堂讲解]查询各品类销售商品的种类数及销量最高的商品

### 2.3.1 题目需求

从订单明细表(order_detail)统计各品类销售出的商品种类数及累积销量最好的商品，期望结果如下：

### 2.3.2 代码实现

hive>

select category_id,

category_name,

sku_id,

name,

order_num,

sku_cnt

from (

select od.sku_id,

sku.name,

sku.category_id,

cate.category_name,

order_num,

rank() over (partition by sku.category_id order by order_num desc) rk,

count(distinct od.sku_id) over (partition by sku.category_id)      sku_cnt

from (

select sku_id,

sum(sku_num) order_num

from order_detail

group by sku_id

) od

left join

sku_info sku

on od.sku_id = sku.sku_id

left join

category_info cate

on sku.category_id = cate.category_id

) t1

where rk = 1;

## 2.4 [课堂讲解]查询用户的累计消费金额及VIP等级

### 2.4.1 题目需求

从订单信息表(order_info)中统计每个用户截止其每个下单日期的累积消费金额，以及每个用户在其每个下单日期的VIP等级。

用户vip等级根据累积消费金额计算，计算规则如下：

设累积消费总额为X，

若0=<X<10000,则vip等级为普通会员

若10000<=X<30000,则vip等级为青铜会员

若30000<=X<50000,则vip等级为白银会员

若50000<=X<80000,则vip为黄金会员

若80000<=X<100000,则vip等级为白金会员

若X>=100000,则vip等级为钻石会员

期望结果如下：

### 2.4.2 代码实现

hive>

select user_id,

create_date,

sum_so_far,

case

when sum_so_far >= 100000 then '钻石会员'

when sum_so_far >= 80000 then '白金会员'

when sum_so_far >= 50000 then '黄金会员'

when sum_so_far >= 30000 then '白银会员'

when sum_so_far >= 10000 then '青铜会员'

when sum_so_far >= 0 then '普通会员'

end vip_level

from (

select user_id,

create_date,

sum(total_amount_per_day) over (partition by user_id order by create_date) sum_so_far

from (

select user_id,

create_date,

sum(total_amount) total_amount_per_day

from order_info

group by user_id, create_date

) t1

) t2;

## 2.5 [课堂讲解]查询首次下单后第二天连续下单的用户比率

### 2.5.1 题目需求

从订单信息表(order_info)中查询首次下单后第二天仍然下单的用户占所有下单用户的比例，结果保留一位小数，使用百分数显示，期望结果如下：

### 2.5.2 代码实现

hive>

select concat(round(sum(if(datediff(buy_date_second, buy_date_first) = 1, 1, 0)) / count(*) * 100, 1), '%') percentage

from (

select user_id,

min(create_date) buy_date_first,

max(create_date) buy_date_second

from (

select user_id,

create_date,

rank() over (partition by user_id order by create_date) rk

from (

select user_id,

create_date

from order_info

group by user_id, create_date

) t1

) t2

where rk <= 2

group by user_id

) t3;

## 2.6 每个商品销售首年的年份、销售数量和销售金额

### 2.6.1 题目需求

从订单明细表(order_detail)统计每个商品销售首年的年份，销售数量和销售总额。

期望结果如下：

### 2.6.2 代码实现

hive>

select sku_id,

year(create_date),

sum(sku_num),

sum(price*sku_num)

from (

select order_id,

sku_id,

price,

sku_num,

create_date,

rank() over (partition by sku_id order by year(create_date)) rk

from order_detail

) t1

where rk = 1

group by sku_id,year(create_date);

## 2.7 筛选去年总销量小于100的商品

### 2.7.1 题目需求

从订单明细表(order_detail)中筛选出去年总销量小于100的商品及其销量，假设今天的日期是2022-01-10，不考虑上架时间小于一个月的商品，期望结果如下：

### 2.7.2 代码实现

hive>

select t1.sku_id,

name,

order_num

from (

select sku_id,

sum(sku_num) order_num

from order_detail

where year(create_date) = '2021'

and sku_id in (

select sku_id

from sku_info

where datediff('2022-01-10', from_date) > 30

)

group by sku_id

having sum(sku_num) < 100

) t1

left join

sku_info t2

on t1.sku_id = t2.sku_id;

## 2.8 查询每日新用户数

### 2.8.1 题目需求

从用户登录明细表（user_login_detail）中查询每天的新增用户数，若一个用户在某天登录了，且在这一天之前没登录过，则任务该用户为这一天的新增用户。期望结果如下：

### 2.8.2 代码实现

hive>

select

login_date_first,

count(*) user_count

from

(

select

user_id,

min(date_format(login_ts,'yyyy-MM-dd')) login_date_first

from user_login_detail

group by user_id

)t1

group by login_date_first;

## 2.9 统计每个商品的销量最高的日期

### 2.9.1 题目需求

从订单明细表（order_detail）中统计出每种商品销售件数最多的日期及当日销量，如果有同一商品多日销量并列的情况，取其中的最小日期。期望结果如下：

### 2.9.2 代码实现

hive>

select sku_id,

create_date,

sum_num

from (

select sku_id,

create_date,

sum_num,

row_number() over (partition by sku_id order by sum_num desc,create_date asc) rn

from (

select sku_id,

create_date,

sum(sku_num) sum_num

from order_detail

group by sku_id, create_date

) t1

) t2

where rn = 1;

## 2.10 查询销售件数高于品类平均数的商品

### 2.10.1 题目需求

从订单明细表（order_detail）中查询累积销售件数高于其所属品类平均数的商品，期望结果如下：

### 2.10.2 代码实现

hive>

select sku_id,

name,

sum_num,

cate_avg_num

from (

select od.sku_id,

category_id,

name,

sum_num,

avg(sum_num) over (partition by category_id) cate_avg_num

from (

select sku_id,

sum(sku_num) sum_num

from order_detail

group by sku_id

) od

left join

(

select sku_id,

name,

category_id

from sku_info

) sku

on od.sku_id = sku.sku_id) t1

where sum_num > cate_avg_num;

## 2.11 用户注册、登录、下单综合统计

### 2.11.1 题目需求

从用户登录明细表（user_login_detail）和订单信息表（order_info）中查询每个用户的注册日期（首次登录日期）、总登录次数以及其在2021年的登录次数、订单数和订单总额。期望结果如下：

### 2.11.2 代码实现

hive>

select login.user_id,

register_date,

total_login_count,

login_count_2021,

order_count_2021,

order_amount_2021

from (

select user_id,

min(date_format(login_ts, 'yyyy-MM-dd'))    register_date,

count(1)                                    total_login_count,

count(if(year(login_ts) = '2021', 1, null)) login_count_2021

from user_login_detail

group by user_id

) login

join

(

select user_id,

count(distinct(order_id))          order_count_2021,

sum(total_amount) order_amount_2021

from order_info

where year(create_date) = '2021'

group by user_id

) oi

on login.user_id = oi.user_id;

## 2.12 查询指定日期的全部商品价格

### 2.12.1 题目需求

从商品价格修改明细表（sku_price_modify_detail）中查询2021-10-01的全部商品的价格，假设所有商品初始价格默认都是99。期望结果如下：

### 2.12.2 代码实现

hive>

select sku_info.sku_id,

nvl(new_price, 99) price

from sku_info

left join

(

select sku_id,

new_price

from (

select sku_id,

new_price,

change_date,

row_number() over (partition by sku_id order by change_date desc) rn

from sku_price_modify_detail

where change_date <= '2021-10-01'

) t1

where rn = 1

) t2

on sku_info.sku_id = t2.sku_id;

## 2.13 即时订单比例

### 2.13.1 题目需求

订单配送中，如果期望配送日期和下单日期相同，称为即时订单，如果期望配送日期和下单日期不同，称为计划订单。

请从配送信息表（delivery_info）中求出每个用户的首单（用户的第一个订单）中即时订单的比例，保留两位小数，以小数形式显示。期望结果如下：

### 2.13.2 代码实现

hive>

select

round(sum(if(order_date=custom_date,1,0))/count(*),2) percentage

from

(

select

delivery_id,

user_id,

order_date,

custom_date,

row_number() over (partition by user_id order by order_date) rn

from delivery_info

)t1

where rn=1;

## 2.14 向用户推荐朋友收藏的商品

### 2.14.1 题目需求

现需要请向所有用户推荐其朋友收藏但是用户自己未收藏的商品，请从好友关系表（friendship_info）和收藏表（favor_info）中查询出应向哪位用户推荐哪些商品。期望结果如下：

- 部分结果展示
- 完整结果
user_idsku_id

1012

1014

1017

1019

1018

10111

1011

1023

1025

10210

1032

1031

1039

1041

1044

10410

1045

1042

1051

1052

1056

10512

1053

10611

10610

1068

1069

1063

10711

1077

1074

1079

10712

1071

1078

1076

1072

1082

1086

10812

1081

1087

1084

1085

1096

10910

1097

1091

10912

1093

10911

10104

101010

10106

101012

101011

10108

10103

10105

10107

### 2.14.2 代码实现

hive>

select

distinct t1.user_id,

friend_favor.sku_id

from

(

select

user1_id user_id,

user2_id friend_id

from friendship_info

union

select

user2_id,

user1_id

from friendship_info

)t1

left join favor_info friend_favor

on t1.friend_id=friend_favor.user_id

left join favor_info user_favor

on t1.user_id=user_favor.user_id

and friend_favor.sku_id=user_favor.sku_id

where user_favor.sku_id is null;

## 2.15 查询所有用户的连续登录两天及以上的日期区间

### 2.15.1 题目需求

从登录明细表（user_login_detail）中查询出，所有用户的连续登录两天及以上的日期区间，以登录时间（login_ts）为准。期望结果如下：

### 2.15.2 代码实现

hive>

select user_id,

min(login_date) start_date,

max(login_date) end_date

from (

select user_id,

login_date,

date_sub(login_date, rn) flag

from (

select user_id,

login_date,

row_number() over (partition by user_id order by login_date) rn

from (

select user_id,

date_format(login_ts, 'yyyy-MM-dd') login_date

from user_login_detail

group by user_id, date_format(login_ts, 'yyyy-MM-dd')

) t1

) t2

) t3

group by user_id, flag

having count(*) >= 2;

## 2.16 男性和女性每日的购物总金额统计

### 2.16.1 题目需求

从订单信息表（order_info）和用户信息表（user_info）中，分别统计每天男性和女性用户的订单总金额，如果当天男性或者女性没有购物，则统计结果为0。期望结果如下：

### 2.16.2 代码实现

hive>

select create_date,

sum(if(gender = '男', total_amount, 0)) total_amount_male,

sum(if(gender = '女', total_amount, 0)) total_amount_female

from order_info oi

left join

user_info ui

on oi.user_id = ui.user_id

group by create_date;

## 2.17 订单金额趋势分析

### 2.17.1 题目需求

查询截止每天的最近3天内的订单金额总和以及订单金额日平均值，保留两位小数，四舍五入。期望结果如下：

### 2.17.2 代码实现

hive>

select create_date,

round(sum(total_amount_by_day) over (order by create_date rows between 2 preceding and current row ),2) total_3d,

round(avg(total_amount_by_day) over (order by create_date rows between 2 preceding and current row ), 2) avg_3d

from (

select create_date,

sum(total_amount) total_amount_by_day

from order_info

group by create_date

) t1;

## 2.18 购买过商品1和商品2但是没有购买商品3的顾客

### 2.18.1 题目需求

从订单明细表(order_detail)中查询出所有购买过商品1和商品2，但是没有购买过商品3的用户，期望结果如下：

### 2.18.2 代码实现

hive>

select user_id

from (

select user_id,

collect_set(sku_id) skus

from order_detail od

left join

order_info oi

on od.order_id = oi.order_id

group by user_id

) t1

where array_contains(skus, '1')

and array_contains(skus, '2')

and !array_contains(skus, '3');

## 2.19 统计每日商品1和商品2销量的差值

### 2.19.1 题目需求

从订单明细表（order_detail）中统计每天商品1和商品2销量（件数）的差值（商品1销量-商品2销量），期望结果如下：

### 2.19.2 代码实现

hive>

select create_date,

sum(if(sku_id = '1', sku_num, 0)) - sum(if(sku_id = '2', sku_num, 0)) diff

from order_detail

where sku_id in ('1', '2')

group by create_date;

## 2.20 查询出每个用户的最近三笔订单

### 2.20.1 题目需求

从订单信息表（order_info）中查询出每个用户的最近三笔订单，期望结果如下：

### 2.20.2 代码实现

hive>

select user_id,

order_id,

create_date

from (

select user_id

, order_id

, create_date

, row_number() over (partition by user_id order by create_date desc) rk

from order_info

) t1

where rk <= 3;

## 2.21 查询每个用户登录日期的最大空档期

### 2.21.1 题目需求

从登录明细表（user_login_detail）中查询每个用户两个登录日期（以login_ts为准）之间的最大的空档期。统计最大空档期时，用户最后一次登录至今的空档也要考虑在内，假设今天为2021-10-10。期望结果如下：

### 2.21.2 代码实现

hive>

select

user_id,

max(diff) max_diff

from

(

select

user_id,

datediff(next_login_date,login_date) diff

from

(

select

user_id,

login_date,

lead(login_date,1,'2021-10-10') over(partition by user_id order by login_date) next_login_date

from

(

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date

from user_login_detail

group by user_id,date_format(login_ts,'yyyy-MM-dd')

)t1

)t2

)t3

group by user_id;

## 2.22 查询相同时刻多地登陆的用户

### 2.22.1 题目需求

从登录明细表（user_login_detail）中查询在相同时刻，多地登陆（ip_address不同）的用户，期望结果如下：

### 2.22.2 代码实现

hive>

select

distinct t2.user_id

from

(

select

t1.user_id,

if(t1.max_logout is null ,2,if(t1.max_logout<t1.login_ts,1,0)) flag

from

(

select

user_id,

login_ts,

logout_ts,

max(logout_ts)over(partition by user_id order by login_ts rows between unbounded preceding and 1 preceding) max_logout

from

user_login_detail

)t1

)t2

where

t2.flag=0

## 2.23 销售额完成任务指标的商品

### 2.23.1 题目需求

商家要求每个商品每个月需要售卖出一定的销售总额

假设1号商品销售总额大于21000，2号商品销售总额大于10000，其余商品没有要求

请写出SQL从订单详情表中（order_detail）查询连续两个月销售总额大于等于任务总额的商品

结果如下：

### 2.23.2 代码实现及步骤

hive>

-- 求出1号商品  和  2号商品 每个月的购买总额 并过滤掉没有满足指标的商品

select

sku_id,

concat(substring(create_date,0,7),'-01') ymd,

sum(price*sku_num)  sku_sum

from

order_detail

where

sku_id=1 or sku_id=2

group by

sku_id,substring(create_date,0,7)

having

(sku_id=1 and sku_sum>=21000) or (sku_id=2 and sku_sum>=10000)

-- 判断是否为连续两个月

select

distinct t3.sku_id

from

(

select

t2.sku_id,

count(*)over(partition by t2.sku_id,t2.rymd) cn

from

(

select

t1.sku_id,

add_months(t1.ymd,-row_number()over(partition by t1.sku_id order by t1.ymd)) rymd

from

(

select

sku_id,

concat(substring(create_date,0,7),'-01') ymd,

sum(price*sku_num)  sku_sum

from

order_detail

where

sku_id=1 or sku_id=2

group by

sku_id,substring(create_date,0,7)

having

(sku_id=1 and sku_sum>=21000) or (sku_id=2 and sku_sum>=10000)

)t1

)t2

)t3

where

t3.cn>=2

## 2.24 根据商品销售情况进行商品分类

### 2.24.1 题目需求

从订单详情表中（order_detail）对销售件数对商品进行分类，0-5000为冷门商品，5001-19999位一般商品，20000往上为热门商品，并求出不同类别商品的数量

结果如下：

### 2.24.2 代码实现

hive>

select

t2.category,

count(*) cn

from

(

select

t1.sku_id,

case

when  t1.sku_sum >=0 and t1.sku_sum<=5000 then '冷门商品'

when  t1.sku_sum >=5001 and t1.sku_sum<=19999 then '一般商品'

when  t1.sku_sum >=20000 then '热门商品'

end  category

from

(

select

sku_id,

sum(sku_num)  sku_sum

from

order_detail

group by

sku_id

)t1

)t2

group by

t2.category

## 2.25 各品类销量前三的所有商品

### 2.25.1 题目需求

从订单详情表中（order_detail）和商品（sku_info）中查询各个品类销售数量前三的商品。如果该品类小于三个商品，则输出所有的商品销量。

结果如下：

### 2.25.2 代码实现

hive>

select

t2.sku_id,

t2.category_id

from

(

select

t1.sku_id,

si.category_id,

rank()over(partition by category_id order by t1.sku_sum desc) rk

from

(

select

sku_id,

sum(sku_num) sku_sum

from

order_detail

group by

sku_id

)t1

join

sku_info si

on

t1.sku_id=si.sku_id

)t2

where

t2.rk<=3;

## 2.26 各品类中商品价格的中位数

### 2.26.1 题目需求

从商品（sku_info）中球中位数如果是偶数则输出中间两个值的平均值，如果是奇数，则输出中间数即可。

结果如下：

### 2.26.2 代码实现

hive>

--求个每个品类 价格排序 商品数量 以及打上奇偶数的标签

select

sku_id,

category_id,

price,

row_number()over(partition by category_id order by price desc) rk,

count(*)over(partition by category_id) cn,

count(*)over(partition by category_id)%2 falg

from

sku_info  t1

--求出偶数品类的中位数

select

distinct t1.category_id,

avg(t1.price)over(partition by t1.category_id) medprice

from

(

select

sku_id,

category_id,

price,

row_number()over(partition by category_id order by price desc) rk,

count(*)over(partition by category_id) cn,

count(*)over(partition by category_id)%2 falg

from

sku_info

)t1

where

t1.falg=0 and (t1.rk=cn/2  or t1.rk=cn/2+1)

--求出奇数品类的中位数

select

t1.category_id,

t1.price

from

(

select

sku_id,

category_id,

price,

row_number()over(partition by category_id order by price desc) rk,

count(*)over(partition by category_id) cn,

count(*)over(partition by category_id)%2 falg

from

sku_info

)t1

where

t1.falg=1 and t1.rk=round(cn/2)

-- 竖向拼接

select

distinct t1.category_id,

avg(t1.price)over(partition by t1.category_id) medprice

from

(

select

sku_id,

category_id,

price,

row_number()over(partition by category_id order by price desc) rk,

count(*)over(partition by category_id) cn,

count(*)over(partition by category_id)%2 falg

from

sku_info

)t1

where

t1.falg=0 and (t1.rk=cn/2  or t1.rk=cn/2+1)

union

select

t1.category_id,

t1.price/1

from

(

select

sku_id,

category_id,

price,

row_number()over(partition by category_id order by price desc) rk,

count(*)over(partition by category_id) cn,

count(*)over(partition by category_id)%2 falg

from

sku_info

)t1

where

t1.falg=1 and t1.rk=round(cn/2)

## 2.27 找出销售额连续3天超过100的商品

### 2.27.1 题目需求

从订单详情表（order_detail）中找出销售额连续3天超过100的商品

结果如下：

### 2.27.2 代码实现

hive>

-- 每个商品每天的销售总额

select

sku_id,

create_date,

sum(price*sku_num) sku_sum

from

order_detail

group by

sku_id,create_date

having

sku_sum>=100

--  判断连续三天以上

select

distinct t3.sku_id

from

(

select

t2.sku_id,

count(*)over(partition by t2.sku_id,t2.date_drk) cdrk

from

(

select

t1.sku_id,

t1.create_date,

date_sub(t1.create_date,rank()over(partition by t1.sku_id order by t1.create_date)) date_drk

from

(

select

sku_id,

create_date,

sum(price*sku_num) sku_sum

from

order_detail

group by

sku_id,create_date

having

sku_sum>=100

)t1

)t2

)t3

where

t3.cdrk>=3

## 2.28 查询有新注册用户的当天的新用户数量、新用户的第一天留存率

### 2.28.1 题目需求

从用户登录明细表（user_login_detail）中首次登录算作当天新增，第二天也登录了算作一日留存

结果如下：

### 2.28.2 代码实现

hive>

-- 每个用户首次登录时间 和 第二天是否登录 并看每天新增和留存数量

select

t1.first_login,

count(t1.user_id) register,

count(t2.user_id) remain_1

from

(

select

user_id,

date_format(min(login_ts),'yyyy-MM-dd')   first_login

from

user_login_detail

group by

user_id

)t1

left join

user_login_detail t2

on

t1.user_id=t2.user_id and datediff(date_format(t2.login_ts,'yyyy-MM-dd'),t1.first_login)=1

group by

t1.first_login

-- 新增数量和留存率

select

t3.first_login,

t3.register,

t3.remain_1/t3.register retention

from

(

select

t1.first_login,

count(t1.user_id) register,

count(t2.user_id) remain_1

from

(

select

user_id,

date_format(min(login_ts),'yyyy-MM-dd')   first_login

from

user_login_detail

group by

user_id

)t1

left join

user_login_detail t2

on

t1.user_id=t2.user_id and datediff(date_format(t2.login_ts,'yyyy-MM-dd'),t1.first_login)=1

group by

t1.first_login

)t3

## 2.29 求出商品连续售卖的时间区间

### 2.29.1 题目需求

从订单详情表（order_detail）中，求出商品连续售卖的时间区间

结果如下（截取部分）：

### 2.29.2 代码实现

hive>

-- 每个商品售卖的日期以及拿到按排序后日期的差值

select

sku_id,

create_date,

date_sub(create_date,rank()over(partition by sku_id order by create_date)) ddrk

from

order_detail

group by

sku_id,create_date

-- 拿到每次售卖的区间

select

distinct

sku_id,

first_value(t1.create_date)over(partition by t1.sku_id,t1.ddrk order by t1.create_date  rows between unbounded preceding and unbounded following) start_date,

last_value(t1.create_date)over(partition by t1.sku_id,t1.ddrk order by t1.create_date  rows between unbounded preceding and unbounded following) end_date

from

(

select

sku_id,

create_date,

date_sub(create_date,rank()over(partition by sku_id order by create_date)) ddrk

from

order_detail

group by

sku_id,create_date

)t1

## 2.30 登录次数及交易次数统计

### 2.30.1 题目需求

分别从登陆明细表（user_login_detail）和配送信息表中用户登录时间和下单时间统计登陆次数和交易次数

结果如下（截取部分）：

### 2.30.2 代码实现

hive>

-- 拿到每个用户每天的登录次数

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date,

count(*) login_count

from

user_login_detail

group by

user_id,date_format(login_ts,'yyyy-MM-dd')

-- 拿到每个用户每天的交易次数

select

t1.user_id,

t1.login_date,

collect_set(t1.login_count)[0] login_count ,

count(di.user_id) order_count

from

(

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date,

count(*) login_count

from

user_login_detail

group by

user_id,date_format(login_ts,'yyyy-MM-dd')

)t1

left join

delivery_info di

on

t1.user_id=di.user_id and t1.login_date=di.order_date

group by

t1.user_id,t1.login_date

## 2.31 按年度列出每个商品销售总额

### 2.31.1 题目需求

从订单明细表（order_detail）中列出每个商品每个年度的购买总额

结果如下（截取部分）：

### 2.31.2 代码实现

hive>

select

sku_id,

year(create_date) year_date,

sum(price*sku_num) sku_sum

from

order_detail

group by

sku_id,year(create_date)

## 2.32 2.32. 某周内每件商品每天销售情况

### 2.32.1 题目需求

从订单详情表（order_detail）中查询2021年9月27号-2021年10月3号这一周所有商品每天销售情况。

结果如下：

### 2.32.2 代码实现

hive>

select

sku_id,

sum(if(dayofweek(create_date)=2,sku_num,0)) Monday,

sum(if(dayofweek(create_date)=3,sku_num,0)) Tuesday,

sum(if(dayofweek(create_date)=4,sku_num,0)) Wednesday,

sum(if(dayofweek(create_date)=5,sku_num,0)) Thursday,

sum(if(dayofweek(create_date)=6,sku_num,0)) Friday,

sum(if(dayofweek(create_date)=7,sku_num,0)) Saturday,

sum(if(dayofweek(create_date)=1,sku_num,0)) Sunday

from

order_detail

where

create_date>='2021-09-27' and create_date<='2021-10-03'

group by

sku_id

## 2.33 查看每件商品的售价涨幅情况

### 2.33.1 题目需求

从商品价格变更明细表（sku_price_modify_detail），得到最近一次价格的涨幅情况，并按照涨幅升序排序。

结果如下：

### 2.33.2 代码实现

hive>

-- 对每个商品按照修改日期倒序排序 并求出差值

select

sku_id,

new_price-lead(new_price,1,0)over(partition by sku_id order by change_date desc) price_change,

rank()over(partition by sku_id order by change_date desc) rk

from

sku_price_modify_detail   t1

-- 最近一次修改的价格

select

t1.sku_id,

t1.price_change

from

(

select

sku_id,

new_price-lead(new_price,1,0)over(partition by sku_id order by change_date desc) price_change,

rank()over(partition by sku_id order by change_date desc) rk

from

sku_price_modify_detail

)t1

where

rk=1

order by

t1.price_change

## 2.34 销售订单首购和次购分析

### 2.34.1 题目需求

通过商品信息表（sku_info）订单信息表（order_info）订单明细表（order_detail）分析如果有一个用户成功下单两个及两个以上的购买成功的手机订单（购买商品为xiaomi 10，apple 12，小米13）那么输出这个用户的id及第一次成功购买手机的日期和第二次成功购买手机的日期，以及购买手机成功的次数。

结果如下：

### 2.34.2 代码实现

hive>

select

distinct oi.user_id,

first_value(od.create_date)over(partition by oi.user_id order by od.create_date rows between unbounded preceding and unbounded following ) first_date,

last_value(od.create_date)over(partition by oi.user_id order by od.create_date rows between unbounded preceding and unbounded following ) last_date,

count(*)over(partition by oi.user_id order by od.create_date rows between unbounded preceding and unbounded following) cn

from

order_info oi

join

order_detail od

on

oi.order_id=od.order_id

join

sku_info si

on

od.sku_id=si.sku_id

where

si.name in('xiaomi 10','apple 12','xiaomi 13')

## 2.35 同期商品售卖分析表

### 2.35.1 题目需求

从订单明细表（order_detail）中。

求出同一个商品在2021年和2022年中同一个月的售卖情况对比。

结果如下（截取部分）：

### 2.35.2 代码实现

hive>

select

if(t1.sku_id is null,t2.sku_id,t1.sku_id),

month(if(t1.ym is null,t2.ym,t1.ym)) ,

if(t1.sku_sum is null ,0 ,t1.sku_sum) 2020_skusum,

if(t2.sku_sum is null ,0 ,t2.sku_sum) 2020_skusum

from

(

select

sku_id,

concat(date_format(create_date,'yyyy-MM'),'-01') ym,

sum(sku_num) sku_sum

from

order_detail

where

year(create_date)=2020

group by

sku_id,date_format(create_date,'yyyy-MM')

)t1

full join

(

select

sku_id,

concat(date_format(create_date,'yyyy-MM'),'-01')  ym,

sum(sku_num) sku_sum

from

order_detail

where

year(create_date)=2021

group by

sku_id,date_format(create_date,'yyyy-MM')

)t2

on

t1.sku_id=t2.sku_id and month(t1.ym) = month(t2.ym)

## 2.36 国庆期间每个品类的商品的收藏量和购买量

### 2.36.1 题目需求

从订单明细表（order_detail）和收藏信息表（favor_info）统计2021国庆期间，每个商品总收藏量和购买量

结果如下：

### 2.36.2 代码实现

hive>

select

t1.sku_id,

t1.sku_sum,

t2.favor_cn

from

(

select

sku_id,

sum(sku_num) sku_sum

from

order_detail

where

create_date>='2021-10-01' and create_date<='2021-10-07'

group by

sku_id

)t1

join

(

select

sku_id,

count(*) favor_cn

from

favor_info

where

create_date>='2021-10-01' and create_date<='2021-10-07'

group by

sku_id

)t2

on

t1.sku_id=t2.sku_id

## 2.37 统计活跃间隔对用户分级结果

### 2.37.1 题目需求

用户等级：

忠实用户：近7天活跃且非新用户

新晋用户：近7天新增

沉睡用户：近7天未活跃但是在7天前活跃

流失用户：近30天未活跃但是在30天前活跃

假设今天是数据中所有日期的最大值，从用户登录明细表中的用户登录时间给各用户分级，求出各等级用户的人数

结果如下：

### 2.37.2 代码实现

hive>

select

t2.level,

count(*)

from

(

select

uld.user_id,

case

when (date_format(max(uld.login_ts),'yyyy-MM-dd') <=date_sub(today, 30))

then '流失用户'-- 最近登录时间三十天前

when (date_format(min(uld.login_ts),'yyyy-MM-dd') <=date_sub(today, 7) and date_format(max(uld.login_ts),'yyyy-MM-dd') >=date_sub(today, 7))

then '忠实用户' -- 最早登陆时间是七天前,并且最近七天登录过

when (date_format(min(uld.login_ts),'yyyy-MM-dd') >=date_sub(today, 7))

then '新增用户' -- 最早登录时间是七天内

when (date_format(min(uld.login_ts),'yyyy-MM-dd') <= date_sub(today, 7) and date_format(max(uld.login_ts),'yyyy-MM-dd') <= date_sub(today, 7))

then '沉睡用户'-- 最早登陆时间是七天前,最大登录时间也是七天前

end level

from

user_login_detail  uld

join

(

select

date_format(max(login_ts),'yyyy-MM-dd') today

from

user_login_detail

)t1

on

1=1

group by

uld.user_id,t1.today

)t2

group by

t2.level

## 2.38 连续签到领金币数

### 2.38.1 题目需求

用户每天签到可以领1金币，并可以累计签到天数，连续签到的第3、7天分别可以额外领2和6金币。

每连续签到7天重新累积签到天数。

从用户登录明细表中求出每个用户金币总数，并按照金币总数倒序排序

结果如下：

### 2.38.2 代码实现

hive>

-- 求连续并标志是连续的第几天

select

t1.user_id,

t1.login_date,

date_sub(t1.login_date,t1.rk) login_date_rk,

count(*)over(partition by t1.user_id, date_sub(t1.login_date,t1.rk) order by t1.login_date) counti_cn

from

(

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date,

rank()over(partition by user_id order by date_format(login_ts,'yyyy-MM-dd')) rk

from

user_login_detail

group by

user_id,date_format(login_ts,'yyyy-MM-dd')

)t1

--求出金币数量，以及签到奖励的金币数量

select

t2.user_id,

max(t2.counti_cn)+sum(if(t2.counti_cn%3=0,2,0))+sum(if(t2.counti_cn%7=0,6,0)) coin_cn

from

(

select

t1.user_id,

t1.login_date,

date_sub(t1.login_date,t1.rk) login_date_rk,

count(*)over(partition by t1.user_id, date_sub(t1.login_date,t1.rk) order by t1.login_date) counti_cn

from

(

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date,

rank()over(partition by user_id order by date_format(login_ts,'yyyy-MM-dd')) rk

from

user_login_detail

group by

user_id,date_format(login_ts,'yyyy-MM-dd')

)t1

)t2

group by

t2.user_id,t2.login_date_rk

-- 求出每个用户的金币总数

select

t3.user_id,

sum(t3.coin_cn) sum_coin_cn

from

(

select

t2.user_id,

max(t2.counti_cn)+sum(if(t2.counti_cn%3=0,2,0))+sum(if(t2.counti_cn%7=0,6,0)) coin_cn

from

(

select

t1.user_id,

t1.login_date,

date_sub(t1.login_date,t1.rk) login_date_rk,

count(*)over(partition by t1.user_id, date_sub(t1.login_date,t1.rk) order by t1.login_date) counti_cn

from

(

select

user_id,

date_format(login_ts,'yyyy-MM-dd') login_date,

rank()over(partition by user_id order by date_format(login_ts,'yyyy-MM-dd')) rk

from

user_login_detail

group by

user_id,date_format(login_ts,'yyyy-MM-dd')

)t1

)t2

group by

t2.user_id,t2.login_date_rk

)t3

group by

t3.user_id

order by

sum_coin_cn desc

## 2.39 国庆期间的7日动销率和滞销率

### 2.39.1 题目需求

动销率定义为品类商品中一段时间内有销量的商品占当前已上架总商品数的比例（有销量的商品/已上架总商品数）。

滞销率定义为品类商品中一段时间内没有销量的商品占当前已上架总商品数的比例。（没有销量的商品 / 已上架总商品数）。

只要当天任一店铺有任何商品的销量就输出该天的结果

从订单明细表（order_detail）和商品信息表（sku_info）表中求出国庆7天每天每个品类的商品的动销率和滞销率

结果如下（截取部分）：

### 2.39.2 代码实现

hive>

-- 国庆每一天 每个商品品类有多少商品被销售了

select

t1.category_id,

sum(if(t1.create_date='2021-10-01',1,0)) `第1天`,

sum(if(t1.create_date='2021-10-02',1,0)) `第2天`,

sum(if(t1.create_date='2021-10-03',1,0)) `第3天`,

sum(if(t1.create_date='2021-10-04',1,0)) `第4天`,

sum(if(t1.create_date='2021-10-05',1,0)) `第5天`,

sum(if(t1.create_date='2021-10-06',1,0)) `第6天`,

sum(if(t1.create_date='2021-10-07',1,0)) `第7天`

from

(

select

distinct

si.category_id,

od.create_date,

si.name

from

order_detail od

join

sku_info si

on

od.sku_id=si.sku_id

where

od.create_date>='2021-10-01' and od.create_date<='2021-10-07'

)t1

group by

t1.category_id

-- 每一天的动销率 和 滞销率

select

t2.category_id,

t2.`第1天`/t3.cn,

1-t2.`第1天`/t3.cn,

t2.`第2天`/t3.cn,

1-t2.`第2天`/t3.cn,

t2.`第3天`/t3.cn,

1-t2.`第3天`/t3.cn,

t2.`第4天`/t3.cn,

1-t2.`第4天`/t3.cn,

t2.`第5天`/t3.cn,

1-t2.`第5天`/t3.cn,

t2.`第6天`/t3.cn,

1-t2.`第6天`/t3.cn,

t2.`第7天`/t3.cn,

1-t2.`第7天`/t3.cn

from

(

select

t1.category_id,

sum(if(t1.create_date='2021-10-01',1,0)) `第1天`,

sum(if(t1.create_date='2021-10-02',1,0)) `第2天`,

sum(if(t1.create_date='2021-10-03',1,0)) `第3天`,

sum(if(t1.create_date='2021-10-04',1,0)) `第4天`,

sum(if(t1.create_date='2021-10-05',1,0)) `第5天`,

sum(if(t1.create_date='2021-10-06',1,0)) `第6天`,

sum(if(t1.create_date='2021-10-07',1,0)) `第7天`

from

(

select

distinct

si.category_id,

od.create_date,

si.name

from

order_detail od

join

sku_info si

on

od.sku_id=si.sku_id

where

od.create_date>='2021-10-01' and od.create_date<='2021-10-07'

)t1

group by

t1.category_id

)t2

join

(

select

category_id,

count(*) cn

from

sku_info

group by

category_id

)t3

on

t2.category_id=t3.category_id

## 2.40 同时在线最多的人数

### 2.40.1 题目需求

根据用户登录明细表（user_login_detail），求出平台同时在线最多的人数。

结果如下：

### 2.40.2 代码实现

hive>

-- 登录标记1 下线标记-1

select

login_ts l_time,

1 flag

from

user_login_detail

union

select

logout_ts l_time,

-1 flag

from

user_login_detail

-- 按照时间求和

select

sum(flag)over(order by t1.l_time) sum_l_time

from

(

select

login_ts l_time,

1 flag

from

user_login_detail

union

select

logout_ts l_time,

-1 flag

from

user_login_detail

)t1

-- 拿到最大值 就是同时在线最多人数

select

max(sum_l_time)

from

(

select

sum(flag)over(order by t1.l_time) sum_l_time

from

(

select

login_ts l_time,

1 flag

from

user_login_detail

union

select

logout_ts l_time,

-1 flag

from

user_login_detail

)t1

)t2
