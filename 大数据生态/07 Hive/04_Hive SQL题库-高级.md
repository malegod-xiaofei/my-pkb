尚硅谷大数据技术之Hive SQL题库-高级

（作者：尚硅谷研究院）

版本：V1.0

# 1 第 1 题 同时在线人数问题

## 1.1 题目需求

现有各直播间的用户访问记录表（live_events）如下，表中每行数据表达的信息为，一个用户何时进入了一个直播间，又在何时离开了该直播间。

现要求统计各直播间最大同时在线人数，期望结果如下：

## 1.2 数据准备

- 建表语句
drop table if exists live_events;

create table if not exists live_events

(

user_id      int comment '用户id',

live_id      int comment '直播id',

in_datetime  string comment '进入直播间时间',

out_datetime string comment '离开直播间时间'

)

comment '直播间访问记录';

- 数据装载
INSERT overwrite table live_events

VALUES (100, 1, '2021-12-01 19:00:00', '2021-12-01 19:28:00'),

(100, 1, '2021-12-01 19:30:00', '2021-12-01 19:53:00'),

(100, 2, '2021-12-01 21:01:00', '2021-12-01 22:00:00'),

(101, 1, '2021-12-01 19:05:00', '2021-12-01 20:55:00'),

(101, 2, '2021-12-01 21:05:00', '2021-12-01 21:58:00'),

(102, 1, '2021-12-01 19:10:00', '2021-12-01 19:25:00'),

(102, 2, '2021-12-01 19:55:00', '2021-12-01 21:00:00'),

(102, 3, '2021-12-01 21:05:00', '2021-12-01 22:05:00'),

(104, 1, '2021-12-01 19:00:00', '2021-12-01 20:59:00'),

(104, 2, '2021-12-01 21:57:00', '2021-12-01 22:56:00'),

(105, 2, '2021-12-01 19:10:00', '2021-12-01 19:18:00'),

(106, 3, '2021-12-01 19:01:00', '2021-12-01 21:10:00');

## 1.3 代码实现

select

live_id,

max(user_count) max_user_count

from

(

select

user_id,

live_id,

sum(user_change) over(partition by live_id order by event_time) user_count

from

(

select user_id,

live_id,

in_datetime event_time,

1 user_change

from live_events

union all

select user_id,

live_id,

out_datetime,

-1

from live_events

)t1

)t2

group by live_id;

# 2 第 2 题 会话划分问题

## 2.1 题目需求

现有页面浏览记录表（page_view_events）如下，表中有每个用户的每次页面访问记录。

规定若同一用户的相邻两次访问记录时间间隔小于60s，则认为两次浏览记录属于同一会话。现有如下需求，为属于同一会话的访问记录增加一个相同的会话id字段，期望结果如下：

## 2.2 数据准备

- 建表语句
drop table if exists page_view_events;

create table if not exists page_view_events

(

user_id        int comment '用户id',

page_id        string comment '页面id',

view_timestamp bigint comment '访问时间戳'

)

comment '页面访问记录';

- 数据装载
insert overwrite table page_view_events

values (100, 'home', 1659950435),

(100, 'good_search', 1659950446),

(100, 'good_list', 1659950457),

(100, 'home', 1659950541),

(100, 'good_detail', 1659950552),

(100, 'cart', 1659950563),

(101, 'home', 1659950435),

(101, 'good_search', 1659950446),

(101, 'good_list', 1659950457),

(101, 'home', 1659950541),

(101, 'good_detail', 1659950552),

(101, 'cart', 1659950563),

(102, 'home', 1659950435),

(102, 'good_search', 1659950446),

(102, 'good_list', 1659950457),

(103, 'home', 1659950541),

(103, 'good_detail', 1659950552),

(103, 'cart', 1659950563);

## 2.3 代码实现

select user_id,

page_id,

view_timestamp,

concat(user_id, '-', sum(session_start_point) over (partition by user_id order by view_timestamp)) session_id

from (

select user_id,

page_id,

view_timestamp,

if(view_timestamp - lagts >= 60, 1, 0) session_start_point

from (

select user_id,

page_id,

view_timestamp,

lag(view_timestamp, 1, 0) over (partition by user_id order by view_timestamp) lagts

from page_view_events

) t1

) t2;

# 3 第 3 题 间断连续登录用户问题

## 3.1 题目需求

现有各用户的登录记录表（login_events）如下，表中每行数据表达的信息是一个用户何时登录了平台。

现要求统计各用户最长的连续登录天数，间断一天也算作连续，例如：一个用户在1,3,5,6登录，则视为连续6天登录。期望结果如下：

## 3.2 数据准备

- 建表语句
drop table if exists login_events;

create table if not exists login_events

(

user_id        int comment '用户id',

login_datetime string comment '登录时间'

)

comment '直播间访问记录';

- 数据装载
INSERT overwrite table login_events

VALUES (100, '2021-12-01 19:00:00'),

(100, '2021-12-01 19:30:00'),

(100, '2021-12-02 21:01:00'),

(100, '2021-12-03 11:01:00'),

(101, '2021-12-01 19:05:00'),

(101, '2021-12-01 21:05:00'),

(101, '2021-12-03 21:05:00'),

(101, '2021-12-05 15:05:00'),

(101, '2021-12-06 19:05:00'),

(102, '2021-12-01 19:55:00'),

(102, '2021-12-01 21:05:00'),

(102, '2021-12-02 21:57:00'),

(102, '2021-12-03 19:10:00'),

(104, '2021-12-04 21:57:00'),

(104, '2021-12-02 22:57:00'),

(105, '2021-12-01 10:01:00');

## 3.3 代码实现

select

user_id,

max(recent_days) max_recent_days  --求出每个用户最大的连续天数

from

(

select

user_id,

user_flag,

datediff(max(login_date),min(login_date)) + 1 recent_days --按照分组求每个用户每次连续的天数(记得加1)

from

(

select

user_id,

login_date,

lag1_date,

concat(user_id,'_',flag) user_flag --拼接用户和标签分组

from

(

select

user_id,

login_date,

lag1_date,

sum(if(datediff(login_date,lag1_date)>2,1,0)) over(partition by user_id order by login_date) flag  --获取大于2的标签

from

(

select

user_id,

login_date,

lag(login_date,1,'1970-01-01') over(partition by user_id order by login_date) lag1_date  --获取上一次登录日期

from

(

select

user_id,

date_format(login_datetime,'yyyy-MM-dd') login_date

from login_events

group by user_id,date_format(login_datetime,'yyyy-MM-dd')  --按照用户和日期去重

)t1

)t2

)t3

)t4

group by user_id,user_flag

)t5

group by user_id;

# 4 第 4 题 日期交叉问题

## 4.1 题目需求

现有各品牌优惠周期表（promotion_info）如下，其记录了每个品牌的每个优惠活动的周期，其中同一品牌的不同优惠活动的周期可能会有交叉。

现要求统计每个品牌的优惠总天数，若某个品牌在同一天有多个优惠活动，则只按一天计算。期望结果如下：

## 4.2 数据准备

- 建表语句
drop table if exists promotion_info;

create table promotion_info

(

promotion_id string comment '优惠活动id',

brand        string comment '优惠品牌',

start_date   string comment '优惠活动开始日期',

end_date     string comment '优惠活动结束日期'

) comment '各品牌活动周期表';

- 数据装载
insert overwrite table promotion_info

values (1, 'oppo', '2021-06-05', '2021-06-09'),

(2, 'oppo', '2021-06-11', '2021-06-21'),

(3, 'vivo', '2021-06-05', '2021-06-15'),

(4, 'vivo', '2021-06-09', '2021-06-21'),

(5, 'redmi', '2021-06-05', '2021-06-21'),

(6, 'redmi', '2021-06-09', '2021-06-15'),

(7, 'redmi', '2021-06-17', '2021-06-26'),

(8, 'huawei', '2021-06-05', '2021-06-26'),

(9, 'huawei', '2021-06-09', '2021-06-15'),

(10, 'huawei', '2021-06-17', '2021-06-21');

## 4.3 代码实现

select

brand,

sum(datediff(end_date,start_date)+1) promotion_day_count

from

(

select

brand,

max_end_date,

if(max_end_date is null or start_date>max_end_date,start_date,date_add(max_end_date,1)) start_date,

end_date

from

(

select

brand,

start_date,

end_date,

max(end_date) over(partition by brand order by start_date rows between unbounded preceding and 1 preceding) max_end_date

from promotion_info

)t1

)t2

where end_date>start_date

group by brand;
