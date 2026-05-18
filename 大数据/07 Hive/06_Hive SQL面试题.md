尚硅谷大数据技术之Hive面试题

(作者：尚硅谷研究院)

版本  2.0

# 1 第 1 题 连续问题

如下数据为蚂蚁森林中用户领取的减少碳排放量

id dt lowcarbon

1001 2021-12-12 123

1002 2021-12-12 45

1001 2021-12-13 43

1001 2021-12-13 45

1001 2021-12-13 23

1002 2021-12-14 45

1001 2021-12-14 230

1002 2021-12-15 45

1001 2021-12-15 23

找出连续3天及以上减少碳排放量在100以上的用户

1)按照用户ID及时间字段分组,计算每个用户单日减少的碳排放量

select

id,

dt,

sum(lowcarbon) lowcarbon

from test1

group by id,dt

having lowcarbon>100;t1

10012021-12-12123

10012021-12-13111

10012021-12-14230

等差数列法:两个等差数列如果等差相同,则相同位置的数据相减等到的结果相同

2)按照用户分组,同时按照时间排序,计算每条数据的Rank值

select

id,

dt,

lowcarbon,

rank() over(partition by id order by dt) rk

from t1;t2

3)将每行数据中的日期减去Rank值

select

id,

dt,

lowcarbon,

date_sub(dt,rk) flag

from t2;t3

4)按照用户及Flag分组,求每个组有多少条数据,并找出大于等于3条的数据

select

id,

flag,

count(*) ct

from t3

group by id,flag

having ct>=3;

5)最终HQL

select

id,

flag,

count(*) ct

from

(select

id,

dt,

lowcarbon,

date_sub(dt,rk) flag

from

(select

id,

dt,

lowcarbon,

rank() over(partition by id order by dt) rk

from

(select

id,

dt,

sum(lowcarbon) lowcarbon

from test1

group by id,dt

having lowcarbon>100)t1)t2)t3

group by id,flag

having ct>=3;

# 2 第 2 题 分组问题

如下为电商公司用户访问时间数据

id ts(秒)

1001 17523641234

1001 17523641256

1002 17523641278

1001 17523641334

1002 17523641434

1001 17523641534

1001 17523641544

1002 17523641634

1001 17523641638

1001 17523641654

某个用户连续的访问记录如果时间间隔小于60秒，则分为同一个组，结果为：

id ts(秒) group

1001 17523641234 1

1001 17523641256 1

1001 17523641334 2

1001 17523641534 3

1001 17523641544 3

1001 17523641638 4

1001 17523641654 4

1002 17523641278 1

1002 17523641434 2

1002 17523641634 3

1)将上一行时间数据下移

lead:领导

lag:延迟

select

id,

ts,

lag(ts,1,0) over(partition by id order by ts) lagts

from

test2;t1

1001175236412340

10011752364125617523641234

10011752364133417523641256

10011752364153417523641334

10011752364154417523641534

10011752364163817523641544

10011752364165417523641638

1002175236412780

10021752364143417523641278

10021752364163417523641434

2)将当前行时间数据减去上一行时间数据

select

id,

ts,

ts-lagts tsdiff

from

t1;t2

select

id,

ts,

ts-lagts tsdiff

from

(select

id,

ts,

lag(ts,1,0) over(partition by id order by ts) lagts

from

test2)t1;t2

10011752364123417523641234

10011752364125622

10011752364133478

100117523641534200

10011752364154410

10011752364163894

10011752364165416

10021752364127817523641278

100217523641434156

100217523641634200

3)计算每个用户范围内从第一行到当前行tsdiff大于等于60的总个数(分组号)

select

id,

ts,

sum(if(tsdiff>=60,1,0)) over(partition by id order by ts) groupid

from

t2;

4)最终HQL

select

id,

ts,

sum(if(tsdiff>=60,1,0)) over(partition by id order by ts) groupid

from

(select

id,

ts,

ts-lagts tsdiff

from

(select

id,

ts,

lag(ts,1,0) over(partition by id order by ts) lagts

from

test2)t1)t2;

# 3 第 3 题 间隔连续问题

某游戏公司记录的用户每日登录数据

id dt

1001 2021-12-12

1002 2021-12-12

1001 2021-12-13

1001 2021-12-14

1001 2021-12-16

1002 2021-12-16

1001 2021-12-19

1002 2021-12-17

1001 2021-12-20

计算每个用户最大的连续登录天数，可以间隔一天。解释：如果一个用户在 1,3,5,6 登录游戏，则视为连续6天登录。

思路一：等差数列

10012021-12-121

10012021-12-132

10012021-12-143

10012021-12-164

10012021-12-195

10012021-12-206

10012021-12-1212021-12-11

10012021-12-1322021-12-11

10012021-12-1432021-12-11

10012021-12-1642021-12-12

10012021-12-1952021-12-14

10012021-12-2062021-12-14

10012021-12-113

10012021-12-121

10012021-12-141

10012021-12-1131

10012021-12-1212

10012021-12-1413

10012021-12-11312021-12-10

10012021-12-12122021-12-10

10012021-12-14132021-12-11

思路二：分组

10012021-12-12

10012021-12-13

10012021-12-14

10012021-12-16

10012021-12-19

10012021-12-20

1)将上一行时间数据下移

10012021-12-121970-01-01

10012021-12-132021-12-12

10012021-12-142021-12-13

10012021-12-162021-12-14

10012021-12-192021-12-16

10012021-12-202021-12-19

select

id,

dt,

lag(dt,1,'1970-01-01') over(partition by id order by dt) lagdt

from

test3;t1

2)将当前行时间减去上一行时间数据(datediff(dt1,dt2))

10012021-12-12564564

10012021-12-131

10012021-12-141

10012021-12-162

10012021-12-193

10012021-12-201

select

id,

dt,

datediff(dt,lagdt) flag

from

t1;t2

3)按照用户分组,同时按照时间排序,计算从第一行到当前行大于2的数据的总条数(sum(if(flag>2,1,0)))

10012021-12-121

10012021-12-131

10012021-12-141

10012021-12-161

10012021-12-192

10012021-12-202

select

id,

dt,

sum(if(flag>2,1,0)) over(partition by id order by dt) flag

from

t2;t3

4)按照用户和flag分组,求最大时间减去最小时间并加上1

select

id,

flag,

datediff(max(dt),min(dt)) days

from

t3

group by id,flag;t4

5)取连续登录天数的最大值

select

id,

max(days)+1

from

t4

group by id;

6)最终HQL

select

id,

max(days)+1

from

(select

id,

flag,

datediff(max(dt),min(dt)) days

from

(select

id,

dt,

sum(if(flag>2,1,0)) over(partition by id order by dt) flag

from

(select

id,

dt,

datediff(dt,lagdt) flag

from

(select

id,

dt,

lag(dt,1,'1970-01-01') over(partition by id order by dt) lagdt

from

test3)t1)t2)t3

group by id,flag)t4

group by id;

# 4 第 4 题 打折日期交叉问题

如下为平台商品促销数据：字段为品牌，打折开始日期，打折结束日期

brand stt edt

oppo 2021-06-05  2021-06-09

oppo 2021-06-11  2021-06-21

vivo 2021-06-05  2021-06-15

vivo 2021-06-09  2021-06-21

redmi 2021-06-05  2021-06-21

redmi 2021-06-09  2021-06-15

redmi 2021-06-17  2021-06-26

huawei  2021-06-05  2021-06-26

huawei  2021-06-09  2021-06-15

huawei  2021-06-17  2021-06-21

计算每个品牌总的打折销售天数，注意其中的交叉日期，比如vivo品牌，第一次活动时间为2021-06-05到2021-06-15，第二次活动时间为2021-06-09到2021-06-21其中9号到15号为重复天数，只统计一次，即vivo总打折天数为2021-06-05到2021-06-21共计17天。

1)将当前行以前的数据中最大的edt放置当前行

select

id,

stt,

edt,

max(edt) over(partition by id order by stt rows between UNBOUNDED PRECEDING and 1 PRECEDING) maxEdt

from test4;t1

redmi2021-06-052021-06-21null

redmi2021-06-092021-06-152021-06-21

redmi2021-06-172021-06-262021-06-21

2)比较开始时间与移动下来的数据,如果开始时间大,则不需要操作,

反之则需要将移动下来的数据加一替换当前行的开始时间

如果是第一行数据,maxEDT为null,则不需要操作

select

id,

if(maxEdt is null,stt,if(stt>maxEdt,stt,date_add(maxEdt,1))) stt,

edt

from t1;t2

redmi2021-06-052021-06-21

redmi2021-06-222021-06-15

redmi2021-06-222021-06-26

3)将每行数据中的结束日期减去开始日期

select

id,

datediff(edt,stt) days

from

t2;t3

redmi16

redmi-4

redmi4

4)按照品牌分组,计算每条数据加一的总和

select

id,

sum(if(days>=0,days+1,0)) days

from

t3

group by id;

redmi22

5)最终HQL

select

id,

sum(if(days>=0,days+1,0)) days

from

(select

id,

datediff(edt,stt) days

from

(select

id,

if(maxEdt is null,stt,if(stt>maxEdt,stt,date_add(maxEdt,1))) stt,

edt

from

(select

id,

stt,

edt,

max(edt) over(partition by id order by stt rows between UNBOUNDED PRECEDING and 1 PRECEDING) maxEdt

from test4)t1)t2)t3

group by id;

# 5 第 5 题 同时在线问题

如下为某直播平台主播开播及关播时间，根据该数据计算出平台最高峰同时在线的主播人数。

id stt edt

1001 2021-06-14 12:12:12 2021-06-14 18:12:12

1003 2021-06-14 13:12:12 2021-06-14 16:12:12

1004 2021-06-14 13:15:12 2021-06-14 20:12:12

1002 2021-06-14 15:12:12 2021-06-14 16:12:12

1005 2021-06-14 15:18:12 2021-06-14 20:12:12

1001 2021-06-14 20:12:12 2021-06-14 23:12:12

1006 2021-06-14 21:12:12 2021-06-14 23:15:12

1007 2021-06-14 22:12:12 2021-06-14 23:10:12

流式！

1)对数据分类,在开始数据后添加正1,表示有主播上线,同时在关播数据后添加-1,表示有主播下线

select id,stt dt,1 p from test5

union

select id,edt dt,-1 p from test5;t1

10012021-06-14 12:12:121

10012021-06-14 18:12:12-1

10012021-06-14 20:12:121

10012021-06-14 23:12:12-1

10022021-06-14 15:12:121

10022021-06-14 16:12:12-1

10032021-06-14 13:12:121

10032021-06-14 16:12:12-1

10042021-06-14 13:15:121

10042021-06-14 20:12:12-1

10052021-06-14 15:18:121

10052021-06-14 20:12:12-1

10062021-06-14 21:12:121

10062021-06-14 23:15:12-1

10072021-06-14 22:12:121

10072021-06-14 23:10:12-1

2)按照时间排序,计算累加人数

select

id,

dt,

sum(p) over(order by dt) sum_p

from

(select id,stt dt,1 p from test5

union

select id,edt dt,-1 p from test5)t1;t2

3)找出同时在线人数最大值

select

max(sum_p)

from

(select

id,

dt,

sum(p) over(order by dt) sum_p

from

(select id,stt dt,1 p from test5

union

select id,edt dt,-1 p from test5)t1)t2;
