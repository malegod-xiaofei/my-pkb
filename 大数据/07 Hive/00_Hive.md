- Hive是什么
  - desc 查看表结构
- 数据仓库是什么?数仓和数据库有什么区别?
  - 联系:
    - 数据库和数仓都是用来存储数据的
    - 数仓是数据库的衍生物
    - 数据库和数仓之间也有数据上的交互,数据库里的数据也会发送给数仓,然后再由数仓进行分析,而分析完成的结果也会发送给数据库,
  - 区别:
    - 数据库是面向事务,数仓是面向主题
    - 数据库的设计是为了避免数据冗余,而数仓是需要数据冗余 ER模型设计,三范式
    - 数据库的数据都是实时数据,实时性强, 数仓的数据都是历史数据,实时性弱,因为需要分析,需要时间
    - 数据库的数据存储量小,数仓的数据存储量大
    - 数据库里的数据可以修改,数仓里的数据不可以被修改
- 三范式
  - 第一范式 -- 原子行
  - 第二范式 -- 主键
  - 第三范式 -- 避免出现依赖传递
- 特点:冗余，数仓希望通过冗余来避免JOIN
  - // id name sex clsno clsname score
  - 1 jack M c01 语文 90
  - 1 jack M c02 数学 80
  - 1 jack M c03 外语 88
- 第1范式--原子性 第2范式--主健 第3范式--避免依赖传递
  - 优点:避免冗余
  - 缺点:需要join关联
  - // id name sex
  - 1 jackM
  - // clsno clsname score sid
  - c01 语文 90 1
  - c02 数学 80 1
  - c03 外语 88 1
# 3.Hive saql

## 3.1 DDL

### 3.1.1 create --创建分区表，分桶表，创建一个带复杂数据类型的表

查看表创建的详细信息: 表结构、表数据文件路径等

```java
show create table table_name;
```

- 普通表
```java
create table if not exists student_01 (id int comment 'id', name string comment 'student name') comment 'use to describe student info' row format delimited stored as textfile;
```

```java
insert into student_01 values (1, 'jack'), (2, 'marry');
```

- 分区表
```java
create table if not exists student_part

(id int comment 'id', name string comment 'student name')

comment 'use to describe student info'

partitioned by (month_date string comment 'partitioned by month_date')

row format delimited

stored as textfile;
```

```java
insert into table student_part partition(month_date='202011') select * from student;
```

- 分桶表
```java
create table if not exists student_bucket

(id int comment 'id', name string comment 'student name')

comment 'student bucket table'

clustered by (id) sorted by (id, name) into 4 buckets

row format delimited

stored as textfile;
```

```java
insert into student_bucket values

(1, 'jack'),(2, 'marry'),(3, 'john'),(4, 'tom'),(5, 'lily'),(6, 'hanmeimei'),(7, 'lihua'),

(1, 'jack'),(2, 'marry'),(3, 'john'),(4, 'tom'),(5, 'lily'),(6, 'hanmeimei'),(7, 'lihua');
```

  - 复杂数据类型的普通表
  - 复杂类型的Array字段
```java
create table student_arr (id int, name string, hobbits array<string>);
```

```java
insert into student_arr values (1, 'zs', array('basket','football','pingpong'));
```

```java
select id, name, hobbits[0] from student_arr;
```

  - 复杂类型的Map字段
```java
create table student_map (id int, name string,scores map<string, decimal(3,1)>);
```

```java
insert into student_map values (1, 'li4', map('yw',80.5,'sx',88.5));
```

```java
select id, name, scores['yw'] from student_map;
```

  - 复杂类型的Strcut字 段
```java
create table student_struct (id int, info struct<name:string,sex:string,age:double>);
```

```java
insert into student_struct values (1, named_struct('name','zs','sex','F','age',cast(22.0 as double)));
```

```java
select id, info.name, info.sex, info.age from student_struct;
```

### 3.1.2 drop--一笔带过

```java
drop table table_name
```

### 3.1.3 alter -—新增分区表的分区

```java
alter table ...
```

```java
alter table student_part add partition(month_date='202009');
```

```java
alter table student_part drop partition(month_date='202009');
```

```java
// 查看分区情况 show partitions student_part;
```

## 3.2 DML

### 3.2.1 insert -- insert into --它会触发计算, 指定分区表进行导入数据

load data .... --不会触发计算, 指定分区表进行导入数据

```java
// 1.插入的时候，不会覆盖原来的数据

insert into table table_name select * from table_name1;

// 2.插入的时候，会覆盖原来的数据

insert overwrite table table_name select * from table_name1;

// 3.导入hdfs数据文件到表中

create table student_load (id int, name string, sex string) row format delimited fields terminated by '\t' stored as textfile;

load data inpath '/tmp/student_load.txt' overwrite into table student_load;
```

:%s/四个空格/制表符/g

```java
// 4. 导入hdfs数据文件到复杂类型的表中

// 4.1 array

create table student_arr_1 (id int, name string, hobbits array<string>) row format delimited fields terminated by '\t' collection items terminated by ',' stored as textfile;

// 4.2 map

create table student_map_1 (id int, name string, scores map<string,double>) row format delimited fields terminated by '\t' collection items terminated by ',' map keys terminated by ':' stored as textfile;

// 4.3 struct

create table student_struct_1 (id int, info struct<name:string,sex:string,age:int>) row format delimited fields terminated by '\t' collection items terminated by ',' stored as textfile;
```

remove -- truncate table table_name -―删除表数据

```java
// 没有delete, update
```

## 3.3 DQL

如何向分区表插入数据(开启动态分区)？

演示如何向分桶表插入数据(load data会触发分桶计算吗)?

如何查看分区数据 如何查看分桶数据

## 3.4自带的系统函数

### 3.4.1自定义系统函数

- 新建Maven
- 导入Hive依赖包
```java
<dependency> <groupId>org.apache.hive</groupId> <artifactId>hive-cli</artifactId> <version>1.2.1</version> <scope>provided</scope> </dependency>
```

- 创建一个类，继承UDF
```java
public class StrMaskUDF extends UDF{ }
```

- 重写evaluate方法
```java
public String evaluate(String str, int len, String replaceStr) { if(str == null || str.trim().length() == 0) { return null; } if(str.length() >= len) { return str.substring(0, len) + replaceStr; } else { return str; } }
```

- 打包上传
```java
mvn package
```

- hive中add jar加载jar包
```java
hive > add jar /xxxxx/yyy.jar
```

- 创建hive函数模板去关联jar包中的自定义UDF类
```java
create temporary function func_name as 'xxx.xxx.xxx.自定义的UDF子类';
```

- 使用hive自定义函数
```java
select func_name(....)
```

上传到自己的hive下:

```java
add jar
```

添加到自定义的方法区:

```java
create temporary function mysk as 'cn.hive.lianxi._01_md5';
```

执行自定义方法:

```java
select mysk('asdasdasd');
```

```java
add jar
```

@全体成员 上传jar的时候，由于大家不是hive用户，注意一下：

- jar包上传到hdfs上
- add jar
- 参考以上例子
1.Hive介绍:

Hive概念: 数据仓库和数据库的区别?

OLTP和OLAP的概念?

2.Hive运行流程

User Interface : Hive Cli | Hive Client | HWI

Hive : Meta Data Driver 做SQL解析 HiveServer2

Hadoop Core : 计算

3.系统函数

聚合函数,字符串操作函数,日期函数,later view ,explode,case ... when,if ,colasece

4.自定义函数

UDF -- 开发步骤,源码

UDAF--开发步骤,源码

5.仓库设计分层

源数据层 -- 数据细节层 -- 数据汇总层 -- 数据集市

6.仓库建模

星型模型,雪花模型,星座模型

ER模型

缓慢变化维 + 拉链表

7.Hive的分析函数

ntile,row_number,rank,dense_rank

lag,lead,first_value,last_value

sum(),count(),avg()

over(partition by ... order by... range between preceding unbounded and current row)加order和不加order默认范围不同

表数据构成

元数据 : metadata,描述数据的数据

实体数据 : entity data

8.hive内表和外表的区别 和联系

联系

元数据都归 Hive 管理

区别

内表的实体数据也归 Hive 管理, 只要删表实体数据也会消失

外表的实体数据不归 Hive 管理, 删表操作成功后,元数据一定会消失,但实体数据不受影响

Hive如何定义内表和外表

- external : 外部的
- create [external] table tableName ......
Hive创建表时候,如何来判定是内表还是外表

创建外表的使用场景 : 数据都是外部导入的,非自己生成的

创建外表的使用场景 : 数据都是外部导入的,非自己生成的

Hive数据表分类

普通表-非分区非分桶

不改变表结构,改变的是数据流向的问题

外区表 : 按照某个字段进行物理上的数据划分,常见的时间、国家,类别等等

以分区值作为hdfs的一个目录,该分区字段是虚字段

水平划分

核心诉求 : 提高查询效率

分桶表

按照某个字段就行物理上的数据划分

垂直划分,分文件来存储,是个实体字段

核心诉求 : 提高查询效率

查看所有的函数 : show function

hive之select, where, group by, order by 谁先谁后的问题

- select < where
- select < group by
- order by < select
- group by < where
- 总结出来 : where > group by > select > order by
