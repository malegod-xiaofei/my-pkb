Jar包执行脚本

#!/bin/sh

```text
# args
```

input=$1

in_charset=$2

user_out=$3

content_out=$4

out_charset=$5

sep=$6

```bash
# run java jar xxx.jar 6args
java -jar ../udf/weibo.jar $input $in_charset $user_out $content_out $out_charset $sep
```

建表脚本 :

- wb_user
#!/bin/sh

db=$1

tb_name=$2

sep=$3

hive -e "USE $db;

```sql
CREATE TABLE IF NOT EXISTS $tb_name(
```

uid string,

screen_name string,

name string,

province string,

city string,

location string,

remark string)

ROW FORMAT DELIMITED

FIELDS TERMINATED BY \"$sep\"

STORED AS TEXTFILE;"

- wb_content
#!/bin/sh

db=$1

tb_name=$2

sep=$3

hive -e "USE $db;

```sql
CREATE TABLE IF NOT EXISTS $tb_name(
```

uid string,

content string,

dt_time string,

repost_cnt int,

comment_cnt int)

ROW FORMAT DELIMITED

FIELDS TERMINATED BY \"$sep\"

STORED AS TEXTFILE;"

上传数据文件到HDFS上

#!/bin/sh

local_path=$1

hdfs_path=$2

hdfs dfs -put $local_path $hdfs_path

Hive加载数据到数据库表中

#!/bin/sh

db=$1

data_path=$2

tb_name=$3

hive -e "USE $db;

LOAD DATA INPATH \"$data_path\" OVERWRITE INTO TABLE $tb_name;"

Main执行总流程:

#!/bin/sh

```properties
# var define
```

in_data=$1

in_char=$2

out_path=$3

user_file=$4

content_file=$5

o_char=$6

sep=$7

hdfs_data_dir=$8

db=$9

tb_user=${10}

tb_content=${11}

```text
# 1. product data
```

echo '++++++start product data++++++'

sh ../deal/product_data.sh $in_data $in_char $out_path/$user_file $out_path/$content_file $o_char $sep

echo '++++++end product data++++++'

```text
# 2. put local to hdfs
```

echo '++++++start put local to hdfs++++++'

sh ../deal/put_file_2_hdfs.sh $out_path/$user_file $hdfs_data_dir

sh ../deal/put_file_2_hdfs.sh $out_path/$content_file $hdfs_data_dir

echo '++++++end put local 2 hdfs++++++'

```sql
# 3. create table
```

echo '++++++start create table ++++++'

sh ../create/create_content.sh $db $tb_content $sep

sh ../create/create_user.sh $db $tb_user $sep

echo '++++++end create table++++++'

```text
# 4. load data
```

echo '++++++start load data++++++'

sh ../deal/load_data_2_table.sh $db $hdfs_data_dir/$user_file $tb_user

sh ../deal/load_data_2_table.sh $db $hdfs_data_dir/$content_file $tb_content

echo '++++++end load data++++++'

脚本调用语句 :

sh main.sh ../data/input 'gbk' ../data/output 'user.txt' 'content.txt' 'utf8' \\001 /tmp/zyf zyf wb_user wb_content

知识点 :

重定向输出到(黑洞) à > /dev/null 2>&1

脚本编写当中$符号的使用

赋值的时候不加

取值的时候必加

echo “20120102.csv” | cut -d . -f1 20120102

保证shell在断开客户端的情况下，依然可以继续执行

nohup : 不挂断的永久执行

& : 在后台运行，当用户会话退出时候，命令自动也跟着退出

事实的监控文件的变化 : tail -10f file_path

查看文件夹中的文件个数 ： ls | wc -l
