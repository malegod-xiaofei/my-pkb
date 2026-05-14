尚硅谷大数据技术之SparkCore

（作者：尚硅谷研究院）

版本：V5.0

# 1 RDD概述

## 1.1 什么是RDD

RDD（Resilient Distributed Dataset）叫做弹性分布式数据集，是Spark中最基本的数据抽象。

代码中是一个抽象类，它代表一个弹性的、不可变、可分区、里面的元素可并行计算的集合。

RDD类比工厂生产。

![图片18.png](images/图片18.png)

## 1.2 RDD五大特性

![图片19.png](images/图片19.png)

# 2 RDD编程

## 2.1 RDD的创建

在Spark中创建RDD的创建方式可以分为三种：从集合中创建RDD、从外部存储创建RDD、从其他RDD创建。

### 2.1.1 IDEA环境准备

- 创建一个maven工程，工程名称叫SparkCore
![图片20.png](images/图片20.png)

- 创建包名：com.atguigu.createrdd
- 在pom文件中添加spark-core的依赖
```xml
<dependencies>

<dependency>

<groupId>org.apache.spark</groupId>

<artifactId>spark-core_2.12</artifactId>

<version>3.3.1</version>

</dependency>

</dependencies>
```

- 如果不希望运行时打印大量日志，可以在resources文件夹中添加log4j2.properties文件，并添加日志配置信息
```

# Set everything to be logged to the console

rootLogger.level = ERROR

rootLogger.appenderRef.stdout.ref = console

# In the pattern layout configuration below, we specify an explicit `%ex` conversion

# pattern for logging Throwables. If this was omitted, then (by default) Log4J would

# implicitly add an `%xEx` conversion pattern which logs stacktraces with additional

# class packaging information. That extra information can sometimes add a substantial

# performance overhead, so we disable it in our default logging config.

# For more information, see SPARK-39361.

appender.console.type = Console

appender.console.name = console

appender.console.target = SYSTEM_ERR

appender.console.layout.type = PatternLayout

appender.console.layout.pattern = %d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n%ex

# Set the default spark-shell/spark-sql log level to WARN. When running the

# spark-shell/spark-sql, the log level for these classes is used to overwrite

# the root logger's log level, so that the user can have different defaults

# for the shell and regular Spark apps.

logger.repl.name = org.apache.spark.repl.Main

logger.repl.level = warn

logger.thriftserver.name = org.apache.spark.sql.hive.thriftserver.SparkSQLCLIDriver

logger.thriftserver.level = warn

# Settings to quiet third party logs that are too verbose

logger.jetty1.name = org.sparkproject.jetty

logger.jetty1.level = warn

logger.jetty2.name = org.sparkproject.jetty.util.component.AbstractLifeCycle

logger.jetty2.level = error

logger.replexprTyper.name = org.apache.spark.repl.SparkIMain$exprTyper

logger.replexprTyper.level = info

logger.replSparkILoopInterpreter.name = org.apache.spark.repl.SparkILoop$SparkILoopInterpreter

logger.replSparkILoopInterpreter.level = info

logger.parquet1.name = org.apache.parquet

logger.parquet1.level = error

logger.parquet2.name = parquet

logger.parquet2.level = error

# SPARK-9183: Settings to avoid annoying messages when looking up nonexistent UDFs in SparkSQL with Hive support

logger.RetryingHMSHandler.name = org.apache.hadoop.hive.metastore.RetryingHMSHandler

logger.RetryingHMSHandler.level = fatal

logger.FunctionRegistry.name = org.apache.hadoop.hive.ql.exec.FunctionRegistry

logger.FunctionRegistry.level = error

# For deploying Spark ThriftServer

# SPARK-34128: Suppress undesirable TTransportException warnings involved in THRIFT-4805

appender.console.filter.1.type = RegexFilter

appender.console.filter.1.regex = .*Thrift error occurred during processing of message.*

appender.console.filter.1.onMatch = deny appender.console.filter.1.onMismatch = neutral
```
### 2.1.2 创建IDEA快捷键

- 点击File->Settings…->Editor->Live Templates->output->Live Template
![图片21.png](images/图片21.png)

![图片22.png](images/图片22.png)

- 点击左下角的Define->选择JAVA
![图片23.png](images/图片23.png)

- 在Abbreviation中输入快捷键名称sc，在Template text中填写，输入快捷键后生成的内容。
![图片24.png](images/图片24.png)

```java
// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 4. 关闭sc

sc.stop();
```

### 2.1.3 异常处理

如果程序代码出现以下错误：

![图片25.png](images/图片25.png)

请采用资料中的hadoop环境。

如果本机操作系统是Windows，在程序中使用了Hadoop相关的东西，比如写入文件到HDFS，则会遇到如下异常：

![图片26.png](images/图片26.png)

出现这个问题的原因，并不是程序的错误，而是用到了Hadoop相关的服务，解决办法

- 配置HADOOP_HOME环境变量
- 在IDEA中配置Run Configuration，添加HADOOP_HOME变量
![图片27.png](images/图片27.png)

![图片28.png](images/图片28.png)

如果出现这个问题，是因为windows上面的hadoop权限不够。
```
Exception in thread "main" java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0(Ljava/lang/String;I)Z

at org.apache.hadoop.io.nativeio.NativeIO$Windows.access0(Native Method)

at org.apache.hadoop.io.nativeio.NativeIO$Windows.access(NativeIO.java:645)

at org.apache.hadoop.fs.FileUtil.canRead(FileUtil.java:1230)

at org.apache.hadoop.fs.FileUtil.list(FileUtil.java:1435)

at org.apache.hadoop.fs.RawLocalFileSystem.listStatus(RawLocalFileSystem.java:493)

at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1868)

at org.apache.hadoop.fs.FileSystem.listStatus(FileSystem.java:1910)

at org.apache.hadoop.fs.FileSystem$4.<init>(FileSystem.java:2072)
```
解决方法是把安装在windows上面的hadoop的bin文件夹中的hadoop.dll复制到C:\Windows\System32文件夹中。

![图片29.png](images/图片29.png)

![图片30.png](images/图片30.png)

### 2.1.4 从集合中创建

- 从集合中创建RDD：parallelize
```java
package com.atguigu.createrdd;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

import java.util.List;

public class Test01_List {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> stringRDD = sc.parallelize(Arrays.asList("hello", "spark"));

List<String> result = stringRDD.collect();

for (String s : result) {

System.out.println(s);

}

// 4. 关闭sc

sc.stop();

}

}
```
### 2.1.5 从外部存储系统的数据集创建

由外部存储系统的数据集创建RDD包括：本地的文件系统，还有所有Hadoop支持的数据集，比如HDFS、HBase等。

- 数据准备
在新建的SparkCore项目名称上右键=》新建input文件夹=》在input文件夹上右键=》分别新建1.txt和2.txt。每个文件里面准备一些word单词。

- 创建RDD
```java
package com.atguigu.createrdd;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.List;

public class Test02_File {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input");

List<String> result = lineRDD.collect();

for (String s : result) {

System.out.println(s);

}

// 4. 关闭sc

sc.stop();

}

}
```
### 2.1.6 从其他RDD创建

主要是通过一个RDD运算完后，再产生新的RDD。

详见2.3节

## 2.2 分区规则

### 2.2.1 从集合创建RDD

- 创建一个包名：com.atguigu.partition
- 代码验证
```java
package com.atguigu.partition;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

public class Test01_ListPartition {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 默认环境的核数

// 可以手动填写参数控制分区的个数

JavaRDD<String> stringRDD = sc.parallelize(Arrays.asList("hello", "spark", "hello", "spark", "hello"),2);

// 数据分区的情况

// 0 => 1,2  1 => 3,4,5

// 利用整数除机制  左闭右开

// 0 => start 0*5/2  end 1*5/2

// 1 => start 1*5/2  end 2*5/2

stringRDD.saveAsTextFile("output");

// 4. 关闭sc

sc.stop();

}

}
```
### 2.2.2 从文件创建RDD

- 分区测试
```java
package com.atguigu.partition;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.List;

public class Test02_FilePartition {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 默认填写的最小分区数   2和环境的核数取小的值  一般为2

JavaRDD<String> lineRDD = sc.textFile("input/1.txt");

// 具体的分区个数需要经过公式计算

// 首先获取文件的总长度  totalSize

// 计算平均长度  goalSize = totalSize / numSplits

// 获取块大小 128M

// 计算切分大小  splitSize = Math.max(minSize, Math.min(goalSize, blockSize));

// 最后使用splitSize  按照1.1倍原则切分整个文件   得到几个分区就是几个分区

// 实际开发中   只需要看文件总大小 / 填写的分区数  和块大小比较  谁小拿谁进行切分

lineRDD.saveAsTextFile("output");

// 数据会分配到哪个分区

// 如果切分的位置位于一行的中间  会在当前分区读完一整行数据

// 0 -> 1,2  1 -> 3  2 -> 4  3 -> 空

// 4. 关闭sc

sc.stop();

}

}
```
- 分区源码
注意：getSplits文件返回的是切片规划，真正读取是在compute方法中创建LineRecordReader读取的，有两个关键变量： start = split.getStart()   end = start + split.getLength

  - 分区数量的计算方式:
    - totalSize = 10
    - goalSize = 10 / 3 = 3(byte) 表示每个分区存储3字节的数据
    - 分区数= totalSize/ goalSize = 10 /3 => 3,3,4
    - 4子节大于3子节的1.1倍,符合hadoop切片1.1倍的策略,因此会多创建一个分区,即一共有4个分区  3,3,3,1
  - Spark读取文件，采用的是hadoop的方式读取，所以一行一行读取，跟字节数没有关系
  - 数据读取位置计算是以偏移量为单位来进行计算的。
## 2.3 Transformation转换算子

### 2.3.1 Value类型

- 创建包名：com.atguigu.value
#### 2.3.1.1 map()映射

参数f是一个函数可以写作匿名子类，它可以接收一个参数。当某个RDD执行map方法时，会遍历该RDD中的每一个数据项，并依次应用f函数，从而产生一个新的RDD。即，这个新RDD中的每一个元素都是原来RDD中每一个元素依次应用f函数而得到的。

- 具体实现
```java
package com.atguigu.value;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

public class Test01_Map {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/1.txt");

// 需求:每行结尾拼接||

// 两种写法  lambda表达式写法(匿名函数)

JavaRDD<String> mapRDD = lineRDD.map(s -> s + "||");

// 匿名函数写法

JavaRDD<String> mapRDD1 = lineRDD.map(new Function<String, String>() {

@Override

public String call(String v1) throws Exception {

return v1 + "||";

}

});

for (String s : mapRDD.collect()) {

System.out.println(s);

}

// 输出数据的函数写法

mapRDD1.collect().forEach(a -> System.out.println(a));

mapRDD1.collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
#### 2.3.1.2 flatMap()扁平化

- 功能说明
与map操作类似，将RDD中的每一个元素通过应用f函数依次转换为新的元素，并封装到RDD中。

区别：在flatMap操作中，f函数的返回值是一个集合，并且会将每一个该集合中的元素拆分出来放到新的RDD中。

- 需求说明：创建一个集合，集合里面存储的还是子集合，把所有子集合中数据取出放入到一个大的集合中。
![图片31.png](images/图片31.png)

- 具体实现：
```java
package com.atguigu.value;

import org.apache.commons.collections.ListUtils;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class Test02_FlatMap {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

ArrayList<List<String>> arrayLists = new ArrayList<>();

arrayLists.add(Arrays.asList("1","2","3"));

arrayLists.add(Arrays.asList("4","5","6"));

JavaRDD<List<String>> listJavaRDD = sc.parallelize(arrayLists,2);

// 对于集合嵌套的RDD 可以将元素打散

// 泛型为打散之后的元素类型

JavaRDD<String> stringJavaRDD = listJavaRDD.flatMap(new FlatMapFunction<List<String>, String>() {

@Override

public Iterator<String> call(List<String> strings) throws Exception {

return strings.iterator();

}

});

stringJavaRDD. collect().forEach(System.out::println);

// 通常情况下需要自己将元素转换为集合

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

JavaRDD<String> stringJavaRDD1 = lineRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

String[] s1 = s.split(" ");

return Arrays.asList(s1).iterator();

}

});

stringJavaRDD1. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
#### 2.3.1.3 groupBy()分组

- 功能说明：分组，按照传入函数的返回值进行分组。将相同的key对应的值放入一个迭代器。
- 需求说明：创建一个RDD，按照元素模以2的值进行分组。
- 具体实现
```java
package com.atguigu.value;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;

public class Test03_GroupBy {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

// 泛型为分组标记的类型

JavaPairRDD<Integer, Iterable<Integer>> groupByRDD = integerJavaRDD.groupBy(new Function<Integer, Integer>() {

@Override

public Integer call(Integer v1) throws Exception {

return v1 % 2;

}

});

groupByRDD.collect().forEach(System.out::println);

// 类型可以任意修改

JavaPairRDD<Boolean, Iterable<Integer>> groupByRDD1 = integerJavaRDD.groupBy(new Function<Integer, Boolean>() {

@Override

public Boolean call(Integer v1) throws Exception {

return v1 % 2 == 0;

}

});

groupByRDD1. collect().forEach(System.out::println);

Thread.sleep(600000);

// 4. 关闭sc

sc.stop();

}

}
```
- groupBy会存在shuffle过程
- shuffle：将不同的分区数据进行打乱重组的过程
- shuffle一定会落盘。可以在local模式下执行程序，通过4040看效果。
#### 2.3.1.4 filter()过滤

- 功能说明
接收一个返回值为布尔类型的函数作为参数。当某个RDD调用filter方法时，会对该RDD中每一个元素应用f函数，如果返回值类型为true，则该元素会被添加到新的RDD中。

- 需求说明：创建一个RDD，过滤出对2取余等于0的数据
![图片32.png](images/图片32.png)

- 代码实现
```java
package com.atguigu.value;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;

public class Test04_Filter {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

JavaRDD<Integer> filterRDD = integerJavaRDD.filter(new Function<Integer, Boolean>() {

@Override

public Boolean call(Integer v1) throws Exception {

return v1 % 2 == 0;

}

});

filterRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
#### 2.3.1.5 distinct()去重

- 功能说明：对内部的元素去重，并将去重后的元素放到新的RDD中。
- 代码实现
```java
package com.atguigu.value;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

public class Test05_Distinct {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4, 5, 6), 2);

// 底层使用分布式分组去重  所有速度比较慢,但是不会OOM

JavaRDD<Integer> distinct = integerJavaRDD.distinct();

distinct. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
注意：distinct会存在shuffle过程。

#### 2.3.1.6 sortBy()排序

- 功能说明
该操作用于排序数据。在排序之前，可以将数据通过f函数进行处理，之后按照f函数处理的结果进行排序，默认为正序排列。排序后新产生的RDD的分区数与原RDD的分区数一致。Spark的排序结果是全局有序。

- 需求说明：创建一个RDD，按照数字大小分别实现正序和倒序排序
![图片33.png](images/图片33.png)

- 代码实现：
```java
package com.atguigu.value;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;

public class Test6_SortBy {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(5, 8, 1, 11, 20), 2);

// (1)泛型为以谁作为标准排序  (2) true为正序  (3) 排序之后的分区个数

JavaRDD<Integer> sortByRDD = integerJavaRDD.sortBy(new Function<Integer, Integer>() {

@Override

public Integer call(Integer v1) throws Exception {

return v1;

}

}, true, 2);

sortByRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
### 2.3.2 Key-Value类型

- 创建包名：com.atguigu.keyvalue
要想使用Key-Value类型的算子首先需要使用特定的方法转换为PairRDD
``` java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

public class Test01_pairRDD{

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

JavaPairRDD<Integer, Integer> pairRDD = integerJavaRDD.mapToPair(new PairFunction<Integer, Integer, Integer>() {

@Override

public Tuple2<Integer, Integer> call(Integer integer) throws Exception {

return new Tuple2<>(integer, integer);

}

});

pairRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
#### 2.3.2.1 mapValues()只对V进行操作

- 功能说明：针对于(K,V)形式的类型只对V进行操作
- 需求说明：创建一个pairRDD，并将value添加字符串"|||"
![图片34.png](images/图片34.png)

- 代码实现：
```java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import scala.Tuple2;

import java.util.Arrays;

public class Test02_MapValues {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaPairRDD<String, String> javaPairRDD = sc.parallelizePairs(Arrays.asList(new Tuple2<>("k", "v"), new Tuple2<>("k1", "v1"), new Tuple2<>("k2", "v2")));

// 只修改value 不修改key

JavaPairRDD<String, String> mapValuesRDD = javaPairRDD.mapValues(new Function<String, String>() {

@Override

public String call(String v1) throws Exception {

return v1 + "|||";

}

});

mapValuesRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

#### 2.3.2.2 groupByKey()按照K重新分组

- 功能说明
groupByKey对每个key进行操作，但只生成一个seq，并不进行聚合。

该操作可以指定分区器或者分区数（默认使用HashPartitioner）

- 需求说明：统计单词出现次数
![图片35.png](images/图片35.png)

- 代码实现：
```java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

public class Test03_GroupByKey {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> integerJavaRDD = sc.parallelize(Arrays.asList("hi","hi","hello","spark" ),2);

// 统计单词出现次数

JavaPairRDD<String, Integer> pairRDD = integerJavaRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

// 聚合相同的key

JavaPairRDD<String, Iterable<Integer>> groupByKeyRDD = pairRDD.groupByKey();

// 合并值

JavaPairRDD<String, Integer> result = groupByKeyRDD.mapValues(new Function<Iterable<Integer>, Integer>() {

@Override

public Integer call(Iterable<Integer> v1) throws Exception {

Integer sum = 0;

for (Integer integer : v1) {

sum += integer;

}

return sum;

}

});

result. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}}
```
#### 2.3.2.3 reduceByKey()按照K聚合V

- 功能说明：该操作可以将RDD[K,V]中的元素按照相同的K对V进行聚合。其存在多种重载形式，还可以设置新RDD的分区数。
- 需求说明：统计单词出现次数
![图片36.png](images/图片36.png)

- 代码实现：
```java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

public class Test04_ReduceByKey {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> integerJavaRDD = sc.parallelize(Arrays.asList("hi","hi","hello","spark" ),2);

// 统计单词出现次数

JavaPairRDD<String, Integer> pairRDD = integerJavaRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

// 聚合相同的key

JavaPairRDD<String, Integer> result = pairRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

});

result. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
#### 2.3.2.4 reduceByKey和groupByKey区别

- reduceByKey：按照key进行聚合，在shuffle之前有combine（预聚合）操作，返回结果是RDD[K,V]。
- groupByKey：按照key进行分组，直接进行shuffle。
- 开发指导：在不影响业务逻辑的前提下，优先选用reduceByKey。求和操作不影响业务逻辑，求平均值影响业务逻辑。影响业务逻辑时建议先对数据类型进行转换再合并。
```java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

public class Test06_ReduceByKeyAvg {

public static void main(String[] args) throws InterruptedException {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaPairRDD<String, Integer> javaPairRDD = sc.parallelizePairs(Arrays.asList(new Tuple2<>("hi", 96), new Tuple2<>("hi", 97), new Tuple2<>("hello", 95), new Tuple2<>("hello", 195)));

// ("hi",(96,1))

JavaPairRDD<String, Tuple2<Integer, Integer>> tuple2JavaPairRDD = javaPairRDD.mapValues(new Function<Integer, Tuple2<Integer, Integer>>() {

@Override

public Tuple2<Integer, Integer> call(Integer v1) throws Exception {

return new Tuple2<>(v1, 1);

}

});

// 聚合RDD

JavaPairRDD<String, Tuple2<Integer, Integer>> reduceRDD = tuple2JavaPairRDD.reduceByKey(new Function2<Tuple2<Integer, Integer>, Tuple2<Integer, Integer>, Tuple2<Integer, Integer>>() {

@Override

public Tuple2<Integer, Integer> call(Tuple2<Integer, Integer> v1, Tuple2<Integer, Integer> v2) throws Exception {

return new Tuple2<>(v1._1 + v2._1, v1._2 + v2._2);

}

});

// 相除

JavaPairRDD<String, Double> result = reduceRDD.mapValues(new Function<Tuple2<Integer, Integer>, Double>() {

@Override

public Double call(Tuple2<Integer, Integer> v1) throws Exception {

return (new Double(v1._1) / v1._2);

}

});

result. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

#### 2.3.2.5 sortByKey()按照K进行排序

- 功能说明
在一个(K,V)的RDD上调用，K必须实现Ordered接口，返回一个按照key进行排序的(K,V)的RDD。

- 需求说明：创建一个pairRDD，按照key的正序和倒序进行排序
![图片37.png](images/图片37.png)

- 代码实现：
```java
package com.atguigu.keyValue;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;

import java.util.Arrays;

public class Test05_SortByKey {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaPairRDD<Integer, String> javaPairRDD = sc.parallelizePairs(Arrays.asList(new Tuple2<>(4, "a"), new Tuple2<>(3, "c"), new Tuple2<>(2, "d")));

// 填写布尔类型选择正序倒序

JavaPairRDD<Integer, String> pairRDD = javaPairRDD.sortByKey(false);

pairRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

## 2.4 Action行动算子

行动算子是触发了整个作业的执行。因为转换算子都是懒加载，并不会立即执行。

- 创建包名：com.atguigu.action
### 2.4.1 collect()以数组的形式返回数据集

- 功能说明：在驱动程序中，以数组Array的形式返回数据集的所有元素。
![图片38.png](images/图片38.png)

注意：所有的数据都会被拉取到Driver端，慎用。

- 需求说明：创建一个RDD，并将RDD内容收集到Driver端打印
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

import java.util.List;

public class Test01_Collect {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

List<Integer> collect = integerJavaRDD.collect();

for (Integer integer : collect) {

System.out.println(integer);

}

// 4. 关闭sc

sc.stop();

}

}
```
### 2.4.2 count()返回RDD中元素个数

- 功能说明：返回RDD中元素的个数
![图片39.png](images/图片39.png)

- 需求说明：创建一个RDD，统计该RDD的条数
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

public class Test02_Count {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

long count = integerJavaRDD.count();

System.out.println(count);

// 4. 关闭sc

sc.stop();

}

}
```
### 2.4.3 first()返回RDD中的第一个元素

- 功能说明：返回RDD中的第一个元素
![图片40.png](images/图片40.png)

- 需求说明：创建一个RDD，返回该RDD中的第一个元素
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

public class Test03_First {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

Integer first = integerJavaRDD.first();

System.out.println(first);

// 4. 关闭sc

sc.stop();

}

}
```
### 2.4.4 take()返回由RDD前n个元素组成的数组

- 功能说明：返回一个由RDD的前n个元素组成的数组
![图片41.png](images/图片41.png)

- 需求说明：创建一个RDD，取出前两个元素
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import java.util.Arrays;

import java.util.List;

public class Test04_Take {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

List<Integer> list = integerJavaRDD.take(3);

list.forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

### 2.4.5 countByKey()统计每种key的个数

- 功能说明：统计每种key的个数
![图片42.png](images/图片42.png)

- 需求说明：创建一个PairRDD，统计每种key的个数
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Map;

public class Test05_CountByKey {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaPairRDD<String, Integer> pairRDD = sc.parallelizePairs(Arrays.asList(new Tuple2<>("a", 8), new Tuple2<>("b", 8), new Tuple2<>("a", 8), new Tuple2<>("d", 8)));

Map<String, Long> map = pairRDD.countByKey();

System.out.println(map);

// 4. 关闭sc

sc.stop();

}

}
```

### 2.4.6 save相关算子

- saveAsTextFile(path)保存成Text文件
功能说明：将数据集的元素以textfile的形式保存到HDFS文件系统或者其他支持的文件系统，对于每个元素，Spark将会调用toString方法，将它装换为文件中的文本

- saveAsObjectFile(path) 序列化成对象保存到文件
功能说明：用于将RDD中的元素序列化成对象，存储到文件中。

- 代码实现
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;

import java.util.Arrays;

public class Test06_Save {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),2);

integerJavaRDD.saveAsTextFile("output");

integerJavaRDD.saveAsObjectFile("output1");

// 4. 关闭sc

sc.stop();

}

}
```

### 2.4.7 foreach()遍历RDD中每一个元素

![图片43.png](images/图片43.png)

- 需求说明：创建一个RDD，对每个元素进行打印
```java
package com.atguigu.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.VoidFunction;

import java.util.Arrays;

public class Test07_Foreach {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> integerJavaRDD = sc.parallelize(Arrays.asList(1, 2, 3, 4),4);

integerJavaRDD.foreach(new VoidFunction<Integer>() {

@Override

public void call(Integer integer) throws Exception {

System.out.println(integer);

}

});

// 4. 关闭sc

sc.stop();

}

}
```

### 2.4.8 foreachPartition ()遍历RDD中每一个分区

```java
package com.atguigu.spark.action;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.VoidFunction;

import java.util.Arrays;

import java.util.Iterator;

public class Test08_ForeachPartition {

public static void main(String[] args) {

// 1. 创建配置对象

SparkConf conf = new SparkConf().setAppName("core").setMaster("local[*]");

// 2. 创建sc环境

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> parallelize = sc.parallelize(Arrays.asList(1, 2, 3, 4, 5, 6), 2);

// 多线程一起计算   分区间无序  单个分区有序

parallelize.foreachPartition(new VoidFunction<Iterator<Integer>>() {

@Override

public void call(Iterator<Integer> integerIterator) throws Exception {

// 一次处理一个分区的数据

while (integerIterator.hasNext()) {

Integer next = integerIterator.next();

System.out.println(next);

}

}

});

// 4. 关闭sc

sc.stop();

}

}

```
## 2.5 WordCount案例实操

- 导入项目依赖
下方的是scala语言打包插件  只要使用scala语法打包运行到linux上面  必须要有

<dependencies>

<dependency>

<groupId>org.apache.spark</groupId>

<artifactId>spark-core_2.12</artifactId>

<version>3.3.1</version>

</dependency>

</dependencies>

### 2.5.1 本地调试

本地Spark程序调试需要使用Local提交模式，即将本机当做运行环境，Master和Worker都为本机。运行时直接加断点调试即可。如下：

- 代码实现
```java
package com.atguigu;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class WordCount {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 读取数据

JavaRDD<String> javaRDD = sc.textFile("input/2.txt");

// 长字符串切分为单个单词

JavaRDD<String> flatMapRDD = javaRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

List<String> strings = Arrays.asList(s.split(" "));

return strings.iterator();

}

});

// 转换格式为  (单词,1)

JavaPairRDD<String, Integer> pairRDD = flatMapRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

// 合并相同单词

JavaPairRDD<String, Integer> javaPairRDD = pairRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

});

javaPairRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

- 调试流程
![图片44.png](images/图片44.png)

### 2.5.2 集群运行

- 修改代码，修改运行模式，将输出的方法修改为落盘，同时设置可以自定义的传入传出路径
```java
package com.atguigu;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class WordCount {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("yarn").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 读取数据

JavaRDD<String> javaRDD = sc.textFile(args[0]);

// 长字符串切分为单个单词

JavaRDD<String> flatMapRDD = javaRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

List<String> strings = Arrays.asList(s.split(" "));

return strings.iterator();

}

});

// 转换格式为  (单词,1)

JavaPairRDD<String, Integer> pairRDD = flatMapRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

// 合并相同单词

JavaPairRDD<String, Integer> javaPairRDD = pairRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

});

javaPairRDD.saveAsTextFile(args[1]);

// 4. 关闭sc

sc.stop();

}

}

```
- 打包到集群测试
  - 点击package打包，然后，查看打完后的jar包
![图片45.png](images/图片45.png)

![图片46.png](images/图片46.png)

  - 将WordCount.jar上传到/opt/module/spark-yarn目录
  - 在HDFS上创建，存储输入文件的路径/input
[atguigu@hadoop102 spark-yarn]$ hadoop fs -mkdir /input

  - 上传输入文件到/input路径
[atguigu@hadoop102 spark-yarn]$ hadoop fs -put /opt/software /input

  - 执行任务
[atguigu@hadoop102 spark-yarn]$ bin/spark-submit \

--class com.atguigu.spark.WordCount \

--master yarn \

./WordCount.jar \

/input \

/output

注意：input和ouput都是HDFS上的集群路径。

  - 查询运行结果
[atguigu@hadoop102 spark-yarn]$ hadoop fs -cat /output/*

## 2.6 RDD序列化

在实际开发中我们往往需要自己定义一些对于RDD的操作，那么此时需要注意的是，初始化工作是在Driver端进行的，而实际运行程序是在Executor端进行的，这就涉及到了跨进程通信，是需要序列化的。下面我们看几个例子：

### 2.6.1 序列化异常

- 创建包名：com.atguigu.serializable
- 创建使用的javaBean：User
```java
package com.atguigu.bean;

import java.io.Serializable;

public class User implements Serializable {

private String name;

private Integer age;

public User(String name, Integer age) {

this.name = name;

this.age = age;

}

public User() {

}

public String getName() {

return name;

}

public void setName(String name) {

this.name = name;

}

public Integer getAge() {

return age;

}

public void setAge(Integer age) {

this.age = age;

}

@Override

public String toString() {

return "User{" +

"name='" + name + '\'' +

", age=" + age +

'}';

}

}
```

- 创建类：Test01_Ser测试序列化
```java
package com.atguigu.serializable;

import com.atguigu.bean.User;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;

public class Test01_Ser {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

User zhangsan = new User("zhangsan", 13);

User lisi = new User("lisi", 13);

JavaRDD<User> userJavaRDD = sc.parallelize(Arrays.asList(zhangsan, lisi), 2);

JavaRDD<User> mapRDD = userJavaRDD.map(new Function<User, User>() {

@Override

public User call(User v1) throws Exception {

return new User(v1.getName(), v1.getAge() + 1);

}

});

mapRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

### 2.6.2 Kryo序列化框架

参考地址:

Java的序列化能够序列化任何的类。但是比较重，序列化后对象的体积也比较大。

Spark出于性能的考虑，Spark2.0开始支持另外一种Kryo序列化机制。Kryo速度是Serializable的10倍。当RDD在Shuffle数据的时候，简单数据类型、数组和字符串类型已经在Spark内部使用Kryo来序列化。

```java
package com.atguigu.serializable;

import com.atguigu.bean.User;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;

public class Test02_Kryo {

public static void main(String[] args) throws ClassNotFoundException {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore")

// 替换默认的序列化机制

.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

// 注册需要使用kryo序列化的自定义类

.registerKryoClasses(new Class[]{Class.forName("com.atguigu.bean.User")});

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

User zhangsan = new User("zhangsan", 13);

User lisi = new User("lisi", 13);

JavaRDD<User> userJavaRDD = sc.parallelize(Arrays.asList(zhangsan, lisi), 2);

JavaRDD<User> mapRDD = userJavaRDD.map(new Function<User, User>() {

@Override

public User call(User v1) throws Exception {

return new User(v1.getName(), v1.getAge() + 1);

}

});

mapRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}

```
## 2.7 RDD依赖关系

### 2.7.1 查看血缘关系

RDD只支持粗粒度转换，即在大量记录上执行的单个操作。将创建RDD的一系列Lineage（血统）记录下来，以便恢复丢失的分区。RDD的Lineage会记录RDD的元数据信息和转换行为，当该RDD的部分分区数据丢失时，它可以根据这些信息来重新运算和恢复丢失的数据分区。

![图片47.png](images/图片47.png)

- 创建包名：com.atguigu.dependency
- 代码实现
```java
package com.atguigu.dependency;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class Test01_Dep {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

System.out.println(lineRDD.toDebugString());

System.out.println("-------------------");

JavaRDD<String> wordRDD = lineRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

List<String> stringList = Arrays.asList(s.split(" "));

return stringList.iterator();

}

});

System.out.println(wordRDD.toDebugString());

System.out.println("-------------------");

JavaPairRDD<String, Integer> tupleRDD = wordRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

System.out.println(tupleRDD.toDebugString());

System.out.println("-------------------");

JavaPairRDD<String, Integer> wordCountRDD = tupleRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

});

System.out.println(wordCountRDD.toDebugString());

System.out.println("-------------------");

// 4. 关闭sc

sc.stop();

}

}
```

- 打印结果
(2) input/2.txt MapPartitionsRDD[1] at textFile at Test01_Dep.java:29 []

|  input/2.txt HadoopRDD[0] at textFile at Test01_Dep.java:29 []

(2) MapPartitionsRDD[2] at flatMap at Test01_Dep.java:32 []

|  input/2.txt MapPartitionsRDD[1] at textFile at Test01_Dep.java:29 []

|  input/2.txt HadoopRDD[0] at textFile at Test01_Dep.java:29 []

(2) MapPartitionsRDD[3] at mapToPair at Test01_Dep.java:42 []

|  MapPartitionsRDD[2] at flatMap at Test01_Dep.java:32 []

|  input/2.txt MapPartitionsRDD[1] at textFile at Test01_Dep.java:29 []

|  input/2.txt HadoopRDD[0] at textFile at Test01_Dep.java:29 []

(2) ShuffledRDD[4] at reduceByKey at Test01_Dep.java:50 []

+-(2) MapPartitionsRDD[3] at mapToPair at Test01_Dep.java:42 []

|  MapPartitionsRDD[2] at flatMap at Test01_Dep.java:32 []

|  input/2.txt MapPartitionsRDD[1] at textFile at Test01_Dep.java:29 []

|  input/2.txt HadoopRDD[0] at textFile at Test01_Dep.java:29 []

注意：圆括号中的数字表示RDD的并行度，也就是有几个分区

### 2.7.2 窄依赖

窄依赖表示每一个父RDD的Partition最多被子RDD的一个Partition使用（一对一or多对一），窄依赖我们形象的比喻为独生子女。

![图片48.png](images/图片48.png)

### 2.7.3 宽依赖

宽依赖表示同一个父RDD的Partition被多个子RDD的Partition依赖（只能是一对多），会引起Shuffle，总结：宽依赖我们形象的比喻为超生。

![图片49.png](images/图片49.png)

具有宽依赖的transformations包括：sort、reduceByKey、groupByKey、join和调用rePartition函数的任何操作。

宽依赖对Spark去评估一个transformations有更加重要的影响，比如对性能的影响。在不影响业务要求的情况下，要尽量避免使用有宽依赖的转换算子，因为有宽依赖，就一定会走shuffle，影响性能。

### 2.7.4 Stage任务划分

- DAG有向无环图
DAG（Directed Acyclic Graph）有向无环图是由点和线组成的拓扑图形，该图形具有方向，不会闭环。例如，DAG记录了RDD的转换过程和任务的阶段。

![图片50.png](images/图片50.png)

- 任务运行的整体流程
![图片51.png](images/图片51.png)

![图片52.png](images/图片52.png)

- RDD任务切分中间分为：Application、Job、Stage和Task
  - Application：初始化一个SparkContext即生成一个Application；
  - Job：一个Action算子就会生成一个Job；
  - Stage：Stage等于宽依赖的个数加1；
  - Task：一个Stage阶段中，最后一个RDD的分区个数就是Task的个数。
注意：Application->Job->Stage->Task每一层都是1对n的关系。

![图片53.png](images/图片53.png)

- 代码实现
```java
package com.atguigu.dependency;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class Test02_Dep {

public static void main(String[] args) throws InterruptedException {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

System.out.println(lineRDD.toDebugString());

System.out.println("-------------------");

JavaRDD<String> wordRDD = lineRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

List<String> stringList = Arrays.asList(s.split(" "));

return stringList.iterator();

}

});

System.out.println(wordRDD);

System.out.println("-------------------");

JavaPairRDD<String, Integer> tupleRDD = wordRDD.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

System.out.println(tupleRDD.toDebugString());

System.out.println("-------------------");

// 缩减分区

JavaPairRDD<String, Integer> coalesceRDD = tupleRDD.coalesce(1);

JavaPairRDD<String, Integer> wordCountRDD = coalesceRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

},4);

System.out.println(wordCountRDD.toDebugString());

System.out.println("-------------------");

wordCountRDD. collect().forEach(System.out::println);

wordCountRDD. collect().forEach(System.out::println);

Thread.sleep(600000);

// 4. 关闭sc

sc.stop();

}

}

```
- 查看Job个数
查看，发现Job有两个。

![图片54.png](images/图片54.png)

- 查看Stage个数
查看Job0的Stage。由于只有1个Shuffle阶段，所以Stage个数为2。

![图片55.png](images/图片55.png)

![图片56.png](images/图片56.png)

查看Job1的Stage。由于只有1个Shuffle阶段，所以Stage个数为2。

![图片57.png](images/图片57.png)

![图片58.png](images/图片58.png)

- Task个数
查看Job0的Stage0的Task个数，2个。

![图片59.png](images/图片59.png)

查看Job0的Stage1的Task个数，2个。

![图片60.png](images/图片60.png)

查看Job1的Stage2的Task个数，0个（2个跳过skipped）。

![图片61.png](images/图片61.png)

查看Job1的Stage3的Task个数，2个。

![图片62.png](images/图片62.png)

注意：如果存在shuffle过程，系统会自动进行缓存，UI界面显示skipped的部分。

## 2.8 RDD持久化

### 2.8.1 RDD Cache缓存

RDD通过Cache或者Persist方法将前面的计算结果缓存，默认情况下会把数据以序列化的形式缓存在JVM的堆内存中。但是并不是这两个方法被调用时立即缓存，而是触发后面的action算子时，该RDD将会被缓存在计算节点的内存中，并供后面重用。

![图片63.png](images/图片63.png)

- 创建包名：com.atguigu.cache
- 代码实现
```java
package com.atguigu.cache;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function;

import scala.Tuple2;

import java.util.Arrays;

import java.util.Iterator;

import java.util.List;

public class Test01_Cache {

public static void main(String[] args) throws InterruptedException {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

//3.1.业务逻辑

JavaRDD<String> wordRDD = lineRDD.flatMap(new FlatMapFunction<String, String>() {

@Override

public Iterator<String> call(String s) throws Exception {

List<String> stringList = Arrays.asList(s.split(" "));

return stringList.iterator();

}

});

JavaRDD<Tuple2<String, Integer>> tuple2JavaRDD = wordRDD.map(new Function<String, Tuple2<String, Integer>>() {

@Override

public Tuple2<String, Integer> call(String v1) throws Exception {

System.out.println("*****************");

return new Tuple2<>(v1, 1);

}

});

//3.5 cache缓存前打印血缘关系

System.out.println(tuple2JavaRDD.toDebugString());

//3.4 数据缓存。

//cache底层调用的就是persist方法,缓存级别默认用的是MEMORY_ONLY

tuple2JavaRDD.cache();

//3.6 persist方法可以更改存储级别

// wordToOneRdd.persist(StorageLevel.MEMORY_AND_DISK_2)

//3.2 触发执行逻辑

tuple2JavaRDD. collect().forEach(System.out::println);

//3.5 cache缓存后打印血缘关系

//cache操作会增加血缘关系，不改变原有的血缘关系

System.out.println(tuple2JavaRDD.toDebugString());

System.out.println("=====================");

//3.3 再次触发执行逻辑

tuple2JavaRDD. collect().forEach(System.out::println);

Thread.sleep(1000000);

// 4. 关闭sc

sc.stop();

}

}
```

- 源码解析
mapRdd.cache()

def cache(): this.type = persist()

def persist(): this.type = persist(StorageLevel.MEMORY_ONLY)

object StorageLevel {

val NONE = new StorageLevel(false, false, false, false)

val DISK_ONLY = new StorageLevel(true, false, false, false)

val DISK_ONLY_2 = new StorageLevel(true, false, false, false, 2)

val MEMORY_ONLY = new StorageLevel(false, true, false, true)

val MEMORY_ONLY_2 = new StorageLevel(false, true, false, true, 2)

val MEMORY_ONLY_SER = new StorageLevel(false, true, false, false)

val MEMORY_ONLY_SER_2 = new StorageLevel(false, true, false, false, 2)

val MEMORY_AND_DISK = new StorageLevel(true, true, false, true)

val MEMORY_AND_DISK_2 = new StorageLevel(true, true, false, true, 2)

val MEMORY_AND_DISK_SER = new StorageLevel(true, true, false, false)

val MEMORY_AND_DISK_SER_2 = new StorageLevel(true, true, false, false, 2)

val OFF_HEAP = new StorageLevel(true, true, true, false, 1)

注意：默认的存储级别都是仅在内存存储一份。在存储级别的末尾加上“_2”表示持久化的数据存为两份。SER：表示序列化。

![图片64.png](images/图片64.png)

缓存有可能丢失，或者存储于内存的数据由于内存不足而被删除，RDD的缓存容错机制保证了即使缓存丢失也能保证计算的正确执行。通过基于RDD的一系列转换，丢失的数据会被重算，由于RDD的各个Partition是相对独立的，因此只需要计算丢失的部分即可，并不需要重算全部Partition。

- 自带缓存算子
Spark会自动对一些Shuffle操作的中间数据做持久化操作（比如：reduceByKey）。这样做的目的是为了当一个节点Shuffle失败了避免重新计算整个输入。但是，在实际使用的时候，如果想重用数据，仍然建议调用persist或cache。

查看前面2.7.4依赖关系代码的DAG图

访问页面，查看第一个和第二个job的DAG图。说明：增加缓存后血缘依赖关系仍然有，但是，第二个job取的数据是从缓存中取的。

![图片65.png](images/图片65.png)

![图片66.png](images/图片66.png)

### 2.8.2 RDD CheckPoint检查点

- 检查点：是通过将RDD中间结果写入磁盘。
- 为什么要做检查点？
由于血缘依赖过长会造成容错成本过高，这样就不如在中间阶段做检查点容错，如果检查点之后有节点出现问题，可以从检查点开始重做血缘，减少了开销。

- 检查点存储路径：Checkpoint的数据通常是存储在HDFS等容错、高可用的文件系统
- 检查点数据存储格式为：二进制的文件
- 检查点切断血缘：在Checkpoint的过程中，该RDD的所有依赖于父RDD中的信息将全部被移除。
- 检查点触发时间：对RDD进行Checkpoint操作并不会马上被执行，必须执行Action操作才能触发。但是检查点为了数据安全，会从血缘关系的最开始执行一遍。
![图片67.png](images/图片67.png)

- 设置检查点步骤
  - 设置检查点数据存储路径：sc.setCheckpointDir("./checkpoint1")
  - 调用检查点方法：wordToOneRdd.checkpoint()
- 代码实现
```java
package com.atguigu.cache;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

public class Test02_CheckPoint {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

sc.setCheckpointDir("ck");

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

JavaPairRDD<String, Long> tupleRDD = lineRDD.mapToPair(new PairFunction<String, String, Long>() {

@Override

public Tuple2<String, Long> call(String s) throws Exception {

return new Tuple2<String, Long>(s, System.currentTimeMillis());

}

});

// 查看血缘关系

System.out.println(tupleRDD.toDebugString());

// 增加检查点避免计算两次

tupleRDD.cache();

// 进行检查点

tupleRDD.checkpoint();

tupleRDD. collect().forEach(System.out::println);

System.out.println(tupleRDD.toDebugString());

// 第二次计算

tupleRDD. collect().forEach(System.out::println);

// 第三次计算

tupleRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

- 执行结果
访问页面，查看4个job的DAG图。其中第2个图是checkpoint的job运行DAG图。第3、4张图说明，检查点切断了血缘依赖关系。

![图片68.png](images/图片68.png)

![图片69.png](images/图片69.png)

![图片70.png](images/图片70.png)

![图片71.png](images/图片71.png)

- 只增加checkpoint，没有增加Cache缓存打印
  - 第1个job执行完，触发了checkpoint，第2个job运行checkpoint，并把数据存储在检查点上。第3、4个job，数据从检查点上直接读取。
(hadoop,1577960215526)

。。。。。。

(hello,1577960215526)

(hadoop,1577960215609)

。。。。。。

(hello,1577960215609)

(hadoop,1577960215609)

。。。。。。

(hello,1577960215609)

  - 增加checkpoint，也增加Cache缓存打印
第1个job执行完，数据就保存到Cache里面了，第2个job运行checkpoint，直接读取Cache里面的数据，并把数据存储在检查点上。第3、4个job，数据从检查点上直接读取。

(hadoop,1577960642223)

。。。。。。

(hello,1577960642225)

(hadoop,1577960642223)

。。。。。。

(hello,1577960642225)

(hadoop,1577960642223)

。。。。。。

(hello,1577960642225)

![图片72.png](images/图片72.png)

### 2.8.3 缓存和检查点区别

- Cache缓存只是将数据保存起来，不切断血缘依赖。Checkpoint检查点切断血缘依赖。
- Cache缓存的数据通常存储在磁盘、内存等地方，可靠性低。Checkpoint的数据通常存储在HDFS等容错、高可用的文件系统，可靠性高。
- 建议对checkpoint()的RDD使用Cache缓存，这样checkpoint的job只需从Cache缓存中读取数据即可，否则需要再从头计算一次RDD。
- 如果使用完了缓存，可以通过unpersist()方法释放缓存。
### 2.8.4 检查点存储到HDFS集群

如果检查点数据存储到HDFS集群，要注意配置访问集群的用户名。否则会报访问权限异常。
```java

package com.atguigu.cache;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

public class Test02_CheckPoint2 {

public static void main(String[] args) {

// 修改用户名称

System.setProperty("HADOOP_USER_NAME","atguigu");

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 需要设置路径.需要提前在HDFS集群上创建/checkpoint路径

sc.setCheckpointDir("hdfs://hadoop102:8020/checkpoint");

// 3. 编写代码

JavaRDD<String> lineRDD = sc.textFile("input/2.txt");

JavaPairRDD<String, Long> tupleRDD = lineRDD.mapToPair(new PairFunction<String, String, Long>() {

@Override

public Tuple2<String, Long> call(String s) throws Exception {

return new Tuple2<String, Long>(s, System.currentTimeMillis());

}

});

// 查看血缘关系

System.out.println(tupleRDD.toDebugString());

// 增加检查点避免计算两次

tupleRDD.cache();

// 进行检查点

tupleRDD.checkpoint();

tupleRDD. collect().forEach(System.out::println);

System.out.println(tupleRDD.toDebugString());

// 第二次计算

tupleRDD. collect().forEach(System.out::println);

// 第三次计算

tupleRDD. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

## 2.9 键值对RDD数据分区

Spark目前支持Hash分区、Range分区和用户自定义分区。Hash分区为当前的默认分区。分区器直接决定了RDD中分区的个数、RDD中每条数据经过Shuffle后进入哪个分区和Reduce的个数。

- 注意：
  - 只有Key-Value类型的pairRDD才有分区器，非Key-Value类型的RDD分区的值是None
  - 每个RDD的分区ID范围：0~numPartitions-1，决定这个值是属于那个分区的。
- 获取RDD分区
  - 创建包名：com.atguigu.partitioner
  - 代码实现
```java
package com.atguigu.partitioner;

import org.apache.spark.Partitioner;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.Optional;

import org.apache.spark.api.java.function.Function2;

import scala.Tuple2;

import java.util.Arrays;

public class Test01_Partitioner {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaPairRDD<String, Integer> tupleRDD = sc.parallelizePairs(Arrays.asList(new Tuple2<>("s", 1), new Tuple2<>("a", 3), new Tuple2<>("d", 2)));

// 获取分区器

Optional<Partitioner> partitioner = tupleRDD.partitioner();

System.out.println(partitioner);

JavaPairRDD<String, Integer> reduceByKeyRDD = tupleRDD.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

});

// 获取分区器

Optional<Partitioner> partitioner1 = reduceByKeyRDD.partitioner();

System.out.println(partitioner1);

// 4. 关闭sc

sc.stop();

}

}

```
### 2.9.1 Hash分区

![图片73.png](images/图片73.png)

### 2.9.2 Ranger分区

![图片74.png](images/图片74.png)

# 3 广播变量

广播变量：分布式共享只读变量。

广播变量用来高效分发较大的对象。向所有工作节点发送一个较大的只读值，以供一个或多个Spark Task操作使用。比如，如果你的应用需要向所有节点发送一个较大的只读查询表，广播变量用起来会很顺手。在多个Task并行操作中使用同一个变量，但是Spark会为每个Task任务分别发送。

- 使用广播变量步骤：
  - 调用SparkContext.broadcast（广播变量）创建出一个广播对象，任何可序列化的类型都可以这么实现。
  - 通过广播变量.value，访问该对象的值。
  - 广播变量只会被发到各个节点一次，作为只读值处理（修改这个值不会影响到别的节点）。
- 原理说明
![图片75.png](images/图片75.png)

- 创建包名：com.atguigu.broadcast
- 代码实现
```java
package com.atguigu.accumulator;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.broadcast.Broadcast;

import java.util.Arrays;

import java.util.List;

public class Test02_Broadcast {

public static void main(String[] args) {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore");

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

JavaRDD<Integer> intRDD = sc.parallelize(Arrays.asList(4, 56, 7, 8, 1, 2));

// 幸运数字

List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);

// 找出幸运数字

// 每一个task都会创建一个list浪费内存

/*

JavaRDD<Integer> result = intRDD.filter(new Function<Integer, Boolean>() {

@Override

public Boolean call(Integer v1) throws Exception {

return list.contains(v1);

}

});

*/

// 创建广播变量

// 只发送一份数据到每一个executor

Broadcast<List<Integer>> broadcast = sc.broadcast(list);

JavaRDD<Integer> result = intRDD.filter(new Function<Integer, Boolean>() {

@Override

public Boolean call(Integer v1) throws Exception {

return broadcast.value().contains(v1);

}

});

result. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```

# 4 SparkCore实战

## 4.1 数据准备

- 数据格式
![图片76.png](images/图片76.png)

- 数据详细字段说明
4.2 需求：Top10热门品类

![图片77.png](images/图片77.png)

需求说明：品类是指产品的分类，大型电商网站品类分多级，咱们的项目中品类只有一级，不同的公司可能对热门的定义不一样。我们按照每个品类的点击、下单、支付的量（次数）来统计热门品类。

鞋点击数 下单数  支付数

衣服点击数 下单数  支付数

电脑点击数 下单数  支付数

例如，综合排名 = 点击数*20% + 下单数*30% + 支付数*50%

为了更好的泛用性，当前案例按照点击次数进行排序，如果点击相同，按照下单数，如果下单还是相同，按照支付数。

### 4.1.1 需求分析

采用样例类的方式实现，聚合算子使用reduceByKey。

![图片78.png](images/图片78.png)

### 4.1.2 需求实现

- 添加lombok的插件
![图片79.png](images/图片79.png)

- 添加依赖lombok可以省略getset代码
<dependency>

<groupId>org.projectlombok</groupId>

<artifactId>lombok</artifactId>

<version>1.18.22</version>

</dependency>

- 创建两个存放数据的类
```java
package com.atguigu.spark.bean;

import lombok.Data;

import java.io.Serializable;

@Data

public class UserVisitAction implements Serializable {

private String date;

private String user_id;

private String session_id;

private String page_id;

private String action_time;

private String search_keyword;

private String click_category_id;

private String click_product_id;

private String order_category_ids;

private String order_product_ids;

private String pay_category_ids;

private String pay_product_ids;

private String city_id;

public UserVisitAction() {

}

public UserVisitAction(String date, String user_id, String session_id, String page_id, String action_time, String search_keyword, String click_category_id, String click_product_id, String order_category_ids, String order_product_ids, String pay_category_ids, String pay_product_ids, String city_id) {

this.date = date;

this.user_id = user_id;

this.session_id = session_id;

this.page_id = page_id;

this.action_time = action_time;

this.search_keyword = search_keyword;

this.click_category_id = click_category_id;

this.click_product_id = click_product_id;

this.order_category_ids = order_category_ids;

this.order_product_ids = order_product_ids;

this.pay_category_ids = pay_category_ids;

this.pay_product_ids = pay_product_ids;

this.city_id = city_id;

}

}

package com.atguigu.spark.bean;

import lombok.Data;

import java.io.Serializable;

@Data

public class CategoryCountInfo implements Serializable, Comparable<CategoryCountInfo> {

private String categoryId;

private Long clickCount;

private Long orderCount;

private Long payCount;

public CategoryCountInfo() {

}

public CategoryCountInfo(String categoryId, Long clickCount, Long orderCount, Long payCount) {

this.categoryId = categoryId;

this.clickCount = clickCount;

this.orderCount = orderCount;

this.payCount = payCount;

}

@Override

public int compareTo(CategoryCountInfo o) {

// 小于返回-1,等于返回0,大于返回1

if (this.getClickCount().equals(o.getClickCount())) {

if (this.getOrderCount().equals(o.getOrderCount())) {

if (this.getPayCount().equals(o.getPayCount())) {

return 0;

} else {

return this.getPayCount() < o.getPayCount() ? -1 : 1;

}

} else {

return this.getOrderCount() < o.getOrderCount() ? -1 : 1;

}

} else {

return this.getClickCount() < o.getClickCount() ? -1 : 1;

}

}

}
```

- 核心业务代码实现
```java
package com.atguigu.spark.demo;

import com.atguigu.spark.bean.CategoryCountInfo;

import com.atguigu.spark.bean.UserVisitAction;

import org.apache.spark.SparkConf;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.JavaRDD;

import org.apache.spark.api.java.JavaSparkContext;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;

import java.util.ArrayList;

import java.util.Iterator;

public class Test06_Top10 {

public static void main(String[] args) throws ClassNotFoundException {

// 1.创建配置对象

SparkConf conf = new SparkConf().setMaster("local[*]").setAppName("sparkCore")

// 替换默认的序列化机制

.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

// 注册需要使用kryo序列化的自定义类

.registerKryoClasses(new Class[]{Class.forName("com.atguigu.spark.bean.CategoryCountInfo"),Class.forName("com.atguigu.spark.bean.UserVisitAction")});

// 2. 创建sparkContext

JavaSparkContext sc = new JavaSparkContext(conf);

// 3. 编写代码

// 分三次进行wordCount 最后使用cogroup合并三组数据

JavaRDD<String> lineRDD = sc.textFile("input/user_visit_action.txt");

// 转换为对象

JavaRDD<UserVisitAction> actionRDD = lineRDD.map(new Function<String, UserVisitAction>() {

@Override

public UserVisitAction call(String v1) throws Exception {

String[] data = v1.split("_");

return new UserVisitAction(

data[0],

data[1],

data[2],

data[3],

data[4],

data[5],

data[6],

data[7],

data[8],

data[9],

data[10],

data[11],

data[12]

);

}

});

JavaRDD<CategoryCountInfo> categoryCountInfoJavaRDD = actionRDD.flatMap(new FlatMapFunction<UserVisitAction, CategoryCountInfo>() {

@Override

public Iterator<CategoryCountInfo> call(UserVisitAction userVisitAction) throws Exception {

ArrayList<CategoryCountInfo> countInfos = new ArrayList<>();

if (!userVisitAction.getClick_category_id().equals("-1")) {

// 当前为点击数据

countInfos.add(new CategoryCountInfo(userVisitAction.getClick_category_id(), 1L, 0L, 0L));

} else if (!userVisitAction.getOrder_category_ids().equals("null")) {

// 当前为订单数据

String[] orders = userVisitAction.getOrder_category_ids().split(",");

for (String order : orders) {

countInfos.add(new CategoryCountInfo(order, 0L, 1L, 0L));

}

} else if (!userVisitAction.getPay_category_ids().equals("null")) {

// 当前为支付数据

String[] pays = userVisitAction.getPay_category_ids().split(",");

for (String pay : pays) {

countInfos.add(new CategoryCountInfo(pay, 0L, 0L, 1L));

}

}

return countInfos.iterator();

}

});

// 合并相同的id

JavaPairRDD<String, CategoryCountInfo> countInfoJavaPairRDD = categoryCountInfoJavaRDD.mapToPair(new PairFunction<CategoryCountInfo, String, CategoryCountInfo>() {

@Override

public Tuple2<String, CategoryCountInfo> call(CategoryCountInfo categoryCountInfo) throws Exception {

return new Tuple2<>(categoryCountInfo.getCategoryId(), categoryCountInfo);

}

});

JavaPairRDD<String, CategoryCountInfo> countInfoPairRDD = countInfoJavaPairRDD.reduceByKey(new Function2<CategoryCountInfo, CategoryCountInfo, CategoryCountInfo>() {

@Override

public CategoryCountInfo call(CategoryCountInfo v1, CategoryCountInfo v2) throws Exception {

v1.setClickCount(v1.getClickCount() + v2.getClickCount());

v1.setOrderCount(v1.getOrderCount() + v2.getOrderCount());

v1.setPayCount(v1.getPayCount() + v2.getPayCount());

return v1;

}

});

JavaRDD<CategoryCountInfo> countInfoJavaRDD = countInfoPairRDD.map(new Function<Tuple2<String, CategoryCountInfo>, CategoryCountInfo>() {

@Override

public CategoryCountInfo call(Tuple2<String, CategoryCountInfo> v1) throws Exception {

return v1._2;

}

});

// CategoryCountInfo需要能够比较大小

JavaRDD<CategoryCountInfo> result = countInfoJavaRDD.sortBy(new Function<CategoryCountInfo, CategoryCountInfo>() {

@Override

public CategoryCountInfo call(CategoryCountInfo v1) throws Exception {

return v1;

}

}, false, 2);

result. collect().forEach(System.out::println);

// 4. 关闭sc

sc.stop();

}

}
```
