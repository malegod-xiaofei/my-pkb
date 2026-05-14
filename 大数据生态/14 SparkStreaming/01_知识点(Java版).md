尚硅谷大数据技术之SparkStreaming

（作者：尚硅谷研究院）

版本：V5.0

# 1 SparkStreaming概述

## 1.1 Spark Streaming是什么

官方文档:

![图片1.png](images/图片1.png)

## 1.2 Spark Streaming架构原理

### 1.2.1 什么是DStream

![图片2.png](images/图片2.png)

### 1.2.2 架构图

- 整体架构图
![图片3.png](images/图片3.png)

- SparkStreaming架构图
![图片4.png](images/图片4.png)

## 1.3 Spark Streaming特点

- 易用
![图片5.png](images/图片5.png)

- 容错
![图片6.png](images/图片6.png)

- 易整合到Spark体系
![图片7.png](images/图片7.png)

# 2 HelloWorld

## 2.1 版本选型

![图片8.png](images/图片8.png)

注意：目前spark3.0.0以上版本只有Direct模式。

## 2.2 HelloWorld实现

需求：通过SparkStreaming读取kafka某个主题的数据并打印输出到控制台。

官方文档:

- 添加依赖

```java
<dependencies>

<dependency>

<groupId>org.apache.spark</groupId>

<artifactId>spark-streaming_2.12</artifactId>

<version>3.3.1</version>

</dependency>

<dependency>

<groupId>org.apache.spark</groupId>

<artifactId>spark-core_2.12</artifactId>

<version>3.3.1</version>

</dependency>

<dependency>

<groupId>org.apache.spark</groupId>

<artifactId>spark-streaming-kafka-0-10_2.12</artifactId>

<version>3.3.1</version>

</dependency>

</dependencies>
```

- 编写代码

```java
package com.atguigu;

import org.apache.kafka.clients.consumer.ConsumerConfig;

import org.apache.kafka.clients.consumer.ConsumerRecord;

import org.apache.spark.api.java.function.Function;

import org.apache.spark.streaming.Duration;

import org.apache.spark.streaming.api.java.JavaInputDStream;

import org.apache.spark.streaming.api.java.JavaStreamingContext;

import org.apache.spark.streaming.kafka010.ConsumerStrategies;

import org.apache.spark.streaming.kafka010.KafkaUtils;

import org.apache.spark.streaming.kafka010.LocationStrategies;

import java.util.ArrayList;

import java.util.HashMap;

public class Test01_HelloWorld {

public static void main(String[] args) throws InterruptedException {

// 创建流环境

JavaStreamingContext javaStreamingContext = new JavaStreamingContext("local[*]", "HelloWorld", Duration.apply(3000));

// 创建配置参数

HashMap<String, Object> map = new HashMap<>();

map.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,"hadoop102:9092,hadoop103:9092,hadoop104:9092");

map.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.GROUP_ID_CONFIG,"atguigu");

map.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

// 需要消费的主题

ArrayList<String> strings = new ArrayList<>();

strings.add("topic_db");

JavaInputDStream<ConsumerRecord<String, String>> directStream = KafkaUtils.createDirectStream(javaStreamingContext, LocationStrategies.PreferBrokers(), ConsumerStrategies.<String, String>Subscribe(strings,map));

directStream.map(new Function<ConsumerRecord<String, String>, String>() {

@Override

public String call(ConsumerRecord<String, String> v1) throws Exception {

return v1.value();

}

}).print(100);

// 执行流的任务

javaStreamingContext.start();

javaStreamingContext.awaitTermination();

}

}
```

- 更改日志打印级别
如果不希望运行时打印大量日志，可以在resources文件夹中添加log4j2.properties文件，并添加日志配置信息

```java
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

- 启动生产者生产数据
```bash
[atguigu@hadoop102 ~]$ kafka-console-producer.sh --broker-list hadoop102:9092 --topic topicA

hello spark
```

- 在Idea控制台输出如下内容
-------------------------------------------

Time: 1602731772000 ms

-------------------------------------------

hello spark

## 2.3 HelloWorld解析

DStream是Spark Streaming的基础抽象，代表持续性的数据流和经过各种Spark算子操作后的结果数据流。

在内部实现上，每一批次的数据封装成一个RDD，一系列连续的RDD组成了DStream。对这些RDD的转换是由Spark引擎来计算。

说明：DStream中批次与批次之间计算相互独立。如果批次设置时间小于计算时间会出现计算任务叠加情况，需要多分配资源。通常情况，批次设置时间要大于计算时间。

![图片9.png](images/图片9.png)

# 3 DStream转换

DStream上的操作与RDD的类似，分为转换和输出两种，此外转换操作中还有一些比较特殊的原语，如：transform()以及各种Window相关的原语。

## 3.1 无状态转化操作

无状态转化操作：就是把RDD转化操作应用到DStream每个批次上，每个批次相互独立，自己算自己的。

### 3.1.1 常规无状态转化操作

DStream的部分无状态转化操作列在了下表中，都是DStream自己的API。

注意，只有JavaPairDStream<Key, Value>才能使用xxxByKey()类型的转换算子。

需要记住的是，尽管这些函数看起来像作用在整个流上一样，但事实上每个DStream在内部是由许多RDD批次组成，且无状态转化操作是分别应用到每个RDD(一个批次的数据)上的。

## 3.2 窗口操作

### 3.2.1 WindowOperations

Window Operations可以设置窗口的大小和滑动窗口的间隔来动态的获取当前Streaming的允许状态。所有基于窗口的操作都需要两个参数，分别为窗口时长以及滑动步长。

- 窗口时长：计算内容的时间范围；
- 滑动步长：隔多久触发一次计算。
注意：这两者都必须为采集批次大小的整数倍。

如下图所示WordCount案例：窗口大小为批次的2倍，滑动步等于批次大小。

![图片10.png](images/图片10.png)

### 3.2.2 Window

- 基本语法：
window(windowLength, slideInterval): 基于对源DStream窗口的批次进行计算返回一个新的DStream。

- 需求：
统计WordCount：3秒一个批次，窗口12秒，滑步6秒。

- 代码编写：

```java
package com.atguigu;

import org.apache.kafka.clients.consumer.ConsumerConfig;

import org.apache.kafka.clients.consumer.ConsumerRecord;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import org.apache.spark.streaming.Duration;

import org.apache.spark.streaming.api.java.JavaDStream;

import org.apache.spark.streaming.api.java.JavaInputDStream;

import org.apache.spark.streaming.api.java.JavaPairDStream;

import org.apache.spark.streaming.api.java.JavaStreamingContext;

import org.apache.spark.streaming.kafka010.ConsumerStrategies;

import org.apache.spark.streaming.kafka010.KafkaUtils;

import org.apache.spark.streaming.kafka010.LocationStrategies;

import scala.Tuple2;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.HashMap;

import java.util.Iterator;

public class Test02_Window {

public static void main(String[] args) throws InterruptedException {

// 创建流环境

JavaStreamingContext javaStreamingContext = new JavaStreamingContext("local[*]", "window", Duration.apply(3000));

// 创建配置参数

HashMap<String, Object> map = new HashMap<>();

map.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,"hadoop102:9092,hadoop103:9092,hadoop104:9092");

map.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.GROUP_ID_CONFIG,"atguigu");

map.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

// 需要消费的主题

ArrayList<String> strings = new ArrayList<>();

strings.add("topicA");

JavaInputDStream<ConsumerRecord<String, String>> directStream = KafkaUtils.createDirectStream(javaStreamingContext, LocationStrategies.PreferBrokers(), ConsumerStrategies.<String, String>Subscribe(strings,map));

JavaDStream<String> stringJavaDStream = directStream.flatMap(new FlatMapFunction<ConsumerRecord<String, String>, String>() {

@Override

public Iterator<String> call(ConsumerRecord<String, String> stringStringConsumerRecord) throws Exception {

String[] split = stringStringConsumerRecord.value().split(" ");

return Arrays.asList(split).iterator();

}

});

JavaPairDStream<String, Integer> javaPairDStream = stringJavaDStream.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

JavaPairDStream<String, Integer> window = javaPairDStream.window(Duration.apply(12000), Duration.apply(6000));

window.reduceByKey(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1+v2;

}

}).print();

// 执行流的任务

javaStreamingContext.start();

javaStreamingContext.awaitTermination();

}

}
```

- 测试
```bash
[atguigu@hadoop102 ~]$ kafka-console-producer.sh --broker-list hadoop102:9092 --topic topicA

hello spark
```

- 如果有多批数据进入窗口，最终也会通过window操作变成统一的RDD处理。
![图片11.png](images/图片11.png)

### 3.2.3 reduceByKeyAndWindow

- 基本语法：
- reduceByKeyAndWindow(func, windowLength, slideInterval, [numTasks])：当在一个(K,V)对的DStream上调用此函数，会返回一个新(K,V)对的DStream，此处通过对滑动窗口中批次数据使用reduce函数来整合每个key的value值。
- 需求：
统计WordCount：3秒一个批次，窗口12秒，滑步6秒。

- 代码编写：

```java
package com.atguigu;

import org.apache.kafka.clients.consumer.ConsumerConfig;

import org.apache.kafka.clients.consumer.ConsumerRecord;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import org.apache.spark.streaming.Duration;

import org.apache.spark.streaming.api.java.JavaDStream;

import org.apache.spark.streaming.api.java.JavaInputDStream;

import org.apache.spark.streaming.api.java.JavaPairDStream;

import org.apache.spark.streaming.api.java.JavaStreamingContext;

import org.apache.spark.streaming.kafka010.ConsumerStrategies;

import org.apache.spark.streaming.kafka010.KafkaUtils;

import org.apache.spark.streaming.kafka010.LocationStrategies;

import scala.Tuple2;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.HashMap;

import java.util.Iterator;

public class Test03_ReduceByKeyAndWindow {

public static void main(String[] args) throws InterruptedException {

// 创建流环境

JavaStreamingContext javaStreamingContext = new JavaStreamingContext("local[*]", "window", Duration.apply(3000L));

// 创建配置参数

HashMap<String, Object> map = new HashMap<>();

map.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,"hadoop102:9092,hadoop103:9092,hadoop104:9092");

map.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.GROUP_ID_CONFIG,"atguigu");

map.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

// 需要消费的主题

ArrayList<String> strings = new ArrayList<>();

strings.add("topicA");

JavaInputDStream<ConsumerRecord<String, String>> directStream = KafkaUtils.createDirectStream(javaStreamingContext, LocationStrategies.PreferBrokers(), ConsumerStrategies.<String, String>Subscribe(strings,map));

JavaDStream<String> stringJavaDStream = directStream.flatMap(new FlatMapFunction<ConsumerRecord<String, String>, String>() {

@Override

public Iterator<String> call(ConsumerRecord<String, String> stringStringConsumerRecord) throws Exception {

String[] split = stringStringConsumerRecord.value().split(" ");

return Arrays.asList(split).iterator();

}

});

JavaPairDStream<String, Integer> javaPairDStream = stringJavaDStream.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

javaPairDStream.reduceByKeyAndWindow(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

},Duration.apply(12000L),Duration.apply(6000L)).print();

// 执行流的任务

javaStreamingContext.start();

javaStreamingContext.awaitTermination();

}

}
```

- 测试
```bash
[atguigu@hadoop102 ~]$ kafka-console-producer.sh --broker-list hadoop102:9092 --topic topicA

hello spark
```

# 4 DStream输出

DStream通常将数据输出到，外部数据库或屏幕上。

DStream与RDD中的惰性求值类似，如果一个DStream及其派生出的DStream都没有被执行输出操作，那么这些DStream就都不会被求值。如果StreamingContext中没有设定输出操作，整个Context就都不会启动。

- 输出操作API如下：
- saveAsTextFiles(prefix, [suffix])：以text文件形式存储这个DStream的内容。每一批次的存储文件名基于参数中的prefix和suffix。"prefix-Time_IN_MS[.suffix]"。
注意：以上操作都是每一批次写出一次，会产生大量小文件，在生产环境，很少使用。

- print()：在运行流程序的驱动结点上打印DStream中每一批次数据的最开始10个元素。这用于开发和调试。
- foreachRDD(func)：这是最通用的输出操作，即将函数func用于产生DStream的每一个RDD。其中参数传入的函数func应该实现将每一个RDD中数据推送到外部系统，如将RDD存入文件或者写入数据库。
在企业开发中通常采用foreachRDD()，它用来对DStream中的RDD进行任意计算。这和transform()有些类似，都可以让我们访问任意RDD。在foreachRDD()中，可以重用我们在Spark中实现的所有行动操作(action算子)。比如，常见的用例之一是把数据写到如MySQL的外部数据库中。

```java
package com.atguigu;

import org.apache.kafka.clients.consumer.ConsumerConfig;

import org.apache.kafka.clients.consumer.ConsumerRecord;

import org.apache.spark.api.java.JavaPairRDD;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import org.apache.spark.api.java.function.VoidFunction;

import org.apache.spark.streaming.Duration;

import org.apache.spark.streaming.api.java.JavaDStream;

import org.apache.spark.streaming.api.java.JavaInputDStream;

import org.apache.spark.streaming.api.java.JavaPairDStream;

import org.apache.spark.streaming.api.java.JavaStreamingContext;

import org.apache.spark.streaming.kafka010.ConsumerStrategies;

import org.apache.spark.streaming.kafka010.KafkaUtils;

import org.apache.spark.streaming.kafka010.LocationStrategies;

import scala.Tuple2;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.HashMap;

import java.util.Iterator;

/**

* @author yhm

* @create 2022-09-01 16:47

*/

public class Test04_Save {

public static void main(String[] args) throws InterruptedException {

// 创建流环境

JavaStreamingContext javaStreamingContext = new JavaStreamingContext("local[*]", "window", Duration.apply(3000L));

// 创建配置参数

HashMap<String, Object> map = new HashMap<>();

map.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,"hadoop102:9092,hadoop103:9092,hadoop104:9092");

map.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.GROUP_ID_CONFIG,"atguigu");

map.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

// 需要消费的主题

ArrayList<String> strings = new ArrayList<>();

strings.add("topicA");

JavaInputDStream<ConsumerRecord<String, String>> directStream = KafkaUtils.createDirectStream(javaStreamingContext, LocationStrategies.PreferBrokers(), ConsumerStrategies.<String, String>Subscribe(strings,map));

JavaDStream<String> stringJavaDStream = directStream.flatMap(new FlatMapFunction<ConsumerRecord<String, String>, String>() {

@Override

public Iterator<String> call(ConsumerRecord<String, String> stringStringConsumerRecord) throws Exception {

String[] split = stringStringConsumerRecord.value().split(" ");

return Arrays.asList(split).iterator();

}

});

JavaPairDStream<String, Integer> javaPairDStream = stringJavaDStream.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

JavaPairDStream<String, Integer> resultDStream = javaPairDStream.reduceByKeyAndWindow(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

}, Duration.apply(12000L), Duration.apply(6000L));

resultDStream.foreachRDD(new VoidFunction<JavaPairRDD<String, Integer>>() {

@Override

public void call(JavaPairRDD<String, Integer> stringIntegerJavaPairRDD) throws Exception {

// 获取mysql连接

// 写入到mysql中

// 关闭连接

}

});

// 执行流的任务

javaStreamingContext.start();

javaStreamingContext.awaitTermination();

}

}
```

# 5 优雅关闭

流式任务需要7*24小时执行，但是有时涉及到升级代码需要主动停止程序，但是分布式程序，没办法做到一个个进程去杀死，所以配置优雅的关闭就显得至关重要了。

关闭方式：使用外部文件系统来控制内部程序关闭。

- 主程序

```java
package com.atguigu;

import org.apache.hadoop.conf.Configuration;

import org.apache.hadoop.fs.FileSystem;

import org.apache.hadoop.fs.Path;

import org.apache.kafka.clients.consumer.ConsumerConfig;

import org.apache.kafka.clients.consumer.ConsumerRecord;

import org.apache.spark.api.java.function.FlatMapFunction;

import org.apache.spark.api.java.function.Function2;

import org.apache.spark.api.java.function.PairFunction;

import org.apache.spark.streaming.Duration;

import org.apache.spark.streaming.StreamingContextState;

import org.apache.spark.streaming.api.java.JavaDStream;

import org.apache.spark.streaming.api.java.JavaInputDStream;

import org.apache.spark.streaming.api.java.JavaPairDStream;

import org.apache.spark.streaming.api.java.JavaStreamingContext;

import org.apache.spark.streaming.kafka010.ConsumerStrategies;

import org.apache.spark.streaming.kafka010.KafkaUtils;

import org.apache.spark.streaming.kafka010.LocationStrategies;

import scala.Tuple2;

import java.net.URI;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.HashMap;

import java.util.Iterator;

public class Test05_Close {

public static void main(String[] args) throws InterruptedException {

// 创建流环境

JavaStreamingContext javaStreamingContext = new JavaStreamingContext("local[*]", "window", Duration.apply(3000L));

// 创建配置参数

HashMap<String, Object> map = new HashMap<>();

map.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,"hadoop102:9092,hadoop103:9092,hadoop104:9092");

map.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

map.put(ConsumerConfig.GROUP_ID_CONFIG,"atguigu");

map.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"latest");

// 需要消费的主题

ArrayList<String> strings = new ArrayList<>();

strings.add("topicA");

JavaInputDStream<ConsumerRecord<String, String>> directStream = KafkaUtils.createDirectStream(javaStreamingContext, LocationStrategies.PreferBrokers(), ConsumerStrategies.<String, String>Subscribe(strings,map));

JavaDStream<String> stringJavaDStream = directStream.flatMap(new FlatMapFunction<ConsumerRecord<String, String>, String>() {

@Override

public Iterator<String> call(ConsumerRecord<String, String> stringStringConsumerRecord) throws Exception {

String[] split = stringStringConsumerRecord.value().split(" ");

return Arrays.asList(split).iterator();

}

});

JavaPairDStream<String, Integer> javaPairDStream = stringJavaDStream.mapToPair(new PairFunction<String, String, Integer>() {

@Override

public Tuple2<String, Integer> call(String s) throws Exception {

return new Tuple2<>(s, 1);

}

});

javaPairDStream.reduceByKeyAndWindow(new Function2<Integer, Integer, Integer>() {

@Override

public Integer call(Integer v1, Integer v2) throws Exception {

return v1 + v2;

}

},Duration.apply(12000L),Duration.apply(6000L)).print();

// 开启监控程序

new Thread(new MonitorStop(javaStreamingContext)).start();

// 执行流的任务

javaStreamingContext.start();

javaStreamingContext.awaitTermination();

}

public static class MonitorStop implements Runnable {

JavaStreamingContext javaStreamingContext = null;

public MonitorStop(JavaStreamingContext javaStreamingContext) {

this.javaStreamingContext = javaStreamingContext;

}

@Override

public void run() {

try {

FileSystem fs = FileSystem.get(new URI("hdfs://hadoop102:8020"), new Configuration(), "atguigu");

while (true){

Thread.sleep(5000);

boolean exists = fs.exists(new Path("hdfs://hadoop102:8020/stopSpark"));

if (exists){

StreamingContextState state = javaStreamingContext.getState();

// 获取当前任务是否正在运行

if (state == StreamingContextState.ACTIVE){

// 优雅关闭

javaStreamingContext.stop(true, true);

System.exit(0);

}

}

}

}catch (Exception e){

e.printStackTrace();

}

}

}

}
```

- 测试
  - 发送数据
```bash
[atguigu@hadoop102 ~]$ kafka-console-producer.sh --broker-list hadoop102:9092 --topic topicA

hello spark
```

  - 启动Hadoop集群
```bash
[atguigu@hadoop102 hadoop-3.1.3]$ sbin/start-dfs.sh

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -mkdir /stopSpark
```
