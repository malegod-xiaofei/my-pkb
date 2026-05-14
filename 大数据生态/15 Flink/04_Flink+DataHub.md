- 在DataHub中找到对应的Topic，添加订阅
  - 订阅应用和描述尽量有区分，让别人知道这是谁在干嘛
- 往Topic中写入一些测试数据，这里就直接上代码，每隔一分钟往DataHub写入三条数据
```java

public class dataHubProducer {

public static int result = 123;

public static void main(String[] args) throws InterruptedException {

while (1 == 1) {

tupleExample("test_crawler_dh", "ods_kuaishou_good_detail_df", 1);

Thread.sleep(60000);

}

}

// 写入Tuple型数据

public static void tupleExample(String project, String topic, int retryTimes) {

// Endpoint以Region: 华东1为例，其他Region请按实际情况填写

String endpoint = "http://dh-cn-beijing.aliyuncs.com";

String accessId = "xxx";

String accessKey = "xxx";

// 创建DataHubClient实例

DatahubClient datahubClient = DatahubClientBuilder.newBuilder()

.setDatahubConfig(

new DatahubConfig(endpoint,

// 是否开启二进制传输，服务端2.12版本开始支持

new AliyunAccount(accessId, accessKey), true))

//专有云使用出错尝试将参数设置为           false

// HttpConfig可不设置，不设置时采用默认值

.setHttpConfig(new HttpConfig()

.setCompressType(HttpConfig.CompressType.LZ4) // 读写数据推荐打开网络传输 LZ4压缩

.setConnTimeout(10000))

.build();

// 获取schema

RecordSchema recordSchema = datahubClient.getTopic(project, topic).getRecordSchema();

// 生成十条数据

List<RecordEntry> recordEntries = new ArrayList<>();

Date date = new Date();

for (int i = 0; i < 3; ++i) {

RecordEntry recordEntry = new RecordEntry();

// 对每条数据设置额外属性，例如ip 机器名等。可以不设置额外属性，不影响数据写入

recordEntry.addAttribute("key1", "value1");

TupleRecordData data = new TupleRecordData(recordSchema);

data.setField("good_id", result + "" + i + "z");

data.setField("title", "这是一个 测试 title");

data.setField("goodurl", "www.baidu.com");

data.setField("images", "123.png");

data.setField("base_info", "店家很懒，什么也没有写");

data.setField("lastcategoryid", "10099");

data.setField("brand_id", "欧莱雅");

data.setField("live_id", result + "" + i + "y");

data.setField("anchor_id", result + "" + i + "f");

data.setField("crawl_date", (int) (date.getTime() / 1000));

recordEntry.setRecordData(data);

recordEntries.add(recordEntry);

}

result = result + 3;

System.out.println((int) (date.getTime() / 1000) + "生产结束 ! ");

try {

PutRecordsResult result = datahubClient.putRecords(project, topic, recordEntries);

int i = result.getFailedRecordCount();

if (i > 0) {

retry(datahubClient, result.getFailedRecords(), retryTimes, project, topic);

}

} catch (DatahubClientException e) {

System.out.println("requestId:" + e.getRequestId() + "\tmessage:" + e.getErrorMessage());

}

}

//重试机制

public static void retry(DatahubClient client, List<RecordEntry> records, int retryTimes, String project, String topic) {

boolean suc = false;

while (retryTimes != 0) {

retryTimes = retryTimes - 1;

PutRecordsResult recordsResult = client.putRecords(project, topic, records);

if (recordsResult.getFailedRecordCount() > 0) {

retry(client, recordsResult.getFailedRecords(), retryTimes, project, topic);

}

suc = true;

break;

}

if (!suc) {

System.out.println("retryFailure");

}

}

}
```
- 创建消费者订阅Topic，
注意这里有一个SUB_ID，这是你第一步生成的订阅ID。时间戳精确到毫秒，这里 Tuple25 函数只有能读取到25，目前是DataHub中的数据表不能超过25列，
```java
public class DatahubSourceDemo implements Serializable {

private static final long serialVersionUID = 1L;

private static final String ENDPOINT = "http://dh-cn-beijing.aliyuncs.com";

private static final String PROJECT_NAME = "test_crawler_dh";

private static final String TOPIC_NAME = "ods_kuaishou_good_detail_df";

private static final String SUB_ID = "1637138056862Q4ART";

private static final String ACCESS_ID = "xxx";

private static final String ACCESS_KEY = "xx";

public void runExample() throws Exception {

StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

env.setParallelism(1);

DatahubSourceFunction datahubSource =

new DatahubSourceFunction(

ENDPOINT,

PROJECT_NAME,

TOPIC_NAME,

SUB_ID,

ACCESS_ID,

ACCESS_KEY,

1637164800000L,

1637251200000L);

datahubSource.setRequestTimeout(30 * 1000);

datahubSource.enableExitAfterReadFinished();

env.addSource(datahubSource)

.map((MapFunction<RecordEntry, Tuple25<String, String, String, String, String, String, String, String, String, String, String, String, String, Boolean, String, String, String, String, String, String, String, String, Boolean, String, String>>) this::getTuple25)

.print();

env.execute();

}

private Tuple25<String, String, String, String, String, String, String, String, String, String, String, String, String, Boolean, String, String, String, String, String, String, String, String, Boolean, String, String> getTuple25(RecordEntry recordEntry) {

Tuple25<String, String, String, String, String, String, String, String, String, String, String, String, String, Boolean, String, String, String, String, String, String, String, String, Boolean, String, String> tuple2 = new Tuple25<>();

TupleRecordData recordData = (TupleRecordData) (recordEntry.getRecordData());

tuple2.f0 = (String) recordData.getField(0);

tuple2.f1 = (String) recordData.getField(1);

tuple2.f2 = (String) recordData.getField(2);

tuple2.f3 = (String) recordData.getField(3);

tuple2.f4 = (String) recordData.getField(4);

tuple2.f5 = (String) recordData.getField(5);

tuple2.f6 = (String) recordData.getField(6);

tuple2.f7 = (String) recordData.getField(7);

tuple2.f8 = (String) recordData.getField(8);

tuple2.f9 = (String) recordData.getField(9);

tuple2.f10 = (String) recordData.getField(10);

tuple2.f12 = (String) recordData.getField(12);

tuple2.f13 = (Boolean) recordData.getField(13);

tuple2.f14 = (String) recordData.getField(14);

tuple2.f15 = (String) recordData.getField(15);

tuple2.f16 = (String) recordData.getField(16);

tuple2.f17 = (String) recordData.getField(17);

tuple2.f18 = (String) recordData.getField(18);

tuple2.f19 = (String) recordData.getField(19);

tuple2.f20 = (String) recordData.getField(20);

tuple2.f21 = (String) recordData.getField(21);

tuple2.f22 = (Boolean) recordData.getField(22);

tuple2.f23 = (String) recordData.getField(23);

tuple2.f24 = (String) recordData.getField(24);

return tuple2;

}

public static void main(String[] args) throws Exception {

DatahubSourceDemo sourceFunctionExample = new DatahubSourceDemo();

sourceFunctionExample.runExample();

}

}
```