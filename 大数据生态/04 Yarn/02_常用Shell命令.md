## 0.1 Yarn 常用命令

Yarn状态的查询，除了可以在hadoop103:8088页面查看外，还可以通过命令操作。常见的命令操作如下所示：

需求：执行WordCount案例，并用Yarn命令查看任务运行情况。

[atguigu@hadoop102 hadoop-3.1.3]$ myhadoop.sh start

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.3.jar wordcount /input1 /output1

### 0.1.1 yarn application 查看任务

- 列出所有Application：
[atguigu@hadoop102 hadoop-3.1.3]$ yarn application -list

2021-02-06 10:21:19,238 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Total number of applications (application-types: [], states: [SUBMITTED, ACCEPTED, RUNNING] and tags: []):0

Application-Id    Application-Name    Application-Type      User     Queue             State       Final-State       Progress                       Tracking-URL

- 根据Application状态过滤：yarn application -list -appStates （所有状态：ALL、NEW、NEW_SAVING、SUBMITTED、ACCEPTED、RUNNING、FINISHED、FAILED、KILLED）
[atguigu@hadoop102 hadoop-3.1.3]$ yarn application -list -appStates FINISHED

2021-02-06 10:22:20,029 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Total number of applications (application-types: [], states: [FINISHED] and tags: []):1

Application-Id    Application-Name    Application-Type      User     Queue             State       Final-State       Progress                       Tracking-URL

application_1612577921195_0001          word count           MAPREDUCE   atguigu   default          FINISHED         SUCCEEDED           100%http://hadoop102:19888/jobhistory/job/job_1612577921195_0001

- Kill掉Application：
[atguigu@hadoop102 hadoop-3.1.3]$ yarn application -kill application_1612577921195_0001

2021-02-06 10:23:48,530 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Application application_1612577921195_0001 has already finished

### 0.1.2 yarn logs 查看日志

- 查询Application日志：yarn logs -applicationId <`ApplicationId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn logs -applicationId application_1612577921195_0001

- 查询Container日志：yarn logs -applicationId <`ApplicationId`> -containerId <`ContainerId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn logs -applicationId application_1722054637370_0001 -containerId container_1722054637370_0001_01_000001

### 0.1.3 yarn applicationattempt 查看尝试运行的任务

- 列出所有Application尝试的列表：yarn applicationattempt -list <`ApplicationId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn applicationattempt -list application_1722054637370_0001

2021-02-06 10:26:54,195 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Total number of application attempts :1

ApplicationAttempt-Id               State                    AM-Container-Id                       Tracking-URL

appattempt_1612577921195_0001_000001            FINISHEDcontainer_1612577921195_0001_01_000001http://hadoop103:8088/proxy/application_1612577921195_0001/

- 打印ApplicationAttemp状态：yarn applicationattempt -status <`ApplicationAttemptId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn applicationattempt -status appattempt_1722054637370_0001_000001

2021-02-06 10:27:55,896 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Application Attempt Report :

ApplicationAttempt-Id : appattempt_1612577921195_0001_000001

State : FINISHED

AMContainer : container_1612577921195_0001_01_000001

Tracking-URL : http://hadoop103:8088/proxy/application_1612577921195_0001/

RPC Port : 34756

AM Host : hadoop104

Diagnostics :

### 0.1.4 yarn container 查看容器

- 列出所有Container：yarn container -list <`ApplicationAttemptId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn container -list appattempt_1722054637370_0001_000001

2021-02-06 10:28:41,396 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Total number of containers :0

Container-Id          Start Time         Finish Time               State                Host   Node Http Address

- 打印Container状态：yarn container -status <`ContainerId`>
[atguigu@hadoop102 hadoop-3.1.3]$ yarn container -status appattempt_1722054637370_0001_000001

2021-02-06 10:29:58,554 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Container with id 'container_1612577921195_0001_01_000001' doesn't exist in RM or Timeline Server.

注：只有在任务跑的途中才能看到container的状态

### 0.1.5 yarn node 查看节点状态

列出所有节点：yarn node -list -all

[atguigu@hadoop102 hadoop-3.1.3]$ yarn node -list -all

2021-02-06 10:31:36,962 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Total Nodes:3

Node-Id     Node-StateNode-Http-AddressNumber-of-Running-Containers

hadoop103:38168        RUNNING   hadoop103:8042                           0

hadoop102:42012        RUNNING   hadoop102:8042                           0

hadoop104:39702        RUNNING   hadoop104:8042                           0

### 0.1.6 yarn rmadmin 更新配置

加载队列配置：yarn rmadmin -refreshQueues

[atguigu@hadoop102 hadoop-3.1.3]$ yarn rmadmin -refreshQueues

2021-02-06 10:32:03,331 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8033

### 0.1.7 yarn queue 查看队列

打印队列信息：yarn queue -status <`QueueName`>

[atguigu@hadoop102 hadoop-3.1.3]$ yarn queue -status default

2021-02-06 10:32:33,403 INFO client.RMProxy: Connecting to ResourceManager at hadoop103/192.168.10.103:8032

Queue Information :

Queue Name : default

State : RUNNING

Capacity : 100.0%

Current Capacity : .0%

Maximum Capacity : 100.0%

Default Node Label expression : <DEFAULT_PARTITION>

Accessible Node Labels : *

Preemption : disabled

Intra-queue Preemption : disabled

## 0.2 Yarn 生产环境核心参数

![图片26.png](images/图片26.png)

调度器选择：大公司选公平，小公司选容量
