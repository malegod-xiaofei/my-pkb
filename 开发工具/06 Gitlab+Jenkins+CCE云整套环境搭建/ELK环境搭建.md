# 环境说明
方案：使用ElasticSearch保存日志，使用Kibana进行日志展示、搜索、过期删除，使用 ElasticSearch 的pipeline进行日志的解析，使用 filebeat 采集日志发送给ElasticSearch。使用服务器`192.168.xxx.xxx`进行部署。

  


准备：

+ 从官网下载 ElasticSearch（elasticsearch-8.15.0-linux-x86_64.tar.gz）上传到服务器
+ 从官网下载 kibana（kibana-8.15.0-linux-x86_64.tar.gz）上传到服务器
+ 从官网下载 `elastic/filebeat` 的docker镜像，推送到cce镜像仓库

  


# 部署环境
## 环境检查
检查`vm.max_map_count`的大小，要求该值至少为`262144`：

```shell
sysctl -n vm.max_map_count
```

如果该值不满足要求，可以修改`/etc/sysctl.conf`文件，在该文件中新增一行或者修改`vm.max_map_count`：

```properties
vm.max_map_count=262144
```

  


检查`ulimit`的值：

```shell
# 检查ulimit的值
ulimit -n
```

修改`ulimit`的值为`65536`：

```shell
ulimit -n 65536
```

  


配置防火墙：

```shell
# 开启elasticsearch、kibana的相关端口
firewall-cmd --zone=public --add-port=9200/tcp --permanent
firewall-cmd --zone=public --add-port=9300/tcp --permanent
firewall-cmd --zon=public --add-service=http --permanent
firewall-cmd --zone=public --add-port=5601/tcp --permanent
firewall-cmd --reload
```

  


## 部署ElasticSearch
将 ElasticSearch 解压：

```shell
tar -zxvf elasticsearch-8.15.0-linux-x86_64.tar.gz
```

调整 ElasticSearch的配置文件：`config/elasticsearch.yml`：

```yaml
cluster.name: elk-cluster
node.name: node-1
path.data: /home/elk/elasticsearch-workspace/data
path.logs: /home/elk/elasticsearch-workspace/logs

network.host: 0.0.0.0
cluster.initial_master_nodes: ["node-1"]
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
# CA 证书名称为下面步骤中生成的CA证书名称
xpack.security.transport.ssl.keystore.path: elasticsearch-certificates.p12
xpack.security.transport.ssl.truststore.path: elasticsearch-certificates.p12
```

创建对应的文件夹：

+ /home/elk/elasticsearch-workspace/data：数据文件夹
+ /home/elk/elasticsearch-workspace/logs：日志文件夹

  


生成证书：

1. 生成CA：

```shell
# 生成CA，一路回车
# 默认的ca文件为 config/elastic-stack-ca.p12
bin/elasticsearch-certutil ca
```

1. 通过CA生成证书：

```shell
# 在config下生成证书elasticsearch-certificates.p12
bin/elasticsearch-certutil cert -out config/elasticsearch-certificates.p12 -pass "" --ca elastic-stack-ca.p12
```

  


启动ElasticSearch：

```shell
# -d 后台启动
bin/elasticsearch -d
```

配置用户密码：

```shell
# interactive交互式启动（即自己设置密码）
# 执行后会提示为相关用户设置密码。为方便记忆，此处全部设置为123456
bin/elasticsearch-setup-passwords interactive
```

  


访问ElasticSearch：[http://192.168.xxx.xxx:9200](http://192.168.xxx.xxx:9200)

如果提示需要用户密码，输入用户`elastic`，密码`123456`（即上面设置的密码）

  


关闭elasticsearch：

```shell
# 查看elastic相关进程进行kill
ps -ef | grep elastic
```

  


## 部署kibana
解压Kibana：

```shell
tar -zxvf kibana-8.15.0-linux-x86_64.tar.gz
```

调整Kibana配置文件：`config/kibana.yml`

```yaml
# 端口号，默认5601
server.port: 5601
# 设置为0.0.0.0，允许访问
server.host: "0.0.0.0"

# 填写elastic的地址、用户、密码等信息
elasticsearch.hosts: ["http://localhost:9200"]
elasticsearch.username: "kibana"
elasticsearch.password: "123456"
# 设置publicBaseUrl，最后面不要带斜杠
server.publicBaseUrl: "http://192.168.xxx.xxx:5601"

# 设置国际化语言中文
i18n.locale: "zh-CN"
```

  


启动kibana：

```shell
# nohup方式访问
nohup ./bin/kibana &
```

  


访问kibana：[http://192.168.xxx.xxx:5601/](http://192.168.xxx.xxx:5601/)

如果提示需要用户密码，输入用户`elastic`，密码`123456`（即elasticsearch设置的密码）

  


关闭Kibana：

```shell
# kibana会启动一个node进程，查看node相关进程，进行kill
ps -ef | grep node
```

  


## 配置项目的日志格式
调整项目的日志格式，使其成为固定格式，例如：

```xml
<!--按空格拆分：[0 1]时间-date [2]追踪ID [3]用户 [4]线程名称-thread [5]日志等级-level [6]logger类名-class [7]主要信息-message   -->
<property name="ENCODER_PATTERN" value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%X{log_opid}] [%X{log_userid }] [%thread] %-5level %logger{80} - %msg%n" />
```

调整日志的输出路径、日志名称、日志级别等信息

  


## 配置项目的ELK索引信息
通过向ElasticSearch发送相关请求，创建项目的索引信息。

创建生命周期策略`myproject-strategy`：

```json
// PUT _ilm/policy/myproject-strategy
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "set_priority": {
            "priority": 100
          }
        }
      },
        // 超过7天的删除
      "delete": {
        "min_age": "7d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```

  


创建索引模板：`myproject-app `

```json
// PUT _index_template/myproject-app  
{
  "template": {
    "settings": {
      "index": {
        "lifecycle": {
          "name": "myproject-strategy"  
        }
      }
    }
  },
  "index_patterns": [
    "myproject-app-*"  
  ]
}
```

  


创建pipeline：`myproject-logback-pipeline`

```json
// PUT _ingest/pipeline/myproject-logback-pipeline

{
  "description": "logback-pipeline",
  "processors": [
    {
      "split": {
        "field": "message",
        "target_field": "message_array",
        "separator": "\\s+"
      }
    },
    {
      "set": {
        "field": "log_date",
        "if": "ctx.message_array.length>0",
        "value": "{{message_array.0}}"
      }
    },
    {
      "set": {
        "field": "log_timestamp_array",
        "if": "ctx.message_array.length>0 && ctx.message_array.length>1",
        "value": ["{{message_array.0}}", "{{message_array.1}}"]
      }
    },
    {
      "join": {
        "field": "log_timestamp_array",
        "separator": " "
      }
    },
    {
      "date": {
        "field": "log_timestamp_array",
        "target_field": "log_timestamp",
        "formats": ["yyyy-MM-dd HH:mm:ss.SSS"],
        "timezone": "Asia/Shanghai"
      }
    },
    {
      "set": {
        "field": "log_opid",
        "if": "ctx.message_array.length>2",
        "value": "{{message_array.2}}"
      }
    },
    {
      "set": {
        "field": "log_userid",
        "if": "ctx.message_array.length>3",
        "value": "{{message_array.3}}"
      }
    },
    {
      "set": {
        "field": "thread",
        "if": "ctx.message_array.length>4",
        "value": "{{message_array.4}}"
      }
    },
    {
      "set": {
        "field": "level",
        "if": "ctx.message_array.length>5",
        "value": "{{message_array.5}}"
      }
    },
    {
      "set": {
        "field": "logger",
        "if": "ctx.message_array.length>6",
        "value": "{{message_array.6}}"
      }
    },
    {
      "remove": {
        "field": "message_array"
      }
    }
  ]
}
```

  


## 部署filebeat
filebeat需要能够读取到云上myproject项目的日志，所以需要将myproject项目的日志映射出来。可以使用以下几种方案：

+ 方案1：使用PVC，将项目日志映射到PVC上，filebeat也挂载该PVC，读取其中的日志
+ 方案2：filebeat配置节点亲和配置为亲和myproject项目，使得filebeat的pod和myproject项目pod运行在同一个节点。将myproject日志映射到节点主机`HostPath`上，filebeat也挂载主机的`HostPath`，读取其中的日志

CCE云上现在没有PVC配额，目前采用方案2。

  


添加一个ConfigMap `myproject-filebeat`：其中配置`filebeat.yml`

```yaml
filebeat.inputs:
  - type: filestream 
    enabled: true
    id: filestream-myproject-app
    paths:
      - /tmp/logs/myproject/myproject.log
    fields:
      sourceSystem: myproject-app
      profile: dev
      project: web
      level: all
      pod: ${POD_IP:"-"}
    fields_under_root: true
    parsers:
      - multiline:
          type: pattern
          pattern: '^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}\s\[[\w.-]*\]\s\[[\w.-]*\]\s\[[\w.-]*\]\s[A-Z]{4,5}\s'
          negate: true
          match: after

setup:
  template:  
    enabled: false
    name: "myproject-app"
    pattern: "myproject-app-*"
    overwrite: true
    settings:
      index.number_of_shards: 1  
  ilm: 
    enabled: false

output.elasticsearch:
  hosts: ["192.168.xxx.xxx:9200"]
  username: "elastic"
  password: "123456"
  index: "myproject-app-dev-%{+yyyy.MM.dd}" 
  pipeline: "myproject-logback-pipeline"
```

  


创建工作负载`myproject-filebeat`，镜像使用`elastic/filebeat:8.15.0`。

数据存储中，将`myproject-filebeat`的`filebeat.yml`挂载到`/usr/share/filebeat/filebeat.yml`（注意配置子路径）

将`HostPath`的`/tmp/logs/`挂载到容器的`/tmp/logs/`。

配置`应用亲和`，亲和` myproject-app`应用。

  


# 查看日志
访问Kibana即可查看相关日志：[http://192.168.xxx.xxx:5601/](http://192.168.xxx.xxx:5601/)
