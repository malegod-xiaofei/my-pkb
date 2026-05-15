## Weaviate 介绍

Weaviate 是一个基于GO语言开发的开源的向量数据库。开源向量数据库（Vector Database），主要用于支持 AI、机器学习和语义搜索 场景。它通过将非结构化数据（文本、图像、视频等）转换为高维向量，并存储和索引这些向量，从而实现高效的 相似度搜索（nearest neighbor search, ANN） 和 知识检索。

## 核心功能

向量存储与检索  
支持高效存储数十亿级别的向量，并进行 ANN（Approximate Nearest Neighbor）检索。  
内置多种 ANN 索引（HNSW 等），保证低延迟、高性能。

多模态数据支持

- 文本（自然语言文档）
- 图像（embedding 后的向量）
- 视频、音频（需转换 embedding）

Schema 与 Graph

- 支持 模式化存储（类似数据库表）
- 支持对象间的 关系（类似图数据库），可做语义 + 关系联合查询

混合搜索（Hybrid Search）

- 向量搜索 + 关键字搜索结合
- BM25 + ANN 同时使用，既能保证语义相关性，也能兼顾关键字精准性

集成预训练模型

- 内置 Transformer 模型（如 OpenAI、Cohere、Hugging Face 模型）
- 可直接用 Weaviate 提供的模块生成向量，无需单独部署 embedding 服务

## 使用场景

语义搜索：用户输入自然语言，Weaviate 能够在文档库中找到语义相关的内容（而非仅仅依赖关键词匹配）。

推荐系统：基于向量相似度的推荐，比如用户相似度、商品相似度。

RAG（Retrieval-Augmented Generation）：大模型（LLM）与知识库结合，Weaviate 提供高效检索接口，给 LLM 提供上下文。

多模态搜索：比如用一张图片查找相似的图片或相关的文本描述。

## 技术特点

水平扩展：支持集群化部署，能处理海量数据。

高性能索引：默认使用 HNSW（Hierarchical Navigable Small World）图结构，检索速度快。

Graph + Vector 结合：不仅是向量数据库，也能存储实体关系，类似“知识图谱”。

REST / GraphQL API：原生支持 GraphQL 查询语言，也支持 RESTful API 和 gRPC。

## Weaviate 部署

## 部署方式

Weaviate支持以下四种部署方式：

Docker部署：Docker部署适用于开发和测试环境

Weaviate Cloud：Weaviate官方提供的Serverless方案，支持高可用、零停机时间，适用于生产环境

K8S部署：使用K8S部署Weaviate，可以用于开发或者生产环境。

嵌入式部署：嵌入式 Weaviate可以从应用程序中运行 Weaviate 实例，不需要从独立的服务器安装，嵌入式Weaviate目前仍处于实验阶段，并且不支持Windows系统。

## docker 部署

运行 Weaviate命令如下

```
docker run --name=weaviate -p 8080:8080 -p 50051:50051 -d -v /opt/docker/weaviate:/var/lib/weaviate cr.weaviate.io/semitechnologies/weaviate:1.32.6
```

-p 8080:8080： Weaviate 的 REST / GraphQL API 默认在 8080 提供服务。

-p 50051:50051： Weaviate 的gRPC 接口，适合高性能场景（比如大规模批量插入、低延迟检索）

-v： Weaviate 会把 索引数据、向量存储等持久化到容器内的 `/var/lib/weaviate`

## Weaviate 使用

Weaviate官方并没有提供可视化界面来查看和操作Weaviate数据库，下面我们通过Weaviate提供的Python 客户端来操作Weaviate数据库。

首先，在项目中安装Weaviate客户端依赖

```
pip install -U weaviate-client
```

在介绍Weaviate客户端使用之前，首先需要了解Weaviate的几个基础知识。

- 在Weaviate中，可以创建多个集合，用来保存数据
- 在Weaviate中，保存数据的载体是对象，在对象中可以包含向量信息（Vector）和属性信息（properties），这里的属性信息就是我们之前所说的元数据信息。
- 所有的对象都属于一个集合且仅属于一个集合

## 连接Weaviate

连接本地Weaviate数据库代码示例如下，指定host地址、端口号和grpc端口号。

```
import weaviate

client = weaviate.connect_to_local(
    host="localhost",
    port=8080,
    grpc_port=50051,
)

print(client.is_ready())
```

执行结果：

## 创建集合

在Weaviate中，可以通过create方法创建集合：

```
client.collections.create("Database")
```

## 创建对象

在集合Database中创建一个带向量和属性的对象，并且insert方法会返回一个uuid，这个uuid就是这个对象的唯一标识。

```
database = client.collections.get("Database")
uuid = database.data.insert(
    properties={
        "segment_id": "1000",
        "document_id": "1",
    },
    
    vector=[0.12345] * 1536
)

print(uuid)
```

执行结果：

```
a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1
```

也可以单独指定uuid，不让Weaviate自动生成，通过指定uuid属性，设置uuid

```
uuid = database.data.insert(
    properties={
        "segment_id": "1000",
        "document_id": "1",
    },
    
    vector=[0.12345] * 1536,
    uuid=uuid.uuid4()
)
```

## 批量导入对象

除了单个创建对象，还可以批量导入对象，预先生成5条数据和5个向量，使用批量导入将对象导入到集合中，并自己指定uuid，当出现失败数量超过10个时，则终止对象导入。

```
data_rows = [{"title": f"标题{i + 1}"} for i in range(5)]

vectors = [[0.1] * 1536for i in range(5)]

collection = client.collections.get("Database")

with collection.batch.fixed_size(batch_size=200) as batch:
    for i, data_row in enumerate(data_rows):
        
        batch.add_object(
            properties=data_row,
            vector=vectors[i],
            
            uuid=uuid.uuid4()
        )
        
        if batch.number_errors > 10:
            print("批量导入对象出现错误次数过多，终止执行")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"导入失败数量: {len(failed_objects)}")
    print(f"第一个导入失败对象: {failed_objects[0]}")
```

## 根据uuid查询对象

Weaviate支持通过uuid 检索对象。如果uuid不存在，将会返回 404 错误，这里还指定了include_vector属性为True表示除了返回对象元数据信息之外，同时返回向量信息，在打印向量时，读取vector的default属性是因为，在Weaviate对象可以保存多个向量信息，默认的向量名就是default。

```
database = client.collections.get("Database")


data_object = database.query.fetch_object_by_id(
    "a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1",
    include_vector=True
)


print(data_object.properties)
print(data_object.vector["default"])
```

执行结果如下：

```
{'document_id': '1', 'segment_id': '1000', 'title': None}
[0.12345000356435776, 0.12345000356435776, 0.12345000356435776, 省略部分数据...]
```

## 查询所有对象

Weaviate 提供了相关API来遍历集合所有的数据，这个方法在迁移数据时非常有用，通过如下方式可以遍历集合内的全部对象信息。

```
collection = client.collections.get("Database")

for item in collection.iterator(
    include_vector=True
):
    print(item.properties)
    print(item.vector)
```

执行结果如下，返回了元数据信息和向量信息。

```
{'title': '标题1', 'segment_id': None, 'document_id': None}
{'default': [0.10000000149011612, 0.10000000149011612, 省略部分数据...]}
{'document_id': None, 'segment_id': None, 'title': '标题2'}
{'default': [0.10000000149011612, 0.10000000149011612, 省略部分数据...]}

省略部分数据...
```

## 更新对象信息

Weaviate支持对对象部分更新，也支持对对象进行整体替换。

首先来介绍对象的部分更新，使用示例如下，根据uuid去更新对象属性信息、向量信息，没有指定更新的属性不会发生变化。

```
database = client.collections.get("Database")
database.data.update(
    uuid="a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1",
    
    properties={
        "segment_id": "2000",
    },
    
    vector=[1.0] * 1536
)
```

在执行上面的程序之前，uuid为a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1的向量信息如下。

```
{'document_id': '1', 'segment_id': '1000', 'title': None}
[0.12345000356435776, 0.12345000356435776, 0.12345000356435776, 省略部分数据...]
```

执行上述程序，重新查询该对象信息如下，数据已经修改成功，由于没有指定document_id因此该属性没有变化。

```
{'title': None, 'document_id': '1', 'segment_id': '2000'}
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 省略部分数据...]
```

除了使用update方法进行属性更新，也可以使用replace方法对整个对象数据进行替换，代码示例如下：

```
database = client.collections.get("Database")
database.data.replace(
    uuid="a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1",
    properties={
        "segment_id": "3000",
    },
    vector=[1.0] * 1536
)
```

执行成功之后，重新查询对象信息，可以看到除了segment_id属性和向量信息都进行更新之外，document_id也被设置为None，因此可以判断整个对象进行了替换。

```
{'document_id': None, 'segment_id': '3000', 'title': None}
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 省略部分数据...]
```

## 删除对象

Weaviate支持按uuid删除、批量删除、删除全部三种删除方式。

按照uuid删除方法

```
database = client.collections.get("Database")
database.data.delete_by_id(
    "a60f4b19-9c97-4eb0-ba02-8c7b0a6cfcb1"
)
```

按条件批量删除方法，使用示例如下，对属性title进行模糊匹配，匹配成功的对象将会被删除。

```
database = client.collections.get("Database")
database.data.delete_many(
    where=Filter.by_property("title").like("标题*")
)
```

所有对象都属于一个集合，因此删除集合就相当于删除全部对象，删除集合方法如下：

```
client.collections.delete(
    "Database"
)
```
