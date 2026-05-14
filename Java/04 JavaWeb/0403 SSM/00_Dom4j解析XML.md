DOM4j解析 XML

pom.xml

<!-- dom4j 依赖包 -->

<dependency>

<groupId>dom4j</groupId>

<artifactId>dom4j</artifactId>

<version>1.6.1</version>

</dependency>

<!-- jaxen的包主要在使用Xpath时会被用到 -->

<dependency>

<groupId>jaxen</groupId>

<artifactId>jaxen</artifactId>

<version>1.1.6</version>

</dependency>

第一步 : // 创建SAXReader

```text
              // SAXReader reader = new SAXReader();
```

第二步 : 加载xml文件

Document document = DocumentHelper.parseText(input);

第三步 : // 获取根节点

Element root = document.getRootElement();

第四步 : // 记录最终结果集

String resultLast = "";

```java
              // System.out.println(root.elementText("content"));
              // System.out.println(root.elementText("time"));
              // System.out.println(root.elementText("repostsCount"));
              // System.out.println(root.elementText("commentsCount"));
              // 拼接最后的字符串
```

resultLast = resultLast + root.elementText("content") + "\t";

resultLast = resultLast + root.elementText("time") + "\t";

resultLast = resultLast + root.elementText("repostsCount") + "\t";

resultLast = resultLast + root.elementText("commentsCount");

```text
              return resultLast;
```

参考博客 :
