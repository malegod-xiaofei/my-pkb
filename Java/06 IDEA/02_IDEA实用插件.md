- 复制类名全称

![图片33.png](images/图片33.png)

  - 之后再粘贴就是包名.类名的方式
- Lombok
  - 在Plugins中下载Lombok插件
  - 添加pom文件

```
<!--配置 JavaBean-->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.16.6</version>
</dependency>
```

  - 然后就可以一键生成JavaBean啦，使用注解生成Get、Set、构造方法、ToString

```java
package com.atguigu.apitest.beans;

import lombok.*;

/**
* 传感器温度读数的数据类型
*
* @author Malegod_xiaofei
* @create 2021-12-25-20:49
*/
@Data
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class SensorReading {
    // 属性：id，时间戳，温度值
    private String id;
    private Long timestamp;
    private Double temperature;
}
```
