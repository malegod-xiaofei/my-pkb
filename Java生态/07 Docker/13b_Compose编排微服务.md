# Compose编排微服务

[目录](Docker与微服务实战.md) · [返回 Compose](13_Docker-compose容器编排.md#t-2-5-7)

<a id="t-2-5-7-1"></a>
## 改造升级微服务工程docker\_boot

<a id="t-2-5-7-1-1"></a>
### 以前的基础版

![配图](images/img-0294.png)

<a id="t-2-5-7-1-2"></a>
### SQL建表建库

CREATE TABLE \`t\_user\` (

\`id\` int(10) unsigned NOT NULL AUTO\_INCREMENT,

\`username\` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名',

\`password\` varchar(50) NOT NULL DEFAULT '' COMMENT '密码',

\`sex\` tinyint(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',

\`deleted\` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',

\`update\_time\` timestamp NOT NULL DEFAULT CURRENT\_TIMESTAMP ON UPDATE CURRENT\_TIMESTAMP COMMENT '更新时间',

\`create\_time\` timestamp NOT NULL DEFAULT CURRENT\_TIMESTAMP COMMENT '创建时间',

PRIMARY KEY (\`id\`)

) ENGINE=InnoDB AUTO\_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='用户表'

<a id="t-2-5-7-1-3"></a>
### 一键生成说明

<a id="t-2-5-7-1-4"></a>
### 改POM

&lt;?xml version="1.0" encoding="UTF-8"?>  
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">  
&lt;modelVersion>4.0.0&lt;/modelVersion>  
&lt;parent>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-parent&lt;/artifactId>  
&lt;version>2.5.6&lt;/version>  
&lt;!--&lt;version>2.3.10.RELEASE&lt;/version>-->  
&lt;relativePath/> &lt;!-- lookup parent from repository -->  
&lt;/parent>

&lt;groupId>com.atguigu.docker&lt;/groupId>  
&lt;artifactId>docker\_boot&lt;/artifactId>  
&lt;version>0.0.1-SNAPSHOT&lt;/version>

&lt;properties>  
&lt;project.build.sourceEncoding>UTF-8&lt;/project.build.sourceEncoding>  
&lt;maven.compiler.source>1.8&lt;/maven.compiler.source>  
&lt;maven.compiler.target>1.8&lt;/maven.compiler.target>  
&lt;junit.version>4.12&lt;/junit.version>  
&lt;log4j.version>1.2.17&lt;/log4j.version>  
&lt;lombok.version>1.16.18&lt;/lombok.version>  
&lt;mysql.version>5.1.47&lt;/mysql.version>  
&lt;druid.version>1.1.16&lt;/druid.version>  
&lt;mapper.version>4.1.5&lt;/mapper.version>  
&lt;mybatis.spring.boot.version>1.3.0&lt;/mybatis.spring.boot.version>  
&lt;/properties>

&lt;dependencies>  
&lt;!--guava Google 开源的 Guava 中自带的布隆过滤器-->  
&lt;dependency>  
&lt;groupId>com.google.guava&lt;/groupId>  
&lt;artifactId>guava&lt;/artifactId>  
&lt;version>23.0&lt;/version>  
&lt;/dependency>  
&lt;!-- redisson -->  
&lt;dependency>  
&lt;groupId>org.redisson&lt;/groupId>  
&lt;artifactId>redisson&lt;/artifactId>  
&lt;version>3.13.4&lt;/version>  
&lt;/dependency>  
&lt;!--SpringBoot通用依赖模块-->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-web&lt;/artifactId>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-actuator&lt;/artifactId>  
&lt;/dependency>  
&lt;!--swagger2-->  
&lt;dependency>  
&lt;groupId>io.springfox&lt;/groupId>  
&lt;artifactId>springfox-swagger2&lt;/artifactId>  
&lt;version>2.9.2&lt;/version>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>io.springfox&lt;/groupId>  
&lt;artifactId>springfox-swagger-ui&lt;/artifactId>  
&lt;version>2.9.2&lt;/version>  
&lt;/dependency>  
&lt;!--SpringBoot与Redis整合依赖-->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-data-redis&lt;/artifactId>  
&lt;/dependency>  
&lt;!--springCache-->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-cache&lt;/artifactId>  
&lt;/dependency>  
&lt;!--springCache连接池依赖包-->  
&lt;dependency>  
&lt;groupId>org.apache.commons&lt;/groupId>  
&lt;artifactId>commons-pool2&lt;/artifactId>  
&lt;/dependency>  
&lt;!-- jedis -->  
&lt;dependency>  
&lt;groupId>redis.clients&lt;/groupId>  
&lt;artifactId>jedis&lt;/artifactId>  
&lt;version>3.1.0&lt;/version>  
&lt;/dependency>  
&lt;!--Mysql数据库驱动-->  
&lt;dependency>  
&lt;groupId>mysql&lt;/groupId>  
&lt;artifactId>mysql-connector-java&lt;/artifactId>  
&lt;version>5.1.47&lt;/version>  
&lt;/dependency>  
&lt;!--SpringBoot集成druid连接池-->  
&lt;dependency>  
&lt;groupId>com.alibaba&lt;/groupId>  
&lt;artifactId>druid-spring-boot-starter&lt;/artifactId>  
&lt;version>1.1.10&lt;/version>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>com.alibaba&lt;/groupId>  
&lt;artifactId>druid&lt;/artifactId>  
&lt;version>${druid.version}&lt;/version>  
&lt;/dependency>  
&lt;!--mybatis和springboot整合-->  
&lt;dependency>  
&lt;groupId>org.mybatis.spring.boot&lt;/groupId>  
&lt;artifactId>mybatis-spring-boot-starter&lt;/artifactId>  
&lt;version>${mybatis.spring.boot.version}&lt;/version>  
&lt;/dependency>  
&lt;!-- 添加springboot对amqp的支持 -->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-amqp&lt;/artifactId>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>commons-codec&lt;/groupId>  
&lt;artifactId>commons-codec&lt;/artifactId>  
&lt;version>1.10&lt;/version>  
&lt;/dependency>  
&lt;!--通用基础配置junit/devtools/test/log4j/lombok/hutool-->  
&lt;!--hutool-->  
&lt;dependency>  
&lt;groupId>cn.hutool&lt;/groupId>  
&lt;artifactId>hutool-all&lt;/artifactId>  
&lt;version>5.2.3&lt;/version>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>junit&lt;/groupId>  
&lt;artifactId>junit&lt;/artifactId>  
&lt;version>${junit.version}&lt;/version>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-devtools&lt;/artifactId>  
&lt;scope>runtime&lt;/scope>  
&lt;optional>true&lt;/optional>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-test&lt;/artifactId>  
&lt;scope>test&lt;/scope>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>log4j&lt;/groupId>  
&lt;artifactId>log4j&lt;/artifactId>  
&lt;version>${log4j.version}&lt;/version>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>org.projectlombok&lt;/groupId>  
&lt;artifactId>lombok&lt;/artifactId>  
&lt;version>${lombok.version}&lt;/version>  
&lt;optional>true&lt;/optional>  
&lt;/dependency>  
&lt;!--persistence-->  
&lt;dependency>  
&lt;groupId>javax.persistence&lt;/groupId>  
&lt;artifactId>persistence-api&lt;/artifactId>  
&lt;version>1.0.2&lt;/version>  
&lt;/dependency>  
&lt;!--通用Mapper-->  
&lt;dependency>  
&lt;groupId>tk.mybatis&lt;/groupId>  
&lt;artifactId>mapper&lt;/artifactId>  
&lt;version>${mapper.version}&lt;/version>  
&lt;/dependency>  
&lt;/dependencies>

&lt;build>  
&lt;plugins>  
&lt;plugin>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-maven-plugin&lt;/artifactId>  
&lt;/plugin>  
&lt;plugin>  
&lt;groupId>org.apache.maven.plugins&lt;/groupId>  
&lt;artifactId>maven-resources-plugin&lt;/artifactId>  
&lt;version>3.1.0&lt;/version>  
&lt;/plugin>  
&lt;/plugins>  
&lt;/build>

&lt;/project>

<a id="t-2-5-7-1-5"></a>
### 写YML

server.port=6001  
\# ========================alibaba.druid相关配置=====================  
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource  
spring.datasource.driver-class-name=com.mysql.jdbc.Driver  
spring.datasource.url=jdbc:mysql://192.168.111.169:3306/db2021?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false  
spring.datasource.username=root  
spring.datasource.password=123456  
spring.datasource.druid.test-while-idle=false  
\# ========================redis相关配置=====================  
spring.redis.database=0  
spring.redis.host=192.168.111.169  
spring.redis.port=6379  
spring.redis.password=  
spring.redis.lettuce.pool.max-active=8  
spring.redis.lettuce.pool.max-wait=-1ms  
spring.redis.lettuce.pool.max-idle=8  
spring.redis.lettuce.pool.min-idle=0  
\# ========================mybatis相关配置===================  
mybatis.mapper-locations=classpath:mapper/\*.xml  
mybatis.type-aliases-package=com.atguigu.docker.entities  
\# ========================swagger=====================  
spring.swagger2.enabled=true

<a id="t-2-5-7-1-6"></a>
### 主启动

package com.atguigu.docker;

import org.springframework.boot.SpringApplication;  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import tk.mybatis.spring.annotation.MapperScan;

@SpringBootApplication  
@MapperScan("com.atguigu.docker.mapper") //import tk.mybatis.spring.annotation.MapperScan;  
public class DockerBootApplication  
{  
public static void main(String[] args)  
{  
SpringApplication.run(DockerBootApplication.class, args);  
}

}

<a id="t-2-5-7-1-7"></a>
### 业务类

- config配置类
  - RedisConfig

    package com.atguigu.docker.config;

    import lombok.extern.slf4j.Slf4j;  
    import org.springframework.context.annotation.Bean;  
    import org.springframework.context.annotation.Configuration;  
    import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;  
    import org.springframework.data.redis.core.RedisTemplate;  
    import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;  
    import org.springframework.data.redis.serializer.StringRedisSerializer;

    import java.io.Serializable;

    /\*\*  
    \* @auther zzyy  
    \* @create 2021-10-27 17:19  
    \*/

    @Configuration  
    @Slf4j  
    public class RedisConfig  
    {  
    /\*\*  
    \* @param lettuceConnectionFactory  
    \* @return  
    \*  
    \* redis序列化的工具配置类，下面这个请一定开启配置  
    \* 127.0.0.1:6379> keys \*  
    \* 1) "ord:102"  序列化过  
    \* 2) "\\xac\\xed\\x00\\x05t\\x00\\aord:102"   野生，没有序列化过  
    \*/  
    @Bean  
    public RedisTemplate&lt;String,Serializable> redisTemplate(LettuceConnectionFactory lettuceConnectionFactory)  
    {  
    RedisTemplate&lt;String,Serializable> redisTemplate = new RedisTemplate&lt;>();

    redisTemplate.setConnectionFactory(lettuceConnectionFactory);  
    //设置key序列化方式string  
    redisTemplate.setKeySerializer(new StringRedisSerializer());  
    //设置value的序列化方式json  
    redisTemplate.setValueSerializer(new GenericJackson2JsonRedisSerializer());

    redisTemplate.setHashKeySerializer(new StringRedisSerializer());  
    redisTemplate.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());

    redisTemplate.afterPropertiesSet();

    return redisTemplate;  
    }

    }
  - SwaggerConfig

    package com.atguigu.docker.config;

    import org.springframework.beans.factory.annotation.Value;  
    import org.springframework.context.annotation.Bean;  
    import org.springframework.context.annotation.Configuration;  
    import springfox.documentation.builders.ApiInfoBuilder;  
    import springfox.documentation.builders.PathSelectors;  
    import springfox.documentation.builders.RequestHandlerSelectors;  
    import springfox.documentation.service.ApiInfo;  
    import springfox.documentation.spi.DocumentationType;  
    import springfox.documentation.spring.web.plugins.Docket;  
    import springfox.documentation.swagger2.annotations.EnableSwagger2;

    import java.text.SimpleDateFormat;  
    import java.util.Date;

    /\*\*  
    \* @auther zzyy  
    \* @create 2021-05-01 16:18  
    \*/  
    @Configuration  
    @EnableSwagger2  
    public class SwaggerConfig  
    {  
    @Value("${spring.swagger2.enabled}")  
    private Boolean enabled;

    @Bean  
    public Docket createRestApi() {  
    return new Docket(DocumentationType.SWAGGER\_2)  
    .apiInfo(apiInfo())  
    .enable(enabled)  
    .select()  
    .apis(RequestHandlerSelectors.basePackage("com.atguigu.docker")) //你自己的package  
    .paths(PathSelectors.any())  
    .build();  
    }

    public ApiInfo apiInfo() {  
    return new ApiInfoBuilder()  
    .title("尚硅谷Java大厂技术"+"\\t"+new SimpleDateFormat("yyyy-MM-dd").format(new Date()))  
    .description("docker-compose")  
    .version("1.0")  
    .termsOfServiceUrl("https://www.atguigu.com/")  
    .build();  
    }  
    }
- 新建entity
  - User

    package com.atguigu.docker.entities;

    import javax.persistence.Column;  
    import javax.persistence.GeneratedValue;  
    import javax.persistence.Id;  
    import javax.persistence.Table;  
    import java.util.Date;

    @Table(name = "t\_user")  
    public class User  
    {  
    @Id  
    @GeneratedValue(generator = "JDBC")  
    private Integer id;

    /\*\*  
    \* 用户名  
    \*/  
    private String username;

    /\*\*  
    \* 密码  
    \*/  
    private String password;

    /\*\*  
    \* 性别 0=女 1=男  
    \*/  
    private Byte sex;

    /\*\*  
    \* 删除标志，默认0不删除，1删除  
    \*/  
    private Byte deleted;

    /\*\*  
    \* 更新时间  
    \*/  
    @Column(name = "update\_time")  
    private Date updateTime;

    /\*\*  
    \* 创建时间  
    \*/  
    @Column(name = "create\_time")  
    private Date createTime;

    /\*\*  
    \* @return id  
    \*/  
    public Integer getId() {  
    return id;  
    }

    /\*\*  
    \* @param id  
    \*/  
    public void setId(Integer id) {  
    this.id = id;  
    }

    /\*\*  
    \* 获取用户名  
    \*  
    \* @return username - 用户名  
    \*/  
    public String getUsername() {  
    return username;  
    }

    /\*\*  
    \* 设置用户名  
    \*  
    \* @param username 用户名  
    \*/  
    public void setUsername(String username) {  
    this.username = username;  
    }

    /\*\*  
    \* 获取密码  
    \*  
    \* @return password - 密码  
    \*/  
    public String getPassword() {  
    return password;  
    }

    /\*\*  
    \* 设置密码  
    \*  
    \* @param password 密码  
    \*/  
    public void setPassword(String password) {  
    this.password = password;  
    }

    /\*\*  
    \* 获取性别 0=女 1=男  
    \*  
    \* @return sex - 性别 0=女 1=男  
    \*/  
    public Byte getSex() {  
    return sex;  
    }

    /\*\*  
    \* 设置性别 0=女 1=男  
    \*  
    \* @param sex 性别 0=女 1=男  
    \*/  
    public void setSex(Byte sex) {  
    this.sex = sex;  
    }

    /\*\*  
    \* 获取删除标志，默认0不删除，1删除  
    \*  
    \* @return deleted - 删除标志，默认0不删除，1删除  
    \*/  
    public Byte getDeleted() {  
    return deleted;  
    }

    /\*\*  
    \* 设置删除标志，默认0不删除，1删除  
    \*  
    \* @param deleted 删除标志，默认0不删除，1删除  
    \*/  
    public void setDeleted(Byte deleted) {  
    this.deleted = deleted;  
    }

    /\*\*  
    \* 获取更新时间  
    \*  
    \* @return update\_time - 更新时间  
    \*/  
    public Date getUpdateTime() {  
    return updateTime;  
    }

    /\*\*  
    \* 设置更新时间  
    \*  
    \* @param updateTime 更新时间  
    \*/  
    public void setUpdateTime(Date updateTime) {  
    this.updateTime = updateTime;  
    }

    /\*\*  
    \* 获取创建时间  
    \*  
    \* @return create\_time - 创建时间  
    \*/  
    public Date getCreateTime() {  
    return createTime;  
    }

    /\*\*  
    \* 设置创建时间  
    \*  
    \* @param createTime 创建时间  
    \*/  
    public void setCreateTime(Date createTime) {  
    this.createTime = createTime;  
    }  
    }
  - UserDTO

    package com.atguigu.docker.entities;

    import io.swagger.annotations.ApiModel;  
    import io.swagger.annotations.ApiModelProperty;  
    import lombok.AllArgsConstructor;  
    import lombok.Data;  
    import lombok.NoArgsConstructor;

    import java.io.Serializable;  
    import java.util.Date;

    @NoArgsConstructor  
    @AllArgsConstructor  
    @Data  
    @ApiModel(value = "用户信息")  
    public class UserDTO implements Serializable  
    {  
    @ApiModelProperty(value = "用户ID")  
    private Integer id;

    @ApiModelProperty(value = "用户名")  
    private String username;

    @ApiModelProperty(value = "密码")  
    private String password;

    @ApiModelProperty(value = "性别 0=女 1=男 ")  
    private Byte sex;

    @ApiModelProperty(value = "删除标志，默认0不删除，1删除")  
    private Byte deleted;

    @ApiModelProperty(value = "更新时间")  
    private Date updateTime;

    @ApiModelProperty(value = "创建时间")  
    private Date createTime;

    /\*\*  
    \* @return id  
    \*/  
    public Integer getId() {  
    return id;  
    }

    /\*\*  
    \* @param id  
    \*/  
    public void setId(Integer id) {  
    this.id = id;  
    }

    /\*\*  
    \* 获取用户名  
    \*  
    \* @return username - 用户名  
    \*/  
    public String getUsername() {  
    return username;  
    }

    /\*\*  
    \* 设置用户名  
    \*  
    \* @param username 用户名  
    \*/  
    public void setUsername(String username) {  
    this.username = username;  
    }

    /\*\*  
    \* 获取密码  
    \*  
    \* @return password - 密码  
    \*/  
    public String getPassword() {  
    return password;  
    }

    /\*\*  
    \* 设置密码  
    \*  
    \* @param password 密码  
    \*/  
    public void setPassword(String password) {  
    this.password = password;  
    }

    /\*\*  
    \* 获取性别 0=女 1=男  
    \*  
    \* @return sex - 性别 0=女 1=男  
    \*/  
    public Byte getSex() {  
    return sex;  
    }

    /\*\*  
    \* 设置性别 0=女 1=男  
    \*  
    \* @param sex 性别 0=女 1=男  
    \*/  
    public void setSex(Byte sex) {  
    this.sex = sex;  
    }

    /\*\*  
    \* 获取删除标志，默认0不删除，1删除  
    \*  
    \* @return deleted - 删除标志，默认0不删除，1删除  
    \*/  
    public Byte getDeleted() {  
    return deleted;  
    }

    /\*\*  
    \* 设置删除标志，默认0不删除，1删除  
    \*  
    \* @param deleted 删除标志，默认0不删除，1删除  
    \*/  
    public void setDeleted(Byte deleted) {  
    this.deleted = deleted;  
    }

    /\*\*  
    \* 获取更新时间  
    \*  
    \* @return update\_time - 更新时间  
    \*/  
    public Date getUpdateTime() {  
    return updateTime;  
    }

    /\*\*  
    \* 设置更新时间  
    \*  
    \* @param updateTime 更新时间  
    \*/  
    public void setUpdateTime(Date updateTime) {  
    this.updateTime = updateTime;  
    }

    /\*\*  
    \* 获取创建时间  
    \*  
    \* @return create\_time - 创建时间  
    \*/  
    public Date getCreateTime() {  
    return createTime;  
    }

    /\*\*  
    \* 设置创建时间  
    \*  
    \* @param createTime 创建时间  
    \*/  
    public void setCreateTime(Date createTime) {  
    this.createTime = createTime;  
    }

    @Override  
    public String toString() {  
    return "User{" +  
    "id=" + id +  
    ", username='" + username + '\\'' +  
    ", password='" + password + '\\'' +  
    ", sex=" + sex +  
    '}';  
    }  
    }
- 新建mapper
  - 新建接口UserMapper

    **package** com.atguigu.docker.mapper;  

    **import** com.atguigu.docker.entities.User;  
    **import** tk.mybatis.mapper.common.Mapper;  

    **public interface** UserMapper **extends** Mapper&lt;User> {  
    }
  - src\\main\\resources路径下新建mapper文件夹并新增UserMapper.xml

    &lt;?xml version="1.0" encoding="UTF-8"?>  
    &lt;!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">  
    &lt;mapper namespace="com.atguigu.docker.mapper.UserMapper">  
    &lt;resultMap id="BaseResultMap" type="com.atguigu.docker.entities.User">  
    &lt;!--  
    WARNING - @mbg.generated  
    -->  
    &lt;id column="id" jdbcType="INTEGER" property="id" />  
    &lt;result column="username" jdbcType="VARCHAR" property="username" />  
    &lt;result column="password" jdbcType="VARCHAR" property="password" />  
    &lt;result column="sex" jdbcType="TINYINT" property="sex" />  
    &lt;result column="deleted" jdbcType="TINYINT" property="deleted" />  
    &lt;result column="update\_time" jdbcType="TIMESTAMP" property="updateTime" />  
    &lt;result column="create\_time" jdbcType="TIMESTAMP" property="createTime" />  
    &lt;/resultMap>  
    &lt;/mapper>
- 新建service

  package com.atguigu.docker.service;

  import com.atguigu.docker.entities.User;  
  import com.atguigu.docker.mapper.UserMapper;  
  import lombok.extern.slf4j.Slf4j;  
  import org.slf4j.Logger;  
  import org.slf4j.LoggerFactory;  
  import org.springframework.beans.factory.annotation.Autowired;  
  import org.springframework.data.redis.core.RedisTemplate;  
  import org.springframework.data.redis.core.ValueOperations;  
  import org.springframework.stereotype.Service;  
  import org.springframework.web.bind.annotation.PathVariable;

  import javax.annotation.Resource;  
  import java.util.concurrent.TimeUnit;

  /\*\*  
  \* @auther zzyy  
  \* @create 2021-05-01 14:58  
  \*/  
  @Service  
  @Slf4j  
  public class UserService {

  public static final String CACHE\_KEY\_USER = "user:";

  @Resource  
  private UserMapper userMapper;  
  @Resource  
  private RedisTemplate redisTemplate;

  /\*\*  
  \* addUser  
  \* @param user  
  \*/  
  public void addUser(User user)  
  {  
  //1 先插入mysql并成功  
  int i = userMapper.insertSelective(user);

  if(i > 0)  
  {  
  //2 需要再次查询一下mysql将数据捞回来并ok  
  user = userMapper.selectByPrimaryKey(user.getId());  
  //3 将捞出来的user存进redis，完成新增功能的数据一致性。  
  String key = CACHE\_KEY\_USER+user.getId();  
  redisTemplate.opsForValue().set(key,user);  
  }  
  }

  /\*\*  
  \* findUserById  
  \* @param id  
  \* @return  
  \*/  
  public User findUserById(Integer id)  
  {  
  User user = null;  
  String key = CACHE\_KEY\_USER+id;

  //1 先从redis里面查询，如果有直接返回结果，如果没有再去查询mysql  
  user = (User) redisTemplate.opsForValue().get(key);

  if(user == null)  
  {  
  //2 redis里面无，继续查询mysql  
  user = userMapper.selectByPrimaryKey(id);  
  if(user == null)  
  {  
  //3.1 redis+mysql 都无数据  
  //你具体细化，防止多次穿透，我们规定，记录下导致穿透的这个key回写redis  
  return user;  
  }else{  
  //3.2 mysql有，需要将数据写回redis，保证下一次的缓存命中率  
  redisTemplate.opsForValue().set(key,user);  
  }  
  }  
  return user;  
  }  
  }
- 新建controller

  package com.atguigu.docker.controller;

  import cn.hutool.core.util.IdUtil;  
  import cn.hutool.core.util.ReferenceUtil;  
  import com.atguigu.docker.entities.User;  
  import com.atguigu.docker.entities.UserDTO;  
  import com.atguigu.docker.service.UserService;  
  import io.swagger.annotations.Api;  
  import io.swagger.annotations.ApiOperation;  
  import io.swagger.models.auth.In;  
  import lombok.extern.slf4j.Slf4j;  
  import org.springframework.beans.BeanUtils;  
  import org.springframework.beans.factory.annotation.Autowired;  
  import org.springframework.web.bind.annotation.\*;

  import javax.annotation.Resource;  
  import java.util.Random;

  /\*\*  
  \* @auther zzyy  
  \* @create 2021-05-01 15:02  
  \*/  
  @Api(description = "用户User接口")  
  @RestController  
  @Slf4j  
  public class UserController  
  {  
  @Resource  
  private UserService userService;

  @ApiOperation("数据库新增3条记录")  
  @RequestMapping(value = "/user/add",method = RequestMethod.POST)  
  public void addUser()  
  {  
  for (int i = 1; i &lt;=3; i++) {  
  User user = new User();

  user.setUsername("zzyy"+i);  
  user.setPassword(IdUtil.simpleUUID().substring(0,6));  
  user.setSex((byte) new Random().nextInt(2));

  userService.addUser(user);  
  }  
  }

  @ApiOperation("删除1条记录")  
  @RequestMapping(value = "/user/delete/{id}",method = RequestMethod.POST)  
  public void deleteUser(@PathVariable Integer id)  
  {  
  userService.deleteUser(id);  
  }

  @ApiOperation("修改1条记录")  
  @RequestMapping(value = "/user/update",method = RequestMethod.POST)  
  public void updateUser(@RequestBody UserDTO userDTO)  
  {  
  User user = new User();  
  BeanUtils.copyProperties(userDTO,user);  
  userService.updateUser(user);  
  }

  @ApiOperation("查询1条记录")  
  @RequestMapping(value = "/user/find/{id}",method = RequestMethod.GET)  
  public User findUserById(@PathVariable Integer id)  
  {  
  return userService.findUserById2(id);  
  }  
  }
<a id="t-2-5-7-1-8"></a>
### mvn package命令将微服务形成新的jar包 并上传到Linux服务器/mydocker目录下

<a id="t-2-5-7-1-9"></a>
### 编写Dockerfile

\# 基础镜像使用java

FROM java:8

\# 作者

MAINTAINER zzyy

\# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmp

VOLUME /tmp

**# 将jar包添加到容器中并更名为zzyy\_docker.jar**

**ADD docker\_boot-0.0.1-SNAPSHOT.jar zzyy\_docker.jar**

\# 运行jar包

RUN bash -c 'touch /zzyy\_docker.jar'

ENTRYPOINT ["java","-jar","/zzyy\_docker.jar"]

\#暴露6001端口作为微服务

EXPOSE 6001

<a id="t-2-5-7-1-10"></a>
### 构建镜像

- docker build -t zzyy\_docker:1.6 .
<a id="t-2-5-7-2"></a>
## 不用Compose

<a id="t-2-5-7-2-1"></a>
### 单独的mysql容器实例

- 新建mysql容器实例

  docker run -p 3306:3306 --name mysql57 --privileged=true -v /zzyyuse/mysql/conf:/etc/mysql/conf.d -v /zzyyuse/mysql/logs:/logs -v /zzyyuse/mysql/data:/var/lib/mysql -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql:5.7
- 进入mysql容器实例并新建库db2021+新建表t\_user

  docker exec -it mysql57 /bin/bash

  mysql -uroot -p

  create database db2021;

  use db2021;

  CREATE TABLE \`t\_user\` (  
  \`id\` INT(10) UNSIGNED NOT NULL AUTO\_INCREMENT,

  \`username\` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '用户名',

  \`password\` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '密码',

  \`sex\` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',

  \`deleted\` TINYINT(4) UNSIGNED NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',

  \`update\_time\` TIMESTAMP NOT NULL DEFAULT CURRENT\_TIMESTAMP ON UPDATE CURRENT\_TIMESTAMP COMMENT '更新时间',

  \`create\_time\` TIMESTAMP NOT NULL DEFAULT CURRENT\_TIMESTAMP COMMENT '创建时间',

  PRIMARY KEY (\`id\`)

  ) ENGINE=INNODB AUTO\_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
<a id="t-2-5-7-2-2"></a>
### 单独的redis容器实例

docker run  -p 6379:6379 --name redis608 --privileged=true -v /app/redis/redis.conf:/etc/redis/redis.conf -v /app/redis/data:/data -d redis:6.0.8 redis-server /etc/redis/redis.conf

<a id="t-2-5-7-2-3"></a>
### 微服务工程

docker run -d -p 6001:6001 zzyy\_docker:1.6

<a id="t-2-5-7-2-4"></a>
### 上面三个容器实例依次顺序启动成功

![配图](images/img-0295.png)

<a id="t-2-5-7-3"></a>
## swagger测试

<a id="t-2-5-7-3-1"></a>
### http://localhost:你的微服务端口/swagger-ui.html#/

<a id="t-2-5-7-4"></a>
## 上面成功了，有哪些问题?

<a id="t-2-5-7-4-1"></a>
### 先后顺序要求固定，先mysql+redis才能微服务访问成功

<a id="t-2-5-7-4-2"></a>
### 多个run命令......

<a id="t-2-5-7-4-3"></a>
### 容器间的启停或宕机，有可能导致IP地址对应的容器实例变化，映射出错， 要么生产IP写死(可以但是不推荐)，要么通过服务调用

<a id="t-2-5-7-5"></a>
## 使用Compose

<a id="t-2-5-7-5-1"></a>
### 服务编排，一套带走，安排

<a id="t-2-5-7-5-2"></a>
### 编写docker-compose.yml文件

version: "3"

services:

microService:

image: zzyy\_docker:1.6

container\_name: ms01

ports:

\- "6001:6001"

volumes:

\- /app/microService:/data

networks:

\- atguigu\_net

depends\_on:

\- redis

\- mysql

redis:

image: redis:6.0.8

ports:

\- "6379:6379"

volumes:

\- /app/redis/redis.conf:/etc/redis/redis.conf

\- /app/redis/data:/data

networks:

\- atguigu\_net

command: redis-server /etc/redis/redis.conf

mysql:

image: mysql:5.7

environment:

MYSQL\_ROOT\_PASSWORD: '123456'

MYSQL\_ALLOW\_EMPTY\_PASSWORD: 'no'

MYSQL\_DATABASE: 'db2021'

MYSQL\_USER: 'zzyy'

MYSQL\_PASSWORD: 'zzyy123'

ports:

\- "3306:3306"

volumes:

\- /app/mysql/db:/var/lib/mysql

\- /app/mysql/conf/my.cnf:/etc/my.cnf

\- /app/mysql/init:/docker-entrypoint-initdb.d

networks:

\- atguigu\_net

command: --default-authentication-plugin=mysql\_native\_password #解决外部无法访问

networks:

atguigu\_net:

<a id="t-2-5-7-5-3"></a>
### 第二次修改微服务工程docker\_boot

- 写YML

  server.port=6001

  \# ========================alibaba.druid相关配置=====================  
  spring.datasource.type=com.alibaba.druid.pool.DruidDataSource  
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver  
  \#spring.datasource.url=jdbc:mysql://192.168.111.169:3306/db2021?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false  
  spring.datasource.url=jdbc:mysql://mysql:3306/db2021?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false  
  spring.datasource.username=root  
  spring.datasource.password=123456  
  spring.datasource.druid.test-while-idle=false

  \# ========================redis相关配置=====================  
  spring.redis.database=0  
  \#spring.redis.host=192.168.111.169  
  spring.redis.host=redis  
  spring.redis.port=6379  
  spring.redis.password=  
  spring.redis.lettuce.pool.max-active=8  
  spring.redis.lettuce.pool.max-wait=-1ms  
  spring.redis.lettuce.pool.max-idle=8  
  spring.redis.lettuce.pool.min-idle=0

  \# ========================mybatis相关配置===================  
  mybatis.mapper-locations=classpath:mapper/\*.xml  
  mybatis.type-aliases-package=com.atguigu.docker.entities

  \# ========================swagger=====================  
  spring.swagger2.enabled=true
  - 通过服务名访问，IP无关
- mvn package命令将微服务形成新的jar包 并上传到Linux服务器/mydocker目录下
- 编写Dockerfile

  \# 基础镜像使用java

  FROM java:8

  \# 作者

  MAINTAINER zzyy

  \# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmp

  VOLUME /tmp

  **# 将jar包添加到容器中并更名为zzyy\_docker.jar**

  **ADD docker\_boot-0.0.1-SNAPSHOT.jar zzyy\_docker.jar**

  \# 运行jar包

  RUN bash -c 'touch /zzyy\_docker.jar'

  ENTRYPOINT ["java","-jar","/zzyy\_docker.jar"]

  \#暴露6001端口作为微服务

  EXPOSE 6001
- 构建镜像
  - docker build -t zzyy\_docker:1.6 .
<a id="t-2-5-7-5-4"></a>
### 执行 docker-compose up 或者 执行 docker-compose up -d

![配图](images/img-0296.png)

![配图](images/img-0297.png)

<a id="t-2-5-7-5-5"></a>
### 进入mysql容器实例并新建库db2021+新建表t\_user

docker exec -it 容器实例id /bin/bash

mysql -uroot -p

create database db2021;

use db2021;

CREATE TABLE \`t\_user\` (  
\`id\` INT(10) UNSIGNED NOT NULL AUTO\_INCREMENT,

\`username\` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '用户名',

\`password\` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '密码',

\`sex\` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',

\`deleted\` TINYINT(4) UNSIGNED NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',

\`update\_time\` TIMESTAMP NOT NULL DEFAULT CURRENT\_TIMESTAMP ON UPDATE CURRENT\_TIMESTAMP COMMENT '更新时间',

\`create\_time\` TIMESTAMP NOT NULL DEFAULT CURRENT\_TIMESTAMP COMMENT '创建时间',

PRIMARY KEY (\`id\`)

) ENGINE=INNODB AUTO\_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

<a id="t-2-5-7-5-6"></a>
### 测试通过

<a id="t-2-5-7-5-7"></a>
### Compose常用命令

**Compose常用命令**

docker-compose -h                           # 查看帮助

docker-compose up                           # 启动所有docker-compose服务

**docker-compose up -d                        # 启动所有docker-compose服务并后台运行**

**docker-compose down                         # 停止并删除容器、网络、卷、镜像。**

docker-compose exec  yml里面的服务id                 # 进入容器实例内部  docker-compose exec **docker-compose.yml文件中写的服务id** /bin/bash

docker-compose ps                      # 展示当前docker-compose编排过的运行的所有容器

docker-compose top                     # 展示当前docker-compose编排过的容器进程

docker-compose logs  yml里面的服务id     # 查看容器输出日志

**dokcer-compose config     # 检查配置**

**dokcer-compose config -q  # 检查配置，有问题才有输出**

docker-compose restart   # 重启服务

docker-compose start     # 启动服务

docker-compose stop      # 停止服务

<a id="t-2-5-7-5-8"></a>
### 关停

![配图](images/img-0298.png)

---

[上一篇 Docker-compose容器编排](13_Docker-compose容器编排.md) · [目录](Docker与微服务实战.md) · [下一篇 Docker轻量级可视化工具Portainer](14_Docker轻量级可视化工具Portainer.md)
