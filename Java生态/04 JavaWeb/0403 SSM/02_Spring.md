spring lazyload 迟加载生命周期

两种情况

1一、什么是懒加载

Spring默认会在容器初始化的过程中，解析xml或注解，创建配置为单例的bean并保存到一个map中，这样的机制在bean比较少时问题不大，但一旦bean非常多时，spring需要在启动的过程中花费大量的时间

来创建bean ，花费大量的空间存储bean，但这些bean可能很久都用不上，这种在启动时在时间和空间上的浪费显得非常的不值得。

所以Spring提供了懒加载机制。所谓的懒加载机制就是可以规定指定的bean不在启动时立即创建，而是在后续第一次用到时才创建，从而减轻在启动过程中对时间和内存的消耗。

懒加载机制只对单例bean有作用，对于多例bean设置懒加载没有意义，因为多例bean本来就是在使用时才创建的。

二、懒加载配置方式

1、xml配置

在xml文件里面，可以通过配置 lazy-init="true"来启用懒加载，。如下面的配置，设置cart启用懒加载，这样，在容器启动的时候，就不会立即创建bean cart，直到第一次使用的时候才会创建。

<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns=""

xmlns:xsi=""

xsi:schemaLocation="

">

<bean id="cart" class="cn.tedu.beans.Cart" lazy-init="true"></bean>

</beans>

上面是单独设置某个bean的懒加载，我们还可以为全局配置懒加载，如下面的代码所示。

<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns=""

xmlns:xsi=""

xsi:schemaLocation="

"

default-lazy-init="true">

<bean id="cart" class="cn.tedu.beans.Cart"></bean>

</beans>

注意，如果同时设定全局和指定bean的懒加载机制，且配置不相同，则对于该bean局部配置会覆盖全局配置。

2、注解配置（@Lazy）

在实际开发中，我们会大量用到注解的方式来配置bean，所以除了会用xml方式启用懒加载外，还应该会通过注解启用懒加载。测试代码如下：

一个实体类Book：

```java
package ztt.lazy;
```

/**

* @Description:

* @Auther: tt

* @Date: 2020/3/1 14:31

*/

```java
public class Book {
    private String bookName;
```

public Book() {

```java
        System.out.println("调用构造方法，创建book...");
    }
    public String getBookName() {
        return bookName;
    }
    public void setBookName(String bookName) {
```

this.bookName = bookName;

```java
    }
    @Override
    public String toString() {
        return "Book{" +
```

"bookName='" + bookName + '\'' +

'}';

```text
    }
}
```

配置类 Config：

```java
package ztt.lazy;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
```

/**

* @Description:

* @Auther: tt

* @Date: 2020/3/1 14:32

*/

```java
public class Config {
    @Bean(value = "book")
```

public Book getBook(){

Book book = new Book();

book.setBookName("《数据结构》");

```java
        return book;
    }
    @Test
    public void test(){
```

ApplicationContext applicationContext = new AnnotationConfigApplicationContext(Config.class);

```text
    }
}
```

在没有用@Lazy注解标注的时候，不会启动懒加载，在容器创建的时候，就会初始化bean，如下图所示。

加上@Lazy注解，启动懒加载，在容器创建的时候，不会初始化bean，如下图所示。

然后，我们获取这个bean，修改代码如下：

```java
    @Test
    public void test(){
```

ApplicationContext applicationContext = new AnnotationConfigApplicationContext(Config.class);

```java
        System.out.println("初始化容器成功！");
        System.out.println("获取bean");
```

Book book = (Book) applicationContext.getBean("book");

```java
        System.out.println("从容器中取出book：");
        System.out.println(book);
    }
```

打印结果：

可以看到，创建容器的时候，没有创建book对像，直到第一次使用的时候才创建。

@Lazy 的属性value 取值有 true 和 false 这两个， 默认值为 true。true 表示使用 延迟加载， false 表示不使用。

2

namespace和别名没有关系
