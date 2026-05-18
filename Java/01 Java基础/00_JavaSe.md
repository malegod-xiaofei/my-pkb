- Java面向对象的特征有哪些?
封装、继承、多态

封装 : 就是保证软件的部件之间具有优良的模块的基础,封装的目的就是要实现软件部件的,高内聚低耦合,

封装的特性 : 1.良好的封装能够减少耦合

2. 类内部的结构可以自由修改

3. 可以对成员变量进行更精确的控制

4. 隐藏信息,实现细节

继承 : 就是子类继承腹裂的特性和行为,使得子类对象(实例)具有父类的实例域和方法,或子类从父类继承方法,使得子类具有父类相同的行为

继承的特性 : 1.子类拥有父类非 private 的属性和方法

2. 子类可以拥有自己的属性和方法,即子类可以对父类进行扩展

3. 子类可以用自己的方式实现父类的方法

4. java 的继承是单继承,但是可以多重继承,单继承就是一个子类只能继承一个父类

5. 提高了类之间的耦合性(继承的缺点,耦合度高就会造成代码之间的联系越紧密,代码独立性差)

多态 : 就是同一个接口,使用不同的实例而执行不同的操作

多态的优点 : 1.消除类型之间的耦合关系

2. 可替换性

3. 可扩充性

4. 接口性

5.灵活性

6. 简化性

面试官要是问第四个就说是 抽象

- String和StringBuffer的区别是什么
str = “Hello”    X000001

final String

final char[] c = new char[5]{‘hello’};

str = “Hello World”

char[] c = new char[11]{‘Hello World’};

str = “Hello World”          X000002

char[] c = new char[11]{‘Hello World’};

string是线程不安全的,固定长度,单线程使用

StringBUffer是线程安全的,可变长度多线程使用

String:是对象不是原始类型.

为不可变对象,一旦被创建,就不能修改它的值.

对于已经存在的String对象的修改都是重新创建一个新的对象,然后把新的值保存进去.

String 是final类,即不能被继承.

StringBuffer:

是一个可变对象,当对他进行修改的时候不会像String那样重新建立对象

它只能通过构造函数来建立,

StringBuffer sb = new StringBuffer();

对象被建立以后,在内存中就会分配内存空间,并初始保存一个null.通过它的append方法向其赋值.

sb.append("hello");

字符串连接操作中StringBuffer的效率要明显比String高:

String对象是不可变对象,每次操作String 都会重新建立新的对象来保存新的值.

StringBuffer对象实例化后，只对这一个对象操作。

- List、Set、Map的特性分别是什么?
- 如何创建一个线程?如何启动一个线程?
- forward和redirect的区别是什么?
- 请编写一个单例模式
- JSP中内置对象有哪些?
request 请求对象　 类型 javax.servlet.ServletRequest 作用域 Request

response 响应对象 类型 javax.servlet.SrvletResponse 作用域 Page

pageContext 页面上下文对象 类型 javax.servlet.jsp.PageContext 作用域 Page

session 会话对象 类型 javax.servlet.http.HttpSession 作用域 Session

application 应用程序对象 类型 javax.servlet.ServletContext 作用域 Application

out 输出对象 类型 javax.servlet.jsp.JspWriter 作用域 Page

config 配置对象 类型 javax.servlet.ServletConfig 作用域 Page

page 页面对象 类型 javax.lang.Object 作用域 Page

exception 例外对象 类型 javax.lang.Throwable 作用域 page

- Servlet生命周期中的几个方法是什么?
- 请简述MVC模式
- SpringBoot的优点是什么
- Spring中常用的注解有哪些?
- MyBatis中${}和#{}的区别?
- Linux中绝对路径用什么表示?当前目录、上级目录用什么表示?切换目录命令是什么?
- 目录创建、文件创建、文件复制分别用什么命令?
- 如何删除文件?如何删除目录?
- 兔子生兔子
- 水仙花数
- 猴子吃桃子
strings 的 replace('内容','要被 替换的字符','替换字符') 替换字符串方法

replaceAll 支持正则表达式

toUppdateCase 转大写

最终完美版单例模式

package

/**

* @author yingfing

* @create 2020--09--26 16:16

* @describe 单例模式 - 加锁优化版 - 完美解决

*/

```java
public class Singleton2 {
    // 1.私有静态实例 , 防止被引用 , 懒加载
```

private static Singleton2 instance = null;

```
    // 2.私有化构造方法
```

private Singleton2() {

```
    }
    // 3.静态方法 , 创建实例
```

/**

* 单例模式使用内部类来维护单例的实现,JVM内部的机制能够保证当一个类被加载的时候,这个类的加载过程是线程互斥的.

* 这样当我们第一次调用 getInstance 的时候, JVM能够帮我们保证 instance 只能被创建一次,并且会保证把赋值给 instance 的内存初始化完毕,这样我们就不用担心上面的问题.

*/

```java
    private static class SingletonFactory {
```

private static Singleton2 instance = new Singleton2();

```
    }
```

public static Singleton2 getInstance() {

```
        return SingletonFactory.instance;
    }
}
```

- object中有哪些公共方法
clone() : 复制对象,慎用,效率低,且对象中有对象的引用,对象引用不能copy

toString() : 返回此对象的字符串表示形式

equals() : 判断值是否相等

getClass() : 返回object的运行时类

wait() : 导致当前线程等待,同时释放锁,直到另一个线程调用该对象的 notify() 方法或者notifyAll() 方法

notify() : 唤醒正在等待对象监听的单个进程

notifyAll() : 唤醒正在等待对象监听器的所有进程

hashCode() : 返回对象的哈希码值

finalize() : 当垃圾收集确定不需要该对象时,垃圾回收器调用该方法

- 什么叫原子性?
原子性就是原有5块石头，B原有3块石头；现有如下操作：

A让C给予B一块石头，那么应该发生的事情有，A失去一块石头，变为4块，B得到一块石头变为5块；此时交易成功。

不排除有意外情况，比如C在给予B的过程中，B出门了，那么，我们称这个操作失败了，要进行回滚。回滚就是回到事务开始之前的状态，

A还是5块石头,B还是3块石头

我们把这种要么一起成功,要么一起失败的操作叫做原子性操作

如果把一个事务可看做是一个程序,它要么完整的被执行,要么完全不执行,这种特性就叫原子性

- 类加载过程?
- 加载
à指的是将类的class文件读入到内存,并为之创建一个java.lang.class对象,类加载器由 JVM 提供,JVM提供的统称为系统类加载器,除此之外,开发者可以通过继承ClassLoader基类来创建自己的类加载器

- 连接
à 类被加载后,系统会为之生成一个对应的class对象,接着会进入连接阶段,连接阶段负责把类的二进制数据合并到jre

- 初始化
à 初始化就是为类的静态变量赋予争正确的初始值,准备阶段和初始化看起来有些矛盾,其实是不矛盾的

例 : private static int a = 10;

首先字节码被加载到内存中,先进行连接的验证这一步,验证通过后,给a分配内存,因为a是static的,所以此时int类型的默认初始值就是 0 ,即 a = 0 ,然后到解析,到初始化这一步,才吧a的真正的值 10 赋值给 a ,此时 a = 10 ;

载入à验证à准备à解析à初始化

- 双亲委派原则?
其工作原理就是如果一个类加载器收到了类的加载请求,他不会自己先去加载类,而是把这个请求委派给父类的加载器去执行,如果父类还存在其父类加载器,则进一步向上委派,依次递归,请求最终到达顶层的启动类加载器,如果父类加载器可以完成类加载任务,就成功返回,倘若父类加载器无法完成此加载任务,子加载器才会尝试自己去加载,这就是双亲委派原则.

优势 : 1.采用双亲委派原则java类随着它的类 加载器一起具备了一种带有优先级的层次关系,通过这种层次关系,可以避免类的重复加载,当父类已经加载了该类时,就没有必要子类ClassLoader再加载一次,

2.考虑到安全因素,java核心 api 中定义的类型不会被随意替换,假设通过网络传递一个名为 java.lang.Integer的类,通过双亲委派原则,发现该类已经被加载时,并不会重新加载网络传递过来的 java.lang.Integer ,直接返回已经加载过的 Integer.class,这样可以防止核心 api 库被随意篡改.

- Stringbuilder和StringBuffer的对比分析
相同点 ： 可变的字符串操作

不同点 ： 前者不安全，StringBuffer安全
