@ComponentScan 注解 -- 该注解默认会扫描该类所在的包下所有的配置类，相当于之前的 <context:component-scan>。

Component ： 组件

Maven scope

默认 ： 该jar包存在所有的maven项目生命周期

provided ： 只存在于开发环节，打包的时候不需要打包

应用场景 ： 当部署环境当中，已具备该jar包时，则使用provided属性

Spring的两大特性-AOP和IOC

IOC：控制反转

AOP：面向切面编程

熟悉陌生项目的流程

- 确定项目的管理形式-maven还是非maven
- 确定项目类型-应用还是web
- 通过pom.xml了解一下项目依赖的复杂度
- 了解一下包结构
- 找到入口类，顺利把项目先跑起来看一看
- 深入查看了解源代码和配置文件
- 二次开发-改代码
- 二次开发完上线项目
