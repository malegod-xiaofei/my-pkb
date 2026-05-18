_24_SpringMVC

1.request和Response的区别

response : 用于向浏览器写东西

request : 获取浏览器发送过来的参数,通过request就可以了

2. SpringMVC的执行流程

1 用户发送请求至前端控制器DispatcherServlet

2 DispatcherServlet收到请求调用HandlerMapping处理器映射器。

3 处理器映射器根据请求url找到具体的处理器，生成处理器对象及处理器拦截器(如果有则生成)一并返回给DispatcherServlet。

4 DispatcherServlet通过HandlerAdapter处理器适配器调用处理器

5 执行处理器(Controller，也叫后端控制器)。

6 Controller执行完成返回ModelAndView

7 HandlerAdapter将controller执行结果ModelAndView返回给DispatcherServlet

8 DispatcherServlet将ModelAndView传给ViewReslover视图解析器

9 ViewReslover解析后返回具体View

10 DispatcherServlet对View进行渲染视图（即将模型数据填充至视图中）。

11 DispatcherServlet响应用户

以上流程是以DispatcherServlet为核心轴,并且DispatcherServlet就是一个Servlet

3. bean的生命周期

Spring启动，查找并加载需要被Spring管理的bean，进行Bean的实例化

Bean实例化后对将Bean的引入和值注入到Bean的属性中

如果Bean实现了BeanNameAware接口的话，Spring将Bean的Id传递给setBeanName()方法

如果Bean实现了BeanFactoryAware接口的话，Spring将调用setBeanFactory()方法，将BeanFactory容器实例传入

如果Bean实现了ApplicationContextAware接口的话，Spring将调用Bean的setApplicationContext()方法，将bean所在应用上下文引用传入进来。

如果Bean实现了BeanPostProcessor接口，Spring就将调用他们的postProcessBeforeInitialization()方法。

如果Bean 实现了InitializingBean接口，Spring将调用他们的afterPropertiesSet()方法。类似的，如果bean使用init-method声明了初始化方法，该方法也会被调用

如果Bean 实现了BeanPostProcessor接口，Spring就将调用他们的postProcessAfterInitialization()方法。

此时，Bean已经准备就绪，可以被应用程序使用了。他们将一直驻留在应用上下文中，直到应用上下文被销毁。

如果bean实现了DisposableBean接口，Spring将调用它的destory()接口方法，同样，如果bean使用了destory-method 声明销毁方法，该方法也会被调用。

————————————初始化————————————

BeanNameAware.setBeanName() 在创建此bean的bean工厂中设置bean的名称，在普通属性设置之后调用，在InitializinngBean.afterPropertiesSet()方法之前调用

BeanClassLoaderAware.setBeanClassLoader(): 在普通属性设置之后，InitializingBean.afterPropertiesSet()之前调用

BeanFactoryAware.setBeanFactory() : 回调提供了自己的bean实例工厂，在普通属性设置之后，在InitializingBean.afterPropertiesSet()或者自定义初始化方法之前调用

EnvironmentAware.setEnvironment(): 设置environment在组件使用时调用

EmbeddedValueResolverAware.setEmbeddedValueResolver(): 设置StringValueResolver 用来解决嵌入式的值域问题

ResourceLoaderAware.setResourceLoader(): 在普通bean对象之后调用，在afterPropertiesSet 或者自定义的init-method 之前调用，在 ApplicationContextAware 之前调用。

ApplicationEventPublisherAware.setApplicationEventPublisher(): 在普通bean属性之后调用，在初始化调用afterPropertiesSet 或者自定义初始化方法之前调用。在 ApplicationContextAware 之前调用。

MessageSourceAware.setMessageSource(): 在普通bean属性之后调用，在初始化调用afterPropertiesSet 或者自定义初始化方法之前调用，在 ApplicationContextAware 之前调用。

ApplicationContextAware.setApplicationContext(): 在普通Bean对象生成之后调用，在InitializingBean.afterPropertiesSet之前调用或者用户自定义初始化方法之前。在ResourceLoaderAware.setResourceLoader，ApplicationEventPublisherAware.setApplicationEventPublisher，MessageSourceAware之后调用。

ServletContextAware.setServletContext(): 运行时设置ServletContext，在普通bean初始化后调用，在InitializingBean.afterPropertiesSet之前调用，在 ApplicationContextAware 之后调用注：是在WebApplicationContext 运行时

BeanPostProcessor.postProcessBeforeInitialization() : 将此BeanPostProcessor 应用于给定的新bean实例 在任何bean初始化回调方法(像是InitializingBean.afterPropertiesSet或者自定义的初始化方法）之前调用。这个bean将要准备填充属性的值。返回的bean示例可能被普通对象包装，默认实现返回是一个bean。

BeanPostProcessor.postProcessAfterInitialization() : 将此BeanPostProcessor 应用于给定的新bean实例 在任何bean初始化回调方法(像是InitializingBean.afterPropertiesSet或者自定义的初始化方法)之后调用。这个bean将要准备填充属性的值。返回的bean示例可能被普通对象包装

InitializingBean.afterPropertiesSet(): 被BeanFactory在设置所有bean属性之后调用(并且满足BeanFactory 和 ApplicationContextAware)。

————————————销毁————————————

在BeanFactory 关闭的时候，Bean的生命周期会调用如下方法:

DestructionAwareBeanPostProcessor.postProcessBeforeDestruction(): 在销毁之前将此BeanPostProcessor 应用于给定的bean实例。能够调用自定义回调，像是DisposableBean 的销毁和自定义销毁方法，这个回调仅仅适用于工厂中的单例bean(包括内部bean)

实现了自定义的destory()方法

# 1 常用注解

- 组件型注解
- @Component在类定义之前添加@Component注解，他会被spring容器识别，并转为bean
- @Repository 对Dao层实现类进行注解
- @Service用于对业务逻辑层进行注解
- @Controller用于控制层注解
- 请求和参数型注解
- @RequestMapping：用于处理请求地址映射，可以作用于类和方法上
- @RequestParam:用于获取传入参数的值
- @PathViriable:用于定义路径参数值
- @ResponseBody:作用于方法上，可以将整个返回结果以某种格式返回
- @ModelAttribute:用于把参数保存到model中，可以注解方法或参数
- @SessionAttributes:如果要跨页面使用，那么需要使用到session。SessionAttribute注解可以使得模型中的数据存储一份到session域中
- S
