# 1 一、配置Maven

- 解压

![图片1.png](images/图片1.png)

- 在我的电脑->属性->高级系统设置->环境变量->系统变量->新建->M2_HOME->D:\Configure\apache-maven-3.6.3(选择本地路径)

![图片2.png](images/图片2.png)

  - 下方找到path->%M2_HOME%\bin;->添加到开头

![图片3.png](images/图片3.png)

  - ->一路确定退出 ->打开cmd->输入:mvn -version

![图片4.png](images/图片4.png)

- 创建.m2仓库
  - 解压

![图片5.png](images/图片5.png)

  - 修改settings.xml下<localRepository>D:\Configure\.m2\respository</localRepository>为本地仓库路径
  - 配置阿里云镜像

```text
<mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>central</mirrorOf>
</mirror>
<mirror>
    <id>huaweicloud</id>
    <mirrorOf>*,!HuaweiCloudSDK</mirrorOf>
    <url>https://mirrors.huaweicloud.com/repository/maven/</url>
</mirror>
<!-- 这里是用来处理阿里云DataHub的镜像仓库 -->
<!-- <mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>*,!oss.sonatype.org-snapshot,!apache.snapshots</mirrorOf>
</mirror> -->
<!-- <mirror>
    <id>huaweicloud</id>
    <mirrorOf>*,!HuaweiCloudSDK</mirrorOf>
    <url>https://mirrors.huaweicloud.com/repository/maven/</url>
</mirror> -->
```

- Idea配置maven
  - 配置全局的maven设置

![图片6.png](images/图片6.png)

  - 更改为自己的maven路径

![图片7.png](images/图片7.png)

  - Maven打包跳过Test文件

![图片8.png](images/图片8.png)

# 2 二、配置Git

- 安装

![图片9.png](images/图片9.png)

- 配置全局用户名和密码
  - git config --global user.name "Malegod丶小飞" 用户名标识 ---- 实际也可以填写您的github仓库的名称
  - git config --global user.email "theshy6668" 邮箱标识 -------可以填写github仓库的邮箱
- 配置SSH免密登录
  - ssh-keygen -t rsa //--创建秘钥
- 秘钥上传到gitee远程仓库->

![图片10.png](images/图片10.png)

- idea配置git
  - settings->git->选择git安装路径下的bin\git.exe

![图片11.png](images/图片11.png)

  - 获取git私人令牌

![图片12.png](images/图片12.png)

  - 添加到gitee中github同理

![图片13.png](images/图片13.png)

  - 配置Terminal为Git-bash
    - 注意是Git->bin目录下的bash.exe，如果是Git目录下的bash.exe会单独打开一个git-bash窗口。

![图片14.png](images/图片14.png)

# 3 三、Idea使用配置

- 配置滚轮设置字体大小写

![图片15.png](images/图片15.png)

- 设置鼠标悬浮文本提示

![图片16.png](images/图片16.png)

- 设置自动导包

![图片17.png](images/图片17.png)

- 配置显示行号和方法之间的分割符

![图片18.png](images/图片18.png)

- 配置忽略大小写提示

![图片19.png](images/图片19.png)

- 配置idea双行显示文件

![图片20.png](images/图片20.png)

![图片21.png](images/图片21.png)

- 配置字体大小、行间距

![图片22.png](images/图片22.png)

- 配置文档注释颜色

![图片23.png](images/图片23.png)

- 配置文档头注释信息

```sql
/**
 * @author Malegod_xiaofei
 * @create ${YEAR}-${MONTH}-${DAY}-${TIME}
 */
```

  - idea设置注释模板

![图片24.png](images/图片24.png)

- 配置编码集

![图片25.png](images/图片25.png)

- 配置工程自动编译

![图片26.png](images/图片26.png)

- 配置两行工具栏

![图片27.png](images/图片27.png)

- 配置全局的文件换行格式

![图片28.png](images/图片28.png)

- 配置全局的编译版本

![图片29.png](images/图片29.png)

- 配置全局的1.8编译版本

![图片30.png](images/图片30.png)

- 配置生成类图

![图片31.png](images/图片31.png)

- 设置弹出Git提交窗口

![图片32.png](images/图片32.png)
