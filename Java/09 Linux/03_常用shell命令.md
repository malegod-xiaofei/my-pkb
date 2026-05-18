- 查看正在运行的spark进程

```
ps aux | grep spark
ps aux | grep flask
kill -9
lsb_release -a
```

- 上传upload.sh文件到远程服务器上去

```
scp /Users/sunny/Desktop/BOSS.tar.gz root@101.200.121.42:/web/
```

- Linux根据占用的端口号来关闭相应的进程的shell脚本写法

```
kill -9 $(lsof -i:22 | awk '{print $2}' | tail -n 2)
```

- 查询正在活着的进程 ：

```
ps aux | less
```

- 打成tar包

```
tar -czvf sensitiveDetect-20260122.tar.gz qidTrade-1.0-SNAPSHOT-jar-with-dependencies.jar
tar -czvf evaluation_monitor.20260310.tar.gz query-trade-eval-monitor-1.0-SNAPSHOT-jar-with-dependencies.jar
tar -czvf my_explainable20241230.tar.gz explainable_analysis-1.0-SNAPSHOT-jar-with-dependencies.jar
tar -czvf 20240906.tar.gz ./infer
tar -czvf my-union-query-trade.tar.gz union-query-trade-1.0.0.0-SNAPSHOT-jar-with-dependencies.jar
tar -czvf querytrade.ernie.infer.20250606.tar.gz infer
tar -czvf zyf.tar.gz Zyf-1.0-SNAPSHOT-jar-with-dependencies.jar
tar -czvf my-query-spark2.tar.gz query-trade-1.0-spark2-SNAPSHOT-jar-with-dependencies.jar
tar -czvf my-query-spark3.tar.gz query-trade-1.0-spark3-SNAPSHOT-jar-with-dependencies.jar
tar -czvf scripts.tar.gz image_goal_split.sh realtime_goal_split.sh video_goal_split.sh xsp_goal_split.sh
tar -czvf 123.tar.gz result.xlsx
# 上线tar包
tar -czvf new-query-trade-20251208.tar.gz query-trade-1.0-spark2-SNAPSHOT-jar-with-dependencies.jar
```

- 解压一个文件

```
# 使用 tar 解压 ：
tar -zxvf java.tar.gz
# gz 文件的解压gzip命令 ： 
gzip -d java.gz
# 也可以使用zcat命令，然后将标准输出保存文件 ： 
zcat java.gz > java.java
# 解压 zip 文件
unzip xxx.zip

strings /lib64/libc.so.6 | grep GLIBC_
```

- shell脚本看文本文件的内容：
  - cat
  - vi  vim
  - more
  - head -n num "文件名"
- 下载 Linux 文件到 Windows
  - sz 文件名
- 搜索文件：find
- 赋予脚本执行权限

```
chmod +x
```

- 后台执行并将日志输出到指定文件中

```
nohup > /home/work/zhaoyingfei/log/output.log 2>&1 &
nohup > sh run_low.sh > /home/work/zhaoyingfei/mr/0902-0908/log.txt 2>&1
# 监控日志文件后十行 n 监控行数 F 持续监控
tail -n 10 -F log.txt
```

Linux使用指令

- 第1章
  - su root
    - 然后输入root账号的密码
  - 1. 重命名文件 :mv old_name new_name
    - cd --> 切换文件夹 mkdir --> 创建文件夹 rm -r --> 删除文件夹
    - su --> 切换用户
    - 切换用户
    - passwd --> 更改密码
    - 相对和绝对
    - vim --> 编辑文件
    - cat --> 查看文件 cat -n 查看前n行
    - ls --> 查看文件
    - cp -r /home/tianliang/study/ /root --> 复制文件
    - touch --> 创建文件
    - touch --> 去其他用户创建文件
    - echo --> 写出
    - head --> 前多少行
    - tail --> 后多少行
    - df --> 查看磁盘
- 第2章 Linux三剑客
  - grep --> 查找/过滤文本行
  - sed --> 批量编辑文本内容
  - awk --> 按列处理和统计文本
- 第3章 使用指令
  - more : 分页查看
  - ls *.zip | xargs unzip 将拿到的参数转化为输入
  - ls *.zip | xargs -n 1 --> 拿到的参数一个一个的处理
  - s *.zip | xargs -n 1 unzip -d ../路径
  - ll -a 显示隐藏的文件夹
  - wc -l * 查看文件大小
  - du -sh * 查看文件大小
  - chown -R 设置文件所有者和文件关联组的命令
  - rz -bye (b:二进制，y：不要问我为什么，直接上传，e：覆盖源文件)
  - history : 查看历史命令记录 ----- ！执行对应的命令索引
- linux目录管理
- 查看虚拟机是Ubuntu还是Centos

```
lsb_release -a
```

- Centos安装git

```
yum -y install git
git --version
```

- 退出当前虚拟机并连接另一台虚拟机

```
exit
dx-lt-yd-hebei-shijiazhuang-10-10-103-10-87
```

- 创建家目录

```
sudo -i # 创建超级用户的shell
```

- 查看文件前几行

```
cat /root/fucheng.wang/pudge-sanmahostregion/01.csv |head -n 100
```

- 在项目根目录下执行->go build app/main.go
