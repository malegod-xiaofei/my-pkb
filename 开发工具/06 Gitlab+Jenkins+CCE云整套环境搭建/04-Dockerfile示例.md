# app-web模块
maven编译后，会将app-web模块打包成war包，可以使用tomcat作为基础镜像进行制作。

`Dockerfile`示例：

```dockerfile
FROM tomcat:9.0.90-jre8
LABEL maintainer="lalala"

# 设置时区为东八区时间
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >/etc/timezone

# 复制编译的war包到tomcat的webapps目录
COPY target/myproject.war /usr/local/tomcat/webapps/myproject.war
WORKDIR /usr/local/tomcat

# 暴露tomcat的8080端口
EXPOSE 8080

# 启动tomcat
ENV JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom"
ENTRYPOINT ["catalina.sh", "run"]
```

  


# system-server模块
maven编译后，会将system-server模块打包成jar包（SpringBoot项目），可以使用openjdk作为基础镜像进行制作。

`Dockerfile`示例：

```dockerfile
FROM openjdk:8u312-bullseye
LABEL maintainer="lalala"

# 设置时区为东八区时间
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >/etc/timezone

# 复制编译的jar包到容器的/usr/src目录
COPY target/system-server-1.0.jar /usr/src/system-server/system-server.jar
WORKDIR /usr/src/system-server

# 设置使用dev环境配置、使用8093端口
ENV JAVA_PARAMS=" -Djava.security.egd=file:/dev/./urandom --server.port=8093 --spring.profiles.active=dev"
# 暴露8093端口
EXPOSE 8093

# 带着配置项运行jar包
ENTRYPOINT ["java", "-jar" ,"/usr/src/system-server/system-server.jar"]
CMD ["$JAVA_PARAMS"]
```

  


# vue项目
## Nginx基础镜像打包
使用Nginx作为基础镜像。

```dockerfile
FROM nginx:1.27.0
LABEL maintainer="lalala"

# 设置时区为上海东八区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >/etc/timezone

# nginx 将编译生成的dist下的文件复制到容器/usr/share/nginx/html中
COPY dist/ /usr/share/nginx/html/myproject-vue/
# 复制nginx配置文件到容器/etc/
COPY nginx.conf /etc/nginx/nginx.conf

# 暴露80端口
EXPOSE 80
```

nginx配置：

```nginx
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    underscores_in_headers on;
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
    
    server {
        listen   80 default_server;
        location /xxx/xxx {
            proxy_pass http://service-xxx:8093/xxx/xxx;
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_hide_header X-Frame-Options;
            add_header X-Frame-Options ALLOWALL;
        }

        location /xxx {
            proxy_pass http://service-xxx:8080/xxx;
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_hide_header X-Frame-Options;
            add_header X-Frame-Options ALLOWALL;
        }
        
        location /xxxxxxxx {
            root /usr/share/nginx/html/;
        }
    }
}
```

  


## 旧的httpd作为基础镜像打包
F5只映射了一个地址，所以需要前端部署为Nginx。目前已不再使用httpd打包。

Node会将vue项目打包编译成镜像页面，可以使用httpd作为基础镜像进行制作。

`Dockerfile`示例：

```dockerfile
FROM httpd:2.4.61
LABEL maintainer="lalala"

# 设置时区为上海东八区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >/etc/timezone

# 将编译生成的dist下的文件复制到容器/usr/local/apache2/htdocs中
COPY dist/ /usr/local/apache2/htdocs/myproject-vue/
# 暴露httpd的80端口
EXPOSE 80
```

