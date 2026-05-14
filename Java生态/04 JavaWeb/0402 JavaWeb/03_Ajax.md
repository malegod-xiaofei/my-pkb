搭建ajax环境

首先导入对应的插件

放到maven项目指定的路径下

新建ajax.jsp文件

对应的导入语句

request.getContextPath()&nbsp;&nbsp;:&nbsp;&nbsp;获取当前项目名

JQuery+ajax模板

$.ajax({

&nbsp;&nbsp;&nbsp;&nbsp;url:'',

&nbsp;&nbsp;&nbsp;&nbsp;type:'POST', //GET

&nbsp;&nbsp;&nbsp;&nbsp;async:true,&nbsp;&nbsp;&nbsp;&nbsp;//或false,是否异步

&nbsp;&nbsp;&nbsp;&nbsp;data:{

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name:'llc',

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;age:22

&nbsp;&nbsp;&nbsp;&nbsp;},

&nbsp;&nbsp;&nbsp;&nbsp;timeout:5000,&nbsp;&nbsp;&nbsp;&nbsp;//超时时间

&nbsp;&nbsp;&nbsp;&nbsp;dataType:'json',&nbsp;&nbsp;&nbsp;&nbsp;//返回的数据格式：json/xml/html/script/jsonp/text

&nbsp;&nbsp;&nbsp;&nbsp;beforeSend:function(xhr){

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log(xhr)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log('发送前')

&nbsp;&nbsp;&nbsp;&nbsp;},

&nbsp;&nbsp;&nbsp;&nbsp;success:function(data,textStatus,jqXHR){

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log(data)；

&nbsp;&nbsp;&nbsp;&nbsp;},

&nbsp;&nbsp;&nbsp;&nbsp;error:function(xhr,textStatus){

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log('错误'，xhr.responseText)；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log(xhr)；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log(textStatus)；

&nbsp;&nbsp;&nbsp;&nbsp;}

})

&nbsp;
