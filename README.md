# cfdbook 程序员入门手册
## 序言

## 第一部分 工具篇

### 第一章 文本编辑器
vs'code

### 第二章 版本控制————git

#### part1如何安装git

#### part3管理多个远程git仓库


### 第三章 UML

#### part1_UML九种图

#### part2_UML类图

## 第二部分 基础知识
一些常见的基础知识，但教材中往往很少提及或一带而过，使得‘学院派’往往不了解这些常见的小知识
CR:\r
LF:\n
dos/windows系统使用CRLF换行:\r\n
Unix/linux/OSX(较新的苹果系统)使用LF换行:\n
老的Mac OS系统使用CR换行:\r(已经基本弃用)

不同平台间的FTP传输
ascii码模式文本传输，部分FTP软件传输时会自动对换行模式进行变化
如果你不希望ftp修改原文件，可以使用二进制码传输文本(bin模式)

一些文本编辑器会提供换行符的自动变化(例如vscode)

windows端口查找
netstat -ano
获得port 对应PID 
tasklist|findstr "PID"
由PID找对应exe

## 第三部分 框架的学习

web server 
### 开发
#### Python Django 
#### Python Flask

### 测试
#### Python spliter
#### Python se
selenium + python 鼠标事件

