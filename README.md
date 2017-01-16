# cfdbook 程序员入门手册
## 序言

## 第一部分 工具篇

### 第一章 文本编辑器
vs'code

### 第二章 版本控制————git

#### 管理多个远程git仓库

假如你有多个远程的git仓库，该如何管理

举例来说
你有一个公司的gitlab账号，用来登陆公司的项目，同时你自己在github上有自己的程序
设置两个文件夹namegithub，namegitlab

1. 设置局部的user.name和user.email
有多个远程仓库时，不建议设置全局(使用参数--global)用户名和邮箱


1. ssh key的设置
ssh-keygen -t rsa -C "your github email@...com" 
回车后将id_rsa改为id\_rsa\_github
然后一路回车

ssh-keygen -t rsa -C "your gitlab email@...com" 
回车后将id_rsa改为id\_rsa\_gitlab
然后一路回车

2. 写config文件
在.ssh中新建一个文本文件contig

```
# github
Host github.com
    HostName github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa_cfdgithub
    User cfdcfd

# gitlab
Host jkom-dev.chinacloudapp.cn
    HostName jkom-dev.chinacloudapp.cn
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa
    User fudong.cheng

```



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

web的运用


