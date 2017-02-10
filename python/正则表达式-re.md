## re
python中正则表达式的常用模块

#### 常规使用说明
仅列举部分常规用法，详见[网络资料](http://www.runoob.com/python/python-reg-expressions.html)


[常见unicode编码表](http://www.cnblogs.com/chenwenbiao/archive/2011/08/17/2142718.html)
列举常用区间如下：
- [\u4e00-\u9fbf]	CJK(中日韩)统一表意符号
- [\u4e00-\u9fa5]	汉字范围，包括部分日韩字符 
- [aeiou]           匹配中括号内的任意一个字母
- [0-9]             匹配任何数字。类似于 [0123456789]
- [a-z]             匹配任何小写字母
- [A-Z]             匹配任何大写字母
- [a-zA-Z0-9]       匹配任何字母及数字
- [^aeiou]          除了aeiou字母以外的所有字符
- [^0-9]            匹配除了数字外的字符

使用的小tips
- [Pp]ython         匹配 "Python" 或 "python"
- rub[ye]           匹配 "ruby" 或 "rube"