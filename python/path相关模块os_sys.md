- os.getcwd()
返回当前工作路径

- os.path.dirname(__file__)
返回该文件所在目录

- os.path.abspath(path)
将path修正为绝对路径(if path is not normal)


- sys.path.append()
加入路径到PYTHONPATH

- 在site-package中加入.pth结尾的文件
```
# .pth file for the my project(这行是注释)
E:\DjangoWord
E:\DjangoWord\mysite
E:\DjangoWord\mysite\polls
```
python 在运行时会自动将.pth结尾的文件中的路径添加到sys.path 设置中

该方法可配合virtualenv虚拟机使用