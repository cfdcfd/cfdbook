## 多线程压缩与解压
#### 单线程命令

- 解压 tar -xzvf file.tar.gz
- 压缩 tar -czvf file.tar.gz

#### pigz 多线程压缩与解压

tar cvf - 目录名 | pigz -9 -p 24 > file.tgz

time tar -cv blast_t2d/SRR34159* | pigz -p 24 -k > SRR590-898DLM.tar.gz

pigz：用法-9是压缩比率比较大，-p是指定cpu的核数。


解压:
pigz -d file.tgz
tar -xf --format=posix file
- 
- 

## 查找文件
find