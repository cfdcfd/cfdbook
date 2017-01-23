#### 分支b操作
- 重命名(远程)分支

删除远程分支 git push --delete origin bname

重命名本地分支 git branch -m bname newname

重新上传 git push remote

- git保证fork出来的project和原来(上游)project同步更新

1 在 Fork 的代码库中添加上游代码库的 remote 源，该操作只需操作一次即可。
如: 其中#upstream 表示上游代码库名， 可以任意。
git remote add upstream repository_address

2 git commit

3 在每次 Pull Request 前做如下操作，即可实现和上游版本库的同步。

3.1 git remote update upstream

3.2 git rebase upstream/{branch name}(需要注意的是在此操作之前，一定要将checkout到{branch name}所指定的branch

4 git push