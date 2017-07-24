## git commit message使用规范
文章描述 AngularJS 项目的规范
参考网络资源[Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)

#### 概述
AngularJS 规范规定git message 由三部分构成, Header(必须)，Body(可省略) 和 Footer(可省略)。
- Header部分只有一行，包括三个字段：type（必需）、scope（可选）和subject（必需）。

> 例子: tag(scope): subject

#### tag
- 7种标签
feat：某个新功能的开发（feature）
fix：修补某个bug
docs：文档（documentation）
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试，(包括测试函数的编写)
chore：构建过程或辅助工具的变动

> 注: chore 的英文原意是零星的琐碎的工作，比如，删除无用的临时文件，改变辅助工具，改变文件夹/文件的名字

#### scope
标注该commit的影响范围

#### subject
描述该commit

> feat(tool): new feature to read database
> docs(cfdgitbook): add a example to use the book
> docs: add README in cfdgitbook
>