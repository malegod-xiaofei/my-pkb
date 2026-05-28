```bash
git log
git rebase -i a6b6aa60833c97d1e86557ba6be781fe38e6a7f1
```

- git合并已经提交的push

```bash
#查看提交日志
git log


#xxxxx代表要修改的记录之前的位置对应的id，尽量往下面显示的选（往下面的越早提交），也可以根据时间选
git rebase -i xxxxx

#将要去掉的那条记录把pick换成f
pick-->f

#wq保存之后再查看一次提交记录，应该已经不见了
git log

#要将修改强制提交到服务器同步,例如dev分支
git push origin dev -f

#如果上面是master可能会报错，因为默认master是受保护的，需要去gitlab里面先去取消受保护的分支
```

- 修改已经push的最近一次commit的信息

```bash
git commit --amend
git push origin dev -f

git 使用向导和规范
```

常用的 git 命令:

这里简单列出, 每个命令的具体行为和参数, 要看git help , 和实际操作.

- git status: 查看本地状态
- git log: 查看提交历史
  - git log --color --graph --decorate -M --pretty=oneline --abbrev-commit -M 以图的形式显示提交历史. 增加 --all参数可以看到所有分支的历史. 类似的长命令可以配置快捷方式, 参见
- git branch: 列出分支或创建分支等.
- git checkout: 切换分支, 撤销修改等.
- git checkout -b: 新建分支并切换到新建立的分支.
- git rebase: 重建提交历史
  - git rebase base_branch tip_branch: 把 tip_branch 以下所有没有包含在base_branch中的提交点, 放到base_branch 上面.
  - git rebase --onto base_branch from_branch tip_branch. rebase 的完整参数形式. 指定from_branch到tip_branch的所有提交点, 放到 base_branch上面.
- git rebase -i: 重新调整提交点顺序.
- git reset: 撤销本地修改
- git reset --hard: 撤销本地修改(包括 staged 的修改). 也可以用于强制切换到某个分支.
- git fetch: 从远端(譬如 origin) 拉取修改, 但不修改本地内容.
- git merge --ff-only:merge 直接父子关系的分支.
- git push: 推送提交历史到远端.
  - git push origin branch: 指定推送的本地分支
  - git push origin branch:remote_branch: 指定本地分支branch推送到远端分支remote_branch
  - git pull
  - git merge
  - GOOD: 例如一个功能点的修改, 文档, 测试, 应该放在一个提交点.
  - BAD: 3个功能点的修改放在1个提交点中, 这3个功能相关的文档和测试放在另1个提交点中.
  - 非常简单的邮件可以只有标题.
  - 复杂1点的提交点的message需要更详细的内容来说明提交的内容.
  - GOOD:
  - BAD:
    - fix.
    - some changes.
    - Separate subject from body with a blank line
    - Limit the subject line to 50 characters
    - Capitalize the subject line
    - Do not end the subject line with a period
    - Use the imperative mood in the subject line
    - Wrap the body at 72 characters
    - Use the body to explain what and why vs. how
    - 将测试好的几个提交点组成PR, 在网页上创建PR, 指定review人.
    - review..修改..
    - merge到主干(master/release)
    - GOOD: 例如一个功能点的修改, 文档, 测试, 应该放在一个PR.
    - BAD: 3个功能点的修改放在1个PR中, 这3个功能相关的文档和测试放在另1个PR中.
    - 命名: 以功能和意图命名, 不以自己的名字命名.
    - master 分支保存已确定的稳定的代码. master 一般只由 release分支通过fast-forward方式更新.
    - release 分支保存已经测试稳定, 但还没在线上环境确认稳定, 可以进入下一次部署的代码.
    - 及时清理无用分支/tag/pull request.
    - 及时rebase自己的开发分支到master(要求稳定)或release(依赖最新的特性).
