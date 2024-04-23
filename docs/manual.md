## 项目结构介绍
```
-|-.github/workflows #这里存储github page部署yml
-|-docs #这个目录用于存储所有文档内容
	 |--index.md #HITWH-CS站点主页
	 |--others.md #或者有其他页面
	 |--example #这是一个样例目录
			|--index.md #example的主页
			|--others1.md #example的具体其他内容
			|--others2.md #example的具体其他内容
-|-mkdocs.yml #网站的配置文件，具体内容看下文
-|-requirments.txt #Python的需求文件，如无必要，勿增实体			
```
## 新增内容说明
如果需要新增板块和页面，请对 `mkdocs.yml` 的 `nav` 板块下进行修改
下图是新增一个通识课 general 的样例
![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221020821.png)
可以看到主页和通识课是两个**板块内容**，其各自对应的**文档内容**显示在左侧导航栏，如下图所示
![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221026701.png)
可以看到主页目录下有 `index.md` 默认主页和 `next.md` 的样例
`nav` 所对应的就是项目结构中 `docs` 所对应的目录结构，
![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221025576.png)
`general` 目录对应新增的核心课的所有内容，一个版块一个目录，方便维护，下面是`general` 目录的内容
![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221029520.png)

## 贡献指南
本网站欢迎一切贡献 
不过课程内容只面向HITWH的课程内容范围，如果你想要为本网站进行贡献，以下是一些指南。

> 可以先看下文git的使用，以熟悉git的操作

### 本地构建
项目拉取：
```sh
git clone https://github.com/Fifth-Space/HITWH-CS.git
cd HITWH-CS
```
安装 Python 依赖
```sh
pip install -r requirements.txt
```
安装本文档插件：
```sh
git clone https://github.com/Fifth-Space/mkdocs_plugins.git
cd mkdocs_plugins
pip install -e .
cd ..
```
在本地运行，确认无误后再进行推送
```sh
mkdocs serve
```
- 之后即可通过浏览器访问 localhost:8000 预览网站


## 贡献守则
- 对于课程请进行客观的评价，尽量不要带有主观色彩
- 对于外部资源，请尽量插入链接，不要将文件传入本 repo
- 尽量不要上传有版权的文件，例如课件等
- 对于自己的笔记、复习提纲等材料：
    - 如果有自己的网站，推荐放在自己的网站并在此插入链接
    - 也可以将文件上传到对应课程文件夹中，并插入相对链接
- 尽量规范编写 markdown，避免出现格式错误，**先在自己的本地进行测试！**

## 贡献方式

==务必查看以下内容，避免协作者冲突==

通过**两次** PR（即 Pull Request）的形式来进行贡献，具体流程：

- 在 GitHub 网页端点击右上角的 fork，将本仓库 fork 到自己的账号下

- 在自己账号的对应仓库中进行修改（提交方式参见git使用）

- 开始你的工作时，将计划的页面写入mkdocs.yml中，提交到个人仓库的fork

- 修改完成后，在自己的仓库内Pull requests中 点击 New pull request，创建一个 PR，**并说明提交的yml文件的修改内容**（第一次提交）

- 然后开始具体的工作，在结束时提交新的的docs内容，同样创建pull request，**说明提交的docs文件的内容**（第二次提交）

  > 第一次提交占一下mkdocs.yml的坑位，这样避免merge冲突
  >
  > 第二次提交就在docs提交你的markdown

  ![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221056918.png)

![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221057922.png)

- 等待管理员的审核、修改，然后合并到本 repo 中，如必要将会联系提交者

## 项目规划
```
general: 通识课
outer: 外专业选修课
basic: 数理基础课
culture：文化素质课
major：CS 专业类课程
labs：学校各个实验室的技术栈介绍和项目（包括老师的实验室）
competition：计算机竞赛相关
salon：俱乐部可公开的分享会文档
CTF-WP：俱乐部参加的CTF比赛题解
```

## 有关Git的使用

### git下载

官网下载 https://git-scm.com/

安装完打开bash输入 `git`即可查看是否正常

### git和github和gitee的关系

git是管理代码的工具，可以记录源码的历史，本地

github和gitee都是托管仓库，在线

使用git可以方便的推送代码到远程仓库，也可以方便的进行**多人协作**

### Git的配置

首先，要配置电脑的ssh key

打开bash/cmd/powershell

```bash
ssh-keygen -t rsa -C "<email>"
```

这个email应该对应你的github/gitee邮箱，事实上两个托管平台用一样的就行（事实上`-C`参数可以不添加

敲三次回车一路到底就行（可以输入文件名/密码，但是不是必要的）

这时候会在你的用户目录下的.ssh文件夹里生成一个id_rsa （私钥） id_rsa.pub（公钥），我们使用公钥

```bash
cat .ssh/id_rsa.pub
```

获取命令行输出的公钥内容，全部复制

登陆github，进入到个人的Settings

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404230003183.png)

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404230005376.png)

添加sshkey，直接粘贴刚刚的公钥就行，确认。

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404230007096.png)

没什么问题的话一封邮件会发到你的邮箱告知你添加了这个公钥。现在，理论上你这台电脑就能连接到github了

```bash
ssh -T git@github.com
```

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222337770.png)

> 如果换台电脑，同样的流程也得走一遍

接下来配置git

还是在命令行（推荐用git的bash）

```bash
git config --global user.name "your_github_username" 
git config --global user.email "your_email"
```

其中用户名是你注册github的**账号名字**

邮箱是注册使用的**邮箱**，没什么问题就和上面公钥用的一样

```bash
git config --global --list
```

可以看到自己的配置

### 如何连接远程

#### 本地项目到远程

在github中新建一个仓库，什么都不添加

```bash
git init #初始化git 生成一个.git文件夹在当前目录,默认创建master分支
git add . #添加文件到暂存区，.代表所有文件
git commit -m "your commit"
git remote add origin <your_ssh_url> #建议使用ssh url,原因下面有讲
git push -u origin master #推送远程，以后用git push就行
```

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222338011.png)

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222338838.png)

这样在github页面上你应该能看到你的添加的文件了

#### 远程项目到本地工作

```bash
git clone <http_url OR ssh_url>
cd example #进入项目文件夹
git pull #每次开启你的工作前，检查是否是最新的
git checkout master #切换到master分支 在我们的站点 这个分支是main
git add . #添加文件到暂存区，.代表所有文件
git commit -m "your commit"
```

以上操作都是正常操作

但是这时候推送，可能会遇到这样的问题：

鉴权失败：github移除了密码验证

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222338241.png)

这个时候实际上就是上文要使用ssh的问题

解决办法如下

```bash
git remote -v #可以看到的确git remote现在是http url 因为clone用的http
git remote rm origin
git reamote add origin git@github.com:cyan4run/example.git #添加ssh的远程
git remote -v #检查一下
```

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222338887.png)

然后愉快的推送到仓库

```bash
git push -u origin master #master是连接的远程分支，而在我们的站点中，这个分支是main
git push #第一次推送以后以后可以用这个
```

![](https://cdn.jsdelivr.net/gh/cyan4run/cdn_img/img/202404222339907.png)

另外的解决办法是，用token替代你的密码，不介绍了，去setting添加就行

### 关于多人协作

将多人协作fork到自己的账号仓库下以后，操作和 **远程项目到本地工作** 相同，参见上文

推送到自己的仓库以后，请提交pull request等待多人协作仓库管理员的审核，即可合并到主分支完成一次贡献

