# 项目结构介绍
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
# 新增内容说明
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
# 贡献指南
本网站欢迎一切贡献 
不过课程内容只面向HITWH的课程内容范围，如果你想要为本网站进行贡献，以下是一些指南。
## 本地构建
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


# 贡献守则
- 对于课程请进行客观的评价，尽量不要带有主观色彩
- 对于外部资源，请尽量插入链接，不要将文件传入本 repo
- 尽量不要上传有版权的文件，例如课件等
- 对于自己的笔记、复习提纲等材料：
    - 如果有自己的网站，推荐放在自己的网站并在此插入链接
    - 也可以将文件上传到对应课程文件夹中，并插入相对链接
- 尽量规范编写 markdown，避免出现格式错误，**先在自己的本地进行测试！**

# 贡献方式
通过 PR（即 Pull Request）的形式来进行贡献，具体流程：

- 在 GitHub 网页端点击右上角的 fork，将本仓库 fork 到自己的账号下
- 在自己账号的对应仓库中进行修改
- 修改完成后，在自己的仓库内Pull requests中 点击 New pull request，提交一个 PR
- ![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221056918.png)
- ![image.png](https://cdn.jsdelivr.net/gh/wandering-the-earth/blog-img//blog/202404221057922.png)

- 等待管理员的审核、修改，然后合并到本 repo 中

# 项目规划
```
general: 通识课
basic: 数理基础课
culture：文化素质课
major：CS 专业类课程
labs：学校各个实验室的技术栈介绍和项目（包括老师的实验室）
salon：俱乐部可公开的分享会文档
CTF-WP：俱乐部参加的CTF比赛题解
```
