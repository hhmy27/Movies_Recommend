# 基于协同过滤的电影推荐系统

**数据集**：MovieLens的ml-latest-small数据集，大概600多个用户，大概9700多部电影，10万条评分记录

**电影详细信息**：ml-latest-small提供了一个CSV文件，里面有电影在IMDB上面的ID编号，用爬虫爬下来的，爬虫代码链接稍后公开
https://blog.csdn.net/hhmy77/article/details/106389370 这篇博客里面有爬虫的代码

**技术栈**：web服务器用的是Django，数据库MySQL，前端用的bootstrap做渲染

**算法**：使用的是UserCF做推荐，600多个用户用UserCF比较快。ItemCF只计算了相似度，在展示相似电影栏里面用到。算法稍后在另一个repo公开，我还没有建好

详细版本：

1. Django 2.0
2. Python 3.6

运行方法：

下载到本地，确保你之前已经配置好Django环境，使用Pycharm打开本项目运行即可



缺点：

1. 数据库密码用明文存储，当时存储的时候没有想到用加密存储
2. 注释了csrf中间件，没有继续研究这个部分
3. 只在本地运行测试，没有部署到服务器上
4. 推荐大概需要3~4秒的时间，并且推荐的结果中热门电影出现的概率很高（当年的星战，黑客帝国，阿甘正传，肖申克的救赎几乎每次都会推荐。。）
5. 界面有些简陋

页面展示：

首页：

![tEkFIA.md.png](https://s1.ax1x.com/2020/05/27/tEkFIA.md.png)

电影详情页：Toy Story为例。黄色提示条下面是相似电影（使用ItemCF计算相似度的方法得出）

![tEkPVH.md.png](https://s1.ax1x.com/2020/05/27/tEkPVH.md.png)

用户的评分记录：

![tEkiad.md.png](https://s1.ax1x.com/2020/05/27/tEkiad.md.png)

推荐效果：使用UserCF

![tEkprD.md.png](https://s1.ax1x.com/2020/05/27/tEkprD.md.png)



