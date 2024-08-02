代码分为两部分，第一部分get_links，先递归获取需要爬取的url列表
注意替换url需要用一个主网站去递归寻找里面其他的网页。当爬取计算机学院列表时出现递归到其他学院官网的现象
第二部分为get_information,为访问url列表里的链接去解析整个网页
test部分测试大学官网网站，目前完成测试阶段，未能访问采取手动获取。代码继续精进至自动记录错误等。访问策略为替换网址元素为大学缩写

0416
test部分为将大学英文缩写转成url链接
下一步把两种信息爬取出来，把大学列表转换成url获取到，最后要有学科分类
https://www.google.com/search?q=

##
university_info获取学校列表
get_SZurl尝试获取百度检索到的网页中的链接，未实现，直接解析
尝试爬取搜索结果链接test_get_SZurl采用标签爬取，未实现
软科排名API
https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=10&year=2023