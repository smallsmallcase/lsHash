<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

1.LSH算法简介：

我们将这样的一族hash函数 H={h:S→U} 称为是(r1,r2,p1,p2)敏感的，如果对于任意H中的函数h，满足以下2个条件：

如果d(O1,O2)<r1，那么Pr[h(O1)=h(O2)]≥p1

如果d(O1,O2)>r2，那么Pr[h(O1)=h(O2)]≤p2

其中，O1,O2∈S，表示两个具有多维属性的数据对象，d(O1,O2)为2个对象的相异程度，也就是1 - 相似度。其实上面的这两个条件说得直白一点，就是当足够相似时，映射为同一hash值的概率足够大；而足够不相似时，映射为同一hash值的概率足够小。

2.项目简介：

paper文件夹中存放的是我在中国论文网爬到的论文，用的是scrapy库。

test.txt是选自其中的一篇，并且添加了一些其他论文中的文字。

lshash是我安装的第三方库

main.py是代码实现

3.用到的库：

lshash,jieba
