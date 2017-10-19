# @Time    : 2017/10/19 10:09
# @Author  : Jalin Hu
# @File    : main.py
# @Software: PyCharm
import os
import jieba
import collections
import random
from lshash.lshash import LSHash

'''函数说明:获取词汇集合

Parameters:
    foldpath - 论文文件夹路径
Returns:
    datalist_dict - 词集字典（名字：词集）'''


def textprocess(foldpath):
    datalist = []
    classlist = []
    # datalist_dict = {}
    vocabset = collections.defaultdict(int)
    filelist = os.listdir(foldpath)  # 获取paper文件夹下面所有的文件名
    for file in filelist:
        with open(os.path.join(foldpath, file), 'r', encoding='utf-8') as f:
            sequence = f.read()
            key = file.strip('.txt').strip('[').strip(']').strip(r"\\'")

            datalist.append(jieba.lcut(sequence, cut_all=False))
            classlist.append(key)
            print(key, ':**************ok')
    for content in datalist:
        for word in content:
            vocabset[word] += 1
    all_word_sorted = sorted(vocabset.items(), key=lambda e: e[1], reverse=True)
    all_word_list, all_word_nums = zip(*all_word_sorted)
    return datalist, classlist, list(all_word_list)

    # # return datalist, classlist
    # data_class_list = list(zip(datalist, classlist))
    # # print(data_class_list)
    # random.shuffle(data_class_list)
    # index = int(len(data_class_list) * testsize) + 1  # 训练集和测试集区分的索引
    # traindatalist, trainclasslist = zip(*(data_class_list[index:]))  # 训练集解压缩
    # testdatalist, testclasslist = zip(*(data_class_list[:index]))  # 测试集解压缩
    #
    # # 统计训练集词频
    # allworddict = collections.defaultdict(int)  # 创建默认字典
    # for word_list in traindatalist:
    #     for word in word_list:
    #         allworddict[word] += 1
    #
    # # 根据键的值倒序排列
    # all_word_sorted = sorted(allworddict.items(), key=lambda e: e[1], reverse=True)
    # all_word_list, all_word_nums = zip(*all_word_sorted)
    # all_word_list = list(all_word_list)
    # return all_word_list, traindatalist, trainclasslist, testdatalist, testclasslist


'''函数说明:读取文件里的内容，并去重

Parameters:
    words_file - 文件路径
Returns:
    words_set - 读取的内容的set集合'''


def make_word_set(word_file):
    word_set = set()
    with open(word_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) > 0:
                word_set.add(word)
    return word_set


'''函数说明:文本特征选取

Parameters:
    all_words_list - 训练集所有文本列表
    deleteN - 删除词频最高的deleteN个词
    stopwords_set - 指定的结束语
Returns:
    feature_words - 特征集'''


def word_dict(vocabset, deleteN, stopwords_set):
    feature_words = []
    for i in range(deleteN, len(vocabset), 1):
        if not vocabset[i].isdigit() and vocabset[i] not in stopwords_set and 1 < len(
                vocabset[i]) < 5:
            feature_words.append(vocabset[i])
    return feature_words


'''函数说明:向量化

Parameters:
    vocablist - 所有特征集
    inputset - 输入的词集
Returns:
    returnvec - 向量'''


def bagof_word2vec(vocablist, inputset):
    returnvec = [0] * len(vocablist)
    for word in inputset:
        if word in vocablist:
            returnvec[vocablist.index(word)] += 1
        else:
            print('word:', word, 'is not in the list_vec')
    return returnvec


if __name__ == '__main__':
    datalist, classlist, vocabset = textprocess('./paper')  # 获取每篇论文的词集
    stop_word_file = './stopwords_cn.txt'
    stop_word_set = make_word_set(stop_word_file)
    feature_words = word_dict(vocabset, 0, stop_word_set)
    trainMat = []

    lsh = LSHash(hash_size=16, input_dim=len(feature_words))
    for postinDoc in datalist:
        trainMat_vec = bagof_word2vec(feature_words, postinDoc)  # 训练集向量化
        trainMat.append(trainMat_vec)
        lsh.index(trainMat_vec)

    testfile = './test.txt'
    testlist = []
    with open(testfile, 'r', encoding='utf-8') as f:
        sequence = f.read()
        testlist.append(jieba.lcut(sequence, cut_all=False))
        testvect = bagof_word2vec(feature_words, testlist[0])

    re = lsh.query(testvect, num_results=2)
    print('最相似的论文是：', classlist[trainMat.index(list(re[0][0]))])
