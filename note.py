# @Time    : 2017/10/15 21:35
# @Author  : Jalin Hu
# @File    : note.py
# @Software: PyCharm
from lshash.lshash import LSHash
if __name__ == '__main__':
    lsh = LSHash(hash_size=6, input_dim=8)
    lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
    lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
    lsh.index([3, 4, 5, 6, 7, 8, 9, 10])
    lsh.index([10, 12, 99, 1, 5, 6, 24, 20])
    res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7], num_results=2)
    print(res)

