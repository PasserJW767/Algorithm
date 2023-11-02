'''
描述
已知一个数组A及它的大小n，在读入这串数的时候算出每个数的秩，即在当前数组中小于等于它的数的个数(不包括它自身)。从而返回一个int数组，元素为每次加入的数的秩。保证数组大小小于等于5000。

测试样例：
[1,2,3,4,5,6,7],7
返回：[0,1,2,3,4,5,6]
'''

# -*- coding:utf-8 -*-

class Rank:
    def getRankOfNumber(self, A, n):
        # write code here
        result = []
        B=sorted(A)
        for i in range(n):
            idx = B.index(A[i])
            result.append(idx)
        return result

if __name__ == '__main__':
    Rank().getRankOfNumber([1,2,3,4,5,6,7],7)