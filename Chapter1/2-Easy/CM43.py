'''
描述
已知一个数组A[0..n-1]和其大小n（不下降序列，元素值可能相同），判断是否存在A[i]=i，返回值为bool，要求时间复杂度小于o(n)。

测试样例：
[1,1,3,4,5]
返回：true
'''
# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        for i in range(n):
            if A[i] == i:
                return True
        return False