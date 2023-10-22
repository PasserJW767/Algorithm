'''
已知数组A[0..n-1]和数组大小n（升序数组，元素值各不相同），若存在A[i]=i则称该数组有魔术索引，请判断该数组是否存在魔术索引，返回值为bool，要求复杂度优于o(n)。

测试样例：
[1,2,3,4,5]
返回：false
'''
# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        for i in range(n):
            if A[i] == i:
                return True
        return False