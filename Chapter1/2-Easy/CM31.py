'''
描述
给定一个数组number包含了0到n的所有整数，但其中缺失了一个。现规定不能直接取数组number里的数，只能询问数组中第i个元素的二进制的第j位是多少(最低位为第0位)，用A[i][j]表示，且该操作的时间复杂度为常数。已知所有剩下的数按从小到大排列的二进制各位的值，请设计算法，在O(n)时间内返回这个缺失的数。

测试样例：
[[0],[0,1]]
返回：1
'''

# 因为数组是已经有序排列的了，就通过判断最后一位数是奇数还是偶数，便可以得到结果
# -*- coding:utf-8 -*-
class Finder:
    def findMissing(self, numbers, n):
        # write code here
        # True is zero, False is one
        flag = True
        for i in range(n):
            if flag:
                if numbers[i][0] == 1:
                    return i
                flag = False
            else: 
                if numbers[i][0] == 0:
                    return i
                flag = True
        return n
