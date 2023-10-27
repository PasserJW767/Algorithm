'''
描述
给定一个有正有负的整数数组A及其大小n，返回从前往后相加最大的连续数列的和。保证n的大小小于等于3000。

测试样例：
[1,2,3,-6,1]
返回：6
'''

'''
思路是：
用一个maxS保存最大的S值
如果数组中的数是正数直接相加
如果数组中的数是负数，且加上该负数以后，和仍然>0就相加
如果数组中的数是负数，且加上该负数以后，和<0，就将和置为0，等待下一个正数时候进行相加
'''

# -*- coding:utf-8 -*-

class MaxSum:
    def getMaxSum(self, A, n):
        # write code here
        maxS = -1
        s = 0
        for i in range(n):
            if A[i] > 0 or (A[i] < 0 and s + A[i] > 0):
                s += A[i]
                if s > maxS:
                    maxS = s
            elif A[i] < 0 and s + A[i] < s:
                s = A[i]
            
        return maxS
    
    '''
    感觉这个更加清晰易懂一些
    当前s与A[i]相加，正数直接相加，结果一般取last+A[i]
    当前s与A[i](<0)相加，加上该数后，若和仍然大于0就仍取last+A[i]
    当前s与A[i](<0)相加，加上该数后，若和比A[i]还小，说明出现了连续多个负数相加的情况，这时s=A[i]，等待到下一个正数出现后取该正数的值
    '''
    def getMaxSum_2(self, A, n):
        last = A[0]
        maxv = A[0]
        for i in range(1,len(A)):
            last = max(last+A[i],A[i])
            maxv = max(last,maxv)
        return maxv