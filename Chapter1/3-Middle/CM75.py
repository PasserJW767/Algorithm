'''
描述
给定一个int正整数数组A及其大小n，请找出数组中每个元素的后面比它大的最小的元素（最接近的），若不存在则为-1。并返回每个元素对应的值组成的那个数组。保证n小于等于1000。

测试样例：
[11,13,10,5,12,21,3],7
[12,21,12,12,21,-1,-1]
'''

# -*- coding:utf-8 -*-

class NextElement:
    # 解法1：暴力破解法，复杂度O(n^2)
    def findNext(self, A, n):
        # write code here
        result = []
        for i in range(n):
            max_min = float('inf')
            for j in range(i+1, n):
                if A[j] > A[i]:
                    if A[j] < max_min:
                        max_min = A[j]
            if max_min == float('inf'):
                result.append(-1)
            else:
                result.append(max_min)
        return result
    
    # 解法2：非暴力破解法
    def findNext2(self, A, n):
        # write code here
        import numpy as np
        result = []
        for i in range(n-1):
            tmp = A[i+1:n]
            tmp = sorted(tmp)
            bound = np.searchsorted(tmp, A[i], side='left')
            if bound == len(tmp):
                result.append(-1)
            else:
                result.append(tmp[bound])
        result.append(-1)
        return result

if __name__ == '__main__':
    print(NextElement().findNext2([11,13,10,5,12,21,3],7))