'''
描述
给定一个int数组A和它的大小n，对于这组数能组成的任意两个数组，若前面一个大于后面一个数字，则这两个数字组成一个逆序对。请设计一种高效的算法返回A中存在的逆序对个数。要求n不大于5000。

测试样例：
[1,2,3,4,5,6,7,0],8
返回：7
'''

# -*- coding:utf-8 -*-

class AntiOrder:
    def count(self, A, n):
        # write code here
        if n == 1:
            return 0
        middle = n // 2
        # S1 = A[:middle+1]的逆序对数
        S1 = self.count(A[:middle], middle)
        # S2 = A[middle+1:]的逆序对数
        S2 = self.count(A[middle:], n-middle)
        # S3 = 跨越middle的逆序对数
        # S1和S2通过分而治之求解，我们只需要求解S3的逆序对数
        
        # 解法1：简单地暴力枚举，时间复杂度O(n^2)
        S3 = 0
        for i in range(middle):
            for j in range(middle,n):
                if A[j] < A[i]:
                    S3 += 1
        
        # 解法2：将两段数组排序后，再通过计算求解
        # 使用二分查找定位，找到一个大于A[j]的数，复杂度n/2log(n/2)
        S3 = 0
        A[:middle] = sorted(A[:middle])
        A[middle:] = sorted(A[middle:])
        for j in range(middle, n):
            for i in range(middle):
                if A[j] < A[i]:
                    S3 += (middle - i) 
                    break

    
if __name__ == '__main__':
    print(AntiOrder().count([1,2,3,4,5,6,7,0],8))