# 给定两个整数A和B。编写函数，返回将整数A转变成整数B所需要改变的数位个数。

# 测试样例：
# 10,5
# 返回：4

# -*- coding:utf-8 -*-
class Transform:
    def calcCost(self, A, B):
        # write code here
        # 异或后求1的个数就是结果
        A = A ^ B
        # 将A转换为二进制，并将首位的"0b"去掉
        A = bin(A)[2:]
        # 统计A中1的个数
        return A.count('1')
        # 除了这种统计二进制1的个数以外，还有一种办法是让数A逐步与数A-1相与，直到A=0为止
        # count = 0
        # while(A!=0):
        #     A = A & (A-1)
        #     count += 1
        # return count
