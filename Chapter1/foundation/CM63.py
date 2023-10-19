# 给定int a和intb，在不使用if-else等比较和判断运算符的情况下返回较大的那个数。若两数相同则返回任意一个。

# 测试样例：
# 1，2
# 返回：2

# -*- coding:utf-8 -*-

class Max:
    def getMax(self, a, b):
        # write code here
        # 利用位运算，首先计算相减的结果
        result = a - b
        # 将结果进行右移31位，并与1相与。如果结果是一个正数，相与后为0，如果结果是一个负数，相与后为1
        result = (result >> 31) & 1
        # 如果result相与后为0，说明a>b；如果result相与后为1，说明a<b
        return a * (1 - result) + b * result
    
    def getMax_v2(self, a, b):
        # 计算出a-b的结果
        b = a - b
        # 如果b是一个正数，说明a > b，此时直接返回a的结果；如果b是一个负数，说明a < b，此时需要返回a减去二者之差(a - b)，相当于a+二者之差的绝对值，=b
        a -= b & (b >> 31)
        print(a)
        return a

if __name__ == '__main__':
    Max().getMax_v2(9, 6)