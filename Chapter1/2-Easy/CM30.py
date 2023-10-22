'''
描述
给定一个int x，交换其二进制的奇数位和偶数位，并返回交换后的数int。

测试样例：
10
返回：5
'''
# -*- coding:utf-8 -*-
class Exchange:
    def exchangeOddEven(self, x):
        # write code here
        x = bin(x)[2:]
        ji = []
        ou = []
        for i in range(len(x)):
            if i % 2 == 0:
                ou.append(x[-1-i])
            else:
                ji.append(x[-1-i])
        num = len(x)
        if len(ji) != len(ou):
            ji.append('0')
            num = len(x) + 1
        ou.reverse()
        ji.reverse()
        result = []
        for i in range(num):
            if i % 2 == 0:
                result.append(ou[i // 2])
            else:
                result.append(ji[i // 2])
        return int("".join(result), 2)

    def exchangeOddEven_2(self, x):
        # 0x55555555是为了取出偶位数
        # 0xAAAAAAAA是为了取出奇位数
        odd = 0x55555555&x >>1  #偶位上的数字右移
        even = 0xAAAAAAAA&x <<1 #奇位上的数左移
        # 偶位移到奇位
        # 奇位移到偶位
        # 运用或运算得到结果
        return even | odd
        