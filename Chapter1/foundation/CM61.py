# 给定一个int数组AB，要求编写一个函数，不使用任何临时变量直接交换第零个元素和第一个元素的值。并返回交换后的数组。

# 测试样例：
# [1,2]
# 返回：[2,1]

# -*- coding:utf-8 -*-

class Exchange:
    def exchangeAB(self, AB):
        # write code here
        # 假设a=1010, b=1111
        # a XOR b, A和B有差异的位为1;无差异的位为0。此时异或结果为0101，保存到a中
        # 想要将原本a的值换到b上，只需要将b和a算一下异或，b和a此时在1,3位不一样，为1，则b=1010
        # 再将b的结果与1010求异或，赋予a，为1111
        # Java和C的异或运算符和python的一样，只是后面多了分号，不赘述
        AB[0] = AB[0] ^ AB[1]
        AB[1] = AB[0] ^ AB[1]
        AB[0] = AB[0] ^ AB[1]
        return AB