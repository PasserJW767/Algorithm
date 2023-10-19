# 现以斜率和截距的形式给出直角坐标系上的两条直线，即double s1，double s2，double y1，double y2，分别代表直线1和2的斜率(即s1,s2)和截距(即y1,y2)，请返回一个bool，判断这两条直线会不会相交（重合也算）。

# 测试样例：
# 3.14,3.14,1,2
# 返回：false

# -*- coding:utf-8 -*-
class CrossLine:
    def checkCrossLine(self, s1, s2, y1, y2):
        # write code here
        # if s1 == s2:
        #     if y1 == y2:
        #         return True
        #     return False
        # return True
        # 有一个问题就是，不能使用"=="直接判断两个浮点数是否相等，而应该利用相减后的值是否小于某个值来判断是否相等，这是其特性
        epson = 1e-10
        if abs(s1-s2) < epson and abs(y1-y2) < epson:
            return True
        if abs(s1-s2) > epson:
            return True
        return False