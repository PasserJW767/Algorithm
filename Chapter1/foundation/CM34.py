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