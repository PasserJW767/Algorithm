'''
描述
给定2个字符串s1和s2，请判断s2是否为s1旋转而成，返回bool值。字符串中字符为英文字母和空格，区分大小写，字符串长度小于等于1000。

测试样例：
"Hello world","worldhello "
返回：false
"waterbottle","erbottlewat"
返回：true
'''

'''
想了很久不知道应该怎么实现，后来发现实际上如果s2是s1旋转后的子串的话，就必定满足s2是s1+s1中的其中一部分这个条件
'''

# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        return len(s1) == len(s2) and s2 in (s1+s1)
