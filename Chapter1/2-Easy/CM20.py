'''
描述
给定一个元素各不相同的有序序列int[] vals（升序排列）,请编写算法创建一棵高度最小的二叉查找树，并返回二叉查找树的高度。
'''

# -*- coding:utf-8 -*-
class MinimalBST:
    def buildMinimalBST(self, vals):
        # write code here
        x = len(vals)
        height = 0
        while x != 1:
            x = x // 2
            height += 1
        return height+1
    
    def buildMinimalBST_2(self, vals):
        # write code here
        return math.log2(vals) + 1