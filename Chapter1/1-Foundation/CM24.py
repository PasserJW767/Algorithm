'''
描述
将一棵无穷大满二叉树的结点按根结点一层一层地从左往右编号，根结点编号为1。现给定a，b为两个结点。设计一个算法，返回a、b最近的公共祖先的编号。注意其祖先也可能是结点本身。

测试样例：
2，3
返回：1
'''

import math
# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        # 别人的方法
        while a!=b:
            if a > b:
                a //= 2
            elif a < b:
                b //= 2
        return a

if __name__ == '__main__':
    a = LCA().getLCA(8, 10)
    print(a)

'''
自己写的Version 2.0 减小了复杂度，但比不上别人写的
class LCA:
    def getLCA(self, a, b):
        # write code here
        if a == 1 or b == 1:
            return 1
        if a < b:
            layer_num = int(math.log(a) / math.log(2)) + 1
        else:            
            layer_num = int(math.log(b) / math.log(2)) + 1
        
        a_ancestors = self.compute_ancestors(a)
        b_ancestors = self.compute_ancestors(b)
        for node in a_ancestors:
            if node in b_ancestors:
                return node
    
    def compute_ancestors(self, x):
        ancestors_list = []
        while x != 1:
            x = int((x - 2) / 2) + 1
            ancestors_list.append(x)
        return ancestors_list
'''

'''
己写的Version 1.0 复杂度高
# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        if a == 1 or b == 1:
            return 1
        if a < b:
            layer_num = 0
            while not self.compute_layer(a, layer_num):
                layer_num += 1
        else:
            layer_num = 0
            while not self.compute_layer(b, layer_num):
                layer_num += 1
        
        # 祖先结点就有可能是位于pow(2, layer_num - 2) - 1到pow(2, layer_num - 1) - 1中的一个结点
        common_node = pow(2, layer_num - 1) - 1
        while not self.compute_common(a, b, common_node):
            common_node -= 1
        return common_node
            
    
    def compute_layer(self, num, x):
        if num > pow(2, x - 1) - 1 and num <= pow(2, x) - 1:
            return True
        else: 
            return False
    
    def compute_common(self, a, b, common_node):
        while a != 1:
            if common_node == a:
                break
            a = a // 2
        while b != 1:
            if common_node == b:
                break
            b = b // 2
        # print(a)
        # print(b)
        if a == b and a == common_node and b == common_node:
            return True
        else:
            return False
'''            