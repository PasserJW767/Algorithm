'''
描述
平衡的定义如下，已知对于树中的任意一个结点，若其两颗子树的高度差不超过1，则我们称该树平衡。现给定指向树根结点的指针TreeNode* root，请编写函数返回一个bool，表示该二叉树是否平衡。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
这题我一开始忽略了一个点：我只判断了根节点的两颗子树高度差不超过1，但是没判断根节点下的所有子树高度差不超过1
这道题的思路是：
1. 首先有一个根节点。如果根节点的左子树和右子树都是None，那这棵树肯定是平衡的
2. 判断完根节点，再判断其所有的左右子树是否为平衡树，这就需要用到递归
3. 求出每个节点的左子树高度和右子树高度，如果高度差小于等于1，就说明这棵子树是平衡的，遍历所有的子树就可以知道这是不是一个平衡二叉树，但凡一颗子树不是平衡的，则所有的都不是平衡的
'''

'''
若一颗树为平衡二叉树，对其所有的子树(包括root.left和root.right)，abs(左子树高度-右子树高度) <= 1
depth用于求该结点的子树高度，返回最高的那一棵
'''

class Balance:
    def isBalance(self, root):
        # write code here
        if root is None:
            return True
        return self.isBalance(root.left) and self.isBalance(root.right) and abs(self.depth(root.left) - self.depth(root.right)) <= 1
    
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

'''
一开始写的代码，只判断了根节点是否为平衡树，没有对其左右节点进一步判断

class Balance:
    def isBalance(self, root):
        # write code here
        if root.left == None and root.right == None:
            return True
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        print(left_depth)
        print(right_depth)
        if abs(left_depth - right_depth) <= 1:
            return True
        else:
            return False
    
    def depth(self, root):
        left = 0
        right = 0
        if root.left == None and root.right == None:
            return 1
        if root.left != None:
            left = self.depth(root.left) + 1
        if root.right != None:
            right = self.depth(root.right) + 1
        
        if left >= right:
            return left
        else:
            return right

'''

if __name__ == '__main__':
    root = TreeNode(1)

    left_node_1 = TreeNode(2)
    right_node_1 = TreeNode(3)

    left_node_2 = TreeNode(4)
    right_node_2 = TreeNode(5)
    
    left_node_3 = TreeNode(6)

    root.left = left_node_1
    root.right = right_node_1

    left_node_1.left = left_node_2
    left_node_1.right = right_node_2

    right_node_2.left = left_node_3

    print(Balance().isBalance(root))
        