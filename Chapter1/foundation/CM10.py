# 给定一个单向链表中的某个节点，请删除这个节点，但要求只能访问该节点。若该节点为尾节点，返回false，否则返回true

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Remove:
    def removeNode(self, pNode):
        # write code here
        # 理解错了题目的意思
        # nt = pNode.next
        # pNode = None
        # if nt == None:
        #     return False
        # else:
        #     return True
        if pNode.next == None:
            return False
        pNode.val = pNode.next.val
        pNode.next = pNode.next.next
        return True