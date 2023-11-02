'''
描述
给定string stringA和string stringB，编写程序确认两字符串包含的字符是否完全相同，注意大小写为不同字符，且考虑字符串中的空格，返回一个bool，代表两串是否由一样的字符组成。保证两串的长度都小于等于5000。

示例1
输入：
"This is nowcoder","is This nowcoder"
返回值：
true

示例2
输入：
"Here you are","Are you here"
返回值：
false
'''

# -*- coding:utf-8 -*-
class Same:
    # 一眼hash就能解决，复杂度O(n)
    def checkSam(self, stringA, stringB):
        # write code 
        hashA = {}
        for s in stringA:
            if s not in hashA.keys():
                hashA[s] = 1
            else:
                hashA[s] = hashA[s] + 1

        hashB = {}
        for s in stringB:
            if s not in hashB.keys():
                hashB[s] = 1
            else:
                hashB[s] = hashB[s] + 1

        for k in hashA.keys():
            if k not in hashB.keys():
                return False
            else:
                if hashA[k] != hashB[k]:
                    return False
        
        return True
    
    # 别人的答案。。。一眼简洁
    # 注意题目的重点：两字符串包含的字符是否完全相同，不用考虑数量
    def checkSam(self, stringA, stringB):
        print(set(stringA))
        return set(stringA)==set(stringB)



if __name__ == '__main__':
    print(Same().checkSam("Here you are","Are you here"))