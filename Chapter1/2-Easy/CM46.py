'''
描述
给定一个字符串A和其长度n，请返回一个bool值代表它是否为一个合法的括号串（只能由括号组成）。

测试样例：
"(()())",6
返回：true
测试样例：
"()a()()",7
返回：false
测试样例：
"()(()()",7
返回：false
'''

# -*- coding:utf-8 -*-
'''
思路：本来想这道题用栈做的，但是忘了python如何初始化栈，于是用了更简单的办法
其实就是一个左括号匹配右括号的问题，有点类似于生产者-消费者，于是我定义了一个变量num来存储在目前左括号出现的情况下，允许有多少个右括号出现
当出现左括号时，num+=1（生产者放入一个产品），当出现右括号时，num-=1（消费者消耗一个产品），如果中间遇到字符时，若缓冲变量（num）为0，说明这个字符不在括号中间，就直接返回FALSE
最后检测num的值，如果num是0，说明括号正好配对完毕，返回True
'''
class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        A = list(A)
        num = 0
        for content in A:
            if content == '(':
                num = num + 1
            elif content == ')':
                num = num - 1
            else:
                if num == 0:
                    return False
                else:
                    continue
        if num != 0:
            return False
        else:
            return True

    # 栈的做法
    def chkParenthesis_Stack(self, A, n):
        res = []
        for i in range(n):
            if A[i] == '(':
                res.append(A[i])
            elif A[i] == ')' and len(res) != 0:
                res.pop(-1)
            elif A[i] == ')' and len(res) == 0: # 没有括号可以弹出
                return Fals
        return True


if __name__ == '__main__':
    print(Parenthesis().chkParenthesis("()(()()",7))
