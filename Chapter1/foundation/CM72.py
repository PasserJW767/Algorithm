'''
描述
给定两个int A和B。编写一个函数返回A+B的值，但不得使用+或其他算数运算符。

测试样例：
1,2
返回：3
'''

class UnusualAdd:
    def addAB(self, A, B):
        # write code here
        A_2 = bin(A)[2:]
        B_2 = bin(B)[2:]
        result = ''
        flag = False
        # 对齐A_2和B_2
        if len(A_2) < len(B_2):
            zero_str = ''
            for i in range(abs(len(A_2) - len(B_2))):
                zero_str += '0'
            A_2 = zero_str + A_2
        elif len(B_2) < len(A_2):
            zero_str = ''
            for i in range(abs(len(A_2) - len(B_2))):
                zero_str += '0'
            B_2 = zero_str + B_2
        # 根据不同的情况进行相加，用flag标志进位
        for i in range(len(A_2) - 1, -1, -1):
            if (A_2[i] == '1' and B_2[i] == '0') or (B_2[i] == '1' and A_2[i] == '0'):
                if flag:
                    result = '0' + result
                else:
                    result = '1' + result
            elif A_2[i] == '0' and B_2[i] == '0':
                if flag:
                    result = '1' + result
                    flag = False
                else:
                    result = '0' + result
            elif A_2[i] == '1' and B_2[i] == '1':
                if flag:
                    result = '1' + result
                else:
                    result = '0' + result
                    flag = True
        if flag:
            result = '1' + result
        return int(result, base=2)

            

if __name__ == '__main__':
    UnusualAdd().addAB(16, 64)