'''
描述
给定两个int A和B。编写一个函数返回A+B的值，但不得使用+或其他算数运算符。

测试样例：
1,2
返回：3
'''

class UnusualAdd:
    # 我的解法
    def addAB(self, A, B):
        # write code here
        A_2 = bin(A)[2:]
        B_2 = bin(B)[2:]
        result = ''
        flag = False
        # 对齐A_2和B_2
        if len(A_2) < len(B_2):
            A_2 = "0" * abs(len(A_2) - len(B_2)) + A_2
        elif len(B_2) < len(A_2):
            B_2 = "0" * abs(len(A_2) - len(B_2)) + B_2
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

    # 别人的解法 
    '''
    试想二进制0101和1101的相加过程
    0 1 0 1
    1 1 0 1
    其实可以看成是不带进位的结果1000和进位产生的1010相加。

    而“不带进位的加法”其实就是异或运算，“进位”其实就是只有两个1的时候才会出现，
    也就是与运算，只是因为进了一位，所以还要往左移动一位。

    这样就将两个数相加通过位运算转换成了不带进位的加法结果和进位相加的问题，
    反复进行下去，最后只要没有进位了，相加的结果也就得到了。
    '''
    def addAB2(self, A, B):
        print(A)
        print(B)
        while(B!=0) :
            t = A^B
            print(A&B)
            B = (A&B)<<1
            A = t
            print(A)
            print(B)
        return A

if __name__ == '__main__':
    UnusualAdd().addAB(16, 64)