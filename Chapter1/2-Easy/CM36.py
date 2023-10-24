'''
描述
给定两个vecotrA和B，分别代表平面上两个正方形的四个顶点。已知正方形上下两条边与x轴平行，请找出一条直线，能够平分这两个正方形，返回值为vector，代表所求直线的斜率和截距，注意保证斜率存在。

测试样例：
[(0,0),(0,1),(1,1),(1,0)],[(1,0),(1,1),(2,0),(2,1)]
返回：[0.0，0.5]
'''

'''
这道题有点不会写，然后看了题解才知道：所求直线肯定经过两个正方形的中心点，利用两个中心点的坐标求出斜率与截距即可 -.- 脑子愚钝
还有一个要注意的是，要想让结果为浮点数，就要除以浮点数而不是除以一个整数（在计算中心点的时候），要不然会导致计算出来的坐标是浮点数
'''

# -*- coding:utf-8 -*-
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Bipartition:
    def getBipartition(self, A, B):
        # write code here
        middle_A = Point((A[0].x + A[2].x) / 2.0, (A[0].y + A[2].y) / 2.0)
        middle_B = Point((B[0].x + B[2].x) / 2.0, (B[0].y + B[2].y) / 2.0)

        # 直线y=kx+b
        k = (middle_A.y-middle_B.y) / (middle_A.x-middle_B.x)
        b = y1 - k*x1

        return [k,b]