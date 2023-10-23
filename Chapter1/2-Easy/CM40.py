'''
给定两个正整数int x,int y，代表一个x乘y的网格，现有一个机器人要从网格左上角顶点走到右下角，每次只能走一步且只能向右或向下走，返回机器人有多少种走法。保证x＋y小于等于12。

测试样例：
2,2
返回：2
'''

# -*- coding:utf-8 -*-
class Robot:
    # 递归法，因为题目说明了x+y<=12，所以不会超时
    def countWays(self, x, y):
        # write code here
        if x <= 0 or y <= 0: 
            return 0
        elif x == 1 or y == 1:
            return 1
        return self.countWays(x - 1, y) + self.countWays(x, y - 1)
    
    # 动态规划法，因为题目说明了x+y<=12，所以不会超时
    '''
        0   1   2   3   4   5   ... 12
    0   0   0   0   0   0   0   ...
    1   0   0   1   1   1   1   ...
    2   0   1   2   3   4   5   ...
    3   0   1   3   6   10  15  ...
    4   0   1   4   10  20  35  ...
    5   0   1   5   15  35  70  ...
    ... ... ... ... ... ... ... ...
    12
    '''
    def countWays_2(self, x, y):
        # write code here
        arr = [[0 for _ in range(13)] for _ in range(13)]
        for i in range(2, 13):
            arr[i][1] = 1
        for j in range(2, 13):
            arr[1][j] = 1
        for i in range(2, 13):
            for j in range(2, 13):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[x][y]


if __name__ == '__main__':
    print(Robot().countWays_2(4, 4))