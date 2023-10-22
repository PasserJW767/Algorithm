'''
描述
给定一个二维数组board，代表棋盘，其中元素为1的代表是当前玩家的棋子，0表示没有棋子，-1代表是对方玩家的棋子。当一方棋子在横竖斜方向上有连成排的及获胜（及井字棋规则），返回当前玩家是否胜出。

测试样例：
[[1,0,1],[1,-1,-1],[1,-1,0]]
返回：true
'''
# -*- coding:utf-8 -*-

class Board:
    def checkWon(self, board):
        # write code here
        for i in range(len(board[0])):
            line_sum_1 = 0
            line_sum_2 = 0
            for j in range(len(board[0])):
                line_sum_1 += board[i][j]
                line_sum_2 += board[j][i]
            if line_sum_1 == 3 or line_sum_2 == 3:
                return True
        line_sum_1 = 0
        line_sum_2 = 0
        for i in range(len(board[0])):
            line_sum_1 += board[i][i]
            line_sum_2 += board[i][len(board[0]) - 1 - i]
        if line_sum_1 == 3 or line_sum_2 == 3:
            return True
        return False