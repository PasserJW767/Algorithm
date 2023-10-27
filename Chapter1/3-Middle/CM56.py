'''
描述
已知一个有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，且矩阵的行和列都是从小到大有序的。设计查找算法返回所查找元素的二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。

数据范围：
0≤n,m≤1000，矩阵中的任何元素满足 0＜mat_(i,j)≤1000000
要求：空间复杂度O(1)，时间复杂度O(n+m)

示例1
输入：
[[1,2,3],[4,5,6]],2,3,6
返回值：
[1,2]

示例2
输入：
[[1,2,3]],1,3,2
返回值：
[0,1]
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param mat int整型二维数组
# @param n int整型
# @param m int整型
# @param x int整型
# @return int整型一维数组
#
class Solution:
    # 方法1：最简单地暴力搜索，时间复杂度是O(nm)
    def findElement(self, mat: list[list[int]], n: int, m: int, x: int) -> list[int]:
        # write code here
        for i in range(n):
            for j in range(m):
                if mat[i][j] == x:
                    return [i, j]

    # 方法2：题目中提到：“矩阵的行和列都是从小到大有序”，可以从左下角开始搜索，最差情况是从左下角走到右上角，时间复杂度O(n+m)
    def findElement2(self, mat: list[list[int]], n: int, m: int, x: int) -> list[int]:
        row = n - 1
        col = 0
        while col <= m - 1 and row >= 0:
            if mat[row][col] > x:
                row = row - 1
            elif mat[row][col] < x:
                col = col + 1
            elif mat[row][col] == x:
                return [row, col]
        # 无解
        return None
    
    # 方法3：枚举每一行，对每一行进行二分搜索，复杂度O(nlogm)
    def findElement3(self, mat: list[list[int]], n: int, m: int, x: int) -> list[int]:
        for i in range(n):
            # x 小于 这一行最小值   或   大于 这一行最大值，则肯定不在这一行
            if x < mat[i][0] or x > mat[i][m - 1]:
                continue
            
            # 二分查找的low值和high值
            low = 0
            high = m - 1
            while low <= high:
                mid = (low + high) // 2
                if mat[i][mid] > x:
                    high = mid - 1
                elif mat[i][mid] < x:
                    low = mid + 1
                else:
                    return [i, mid]

if __name__ == '__main__':
    print(Solution().findElement2([[1,2,3],[4,5,6]],2,3,6))