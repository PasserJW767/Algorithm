'''
描述
给定一个string数组str,其是由一个排过序的字符串数组插入了一些空字符串得到的，同时给定数组大小n和需要查找的string x，请用时间复杂度在log级别的算法返回该串的位置(位置从零开始)。

测试样例：
["a","b","","c","","d"],6,"c"
返回：3
'''

# -*- coding:utf-8 -*-

class Finder:
    '''
    初始思路，处理空字符串的方法太复杂了
    '''
    def findString(self, s, n, x):
        # write code here
        # 算出所有""的位置
        empty_idx = []
        tmp = s
        final_val = 0
        a = 0
        # 复杂度O(n)
        while "" in tmp:
            if len(tmp) == 0:
                break
            else:
                if a != 0:
                    final_val = final_val + tmp.index("") + 1
                else:
                    final_val = final_val + tmp.index("")
                    a += 1                
                empty_idx.append(final_val)
                tmp = s[final_val+1:]
        
        # 剔除所有""，复杂度O(n)
        while "" in s:
            s.remove("")

        # 有序数组，二分查找，复杂度O(logn)
        low = 0
        high = n - 1
        mid = -1
        while low <= high:
            mid = (low + high) // 2
            if s[mid] < x:
                low = mid + 1
            elif s[mid] > x:
                high = mid - 1
            else:
                break
        
        result = mid
        for idx in empty_idx:
            if mid >= idx:
                result += 1
        return result
    
    def findString2(self, s, n, x):
        '''
        思路是：如果low是空字符串的话，low不断右移；如果high是空字符串的话，high不断左移；
        直到两侧不为空，求解mid
        '''
        low = 0
        high = n - 1
        mid = -1
        while low <= high:
            # 如果左侧为空，low不断+1
            while s[low] == "":
                low += 1
            # 如果右侧为空，high不断-1
            while s[high] == "":
                high -= 1
            # 算mid
            mid = (low + high) >> 1
            if s[mid] == x:
                return mid
            # 如果mid为空的处理
            while s[mid] == "" and mid > low:
                mid -= 1
            # 正常二分
            if s[mid] < x:
                low = mid + 1
            elif s[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    print(Finder().findString2(["a","b","","c","","d"],6,"c"))