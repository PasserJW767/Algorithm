'''
描述
给定一个string数组article（有单词构成）和数组中元素的个数n，同时给定数组中的两个单词x和y。请返回这两个单词的最短距离（比如两个单词分别在第1和第3个位置，则最短距离为2）。保证两个单词不相同且均在数组中出现，同时保证数组中单词数小于等于1000。
'''

# -*- coding:utf-8 -*-

class Distance:
    '''
    我写的方法，复杂度应该是O(nlogn)，但是有一些测试用例无法通过
    '''
    def getDistance(self, article, n, x, y):
        # write code here
        # article = article.split(' ')
        print(article)

        x_idx = []
        tmp = article
        save_value = 0
        a = 0
        while x in tmp:
            if a != 0:
                save_value = save_value + tmp.index(x) + 1
            else:
                save_value = save_value + tmp.index(x)
                a += 1
            x_idx.append(save_value)
            tmp = article[save_value+1:]
        
        y_idx = []
        tmp = article
        save_value = 0
        a = 0
        while y in tmp:
            if a != 0:
                save_value = save_value + tmp.index(y) + 1
            else:
                save_value = save_value + tmp.index(y)
                a += 1
            y_idx.append(save_value)
            tmp = article[save_value+1:]

        print(x_idx)
        print(y_idx)

        min_distance = float('inf')
        epoch_result = float('inf')
        left = 0
        right = len(x_idx)-1
        for y in y_idx:
            insert_loc = -1
            while left < right:
                mid = (left + right) // 2

                if x_idx[mid] == y:
                    insert_loc = mid
                    break
                elif x_idx[mid] < y:
                    left = mid + 1
                else:
                    right = mid
            insert_loc = right
            if insert_loc == 0:
                epoch_result = abs(x_idx[0] - y)
            elif insert_loc == len(x_idx):
                epoch_result =  abs(y - x_idx[len(x_idx)])
            else:
                epoch_result = min(abs(y - x_idx[insert_loc - 1]), abs(x_idx[insert_loc] - y))
            if epoch_result < min_distance and epoch_result > 0:
                min_distance = epoch_result
        
        return min_distance

        # import numpy as np
        # bound = -1
        # for y in y_idx:
        #     bound = np.searchsorted(x_idx, y, side='left')
        # if bound == 0:
        #     return x_idx[0]
        # elif bound == len(x_idx):
        #     return x_idx[len(x_idx) - 1]
        # else:
        #     return min(y - x_idx[bound - 1], x_idx[bound] - y)

    '''
    这道题用O(n)复杂度就可以解出来，是我弄复杂了
    '''
    def getDistance2(self, article, n, x, y):
        x_idx = -1
        y_idx = -1
        min_distance = float('inf')
        for idx in range(len(article)):
            if article[idx] == x:
                x_idx = idx
            elif article[idx] == y:
                y_idx = idx
            if x_idx != -1 and y_idx != -1:
                min_distance = min(min_distance, abs(x_idx - y_idx))
        return min_distance

        

if __name__ == '__main__':
    print(Distance().getDistance2(["lab","lab","nhb","nhb","lab","nhb","nhb","nhb","lab"], 9, 'nhb', 'lab'))