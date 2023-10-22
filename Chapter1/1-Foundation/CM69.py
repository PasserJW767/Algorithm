# 给定一个string数组article及其大小n及一个待统计单词word，请返回该单词在数组中出现的频数。文章的词数在1000以内。

# -*- coding:utf-8 -*-

class Frequency:
    def getFrequency(self, article, n, word):
        # write code here
        sumword = 0
        for w in article:
            if w == word:
                sumword += 1
        return sumword

if __name__ == '__main__':
    Frequency().getFrequency(["a","b","a","ab","abc"], 5, "a")