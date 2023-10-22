// 给定int a和intb，在不使用if-else等比较和判断运算符的情况下返回较大的那个数。若两数相同则返回任意一个。

// 测试样例：
// 1，2
// 返回：2

import java.util.*;

public class Max {
    public int getMax(int a, int b) {
        // write code here
        // 定义result放置a和b的结果
        int result = a - b;
        // 对result进行位运算，判断其正负。如果result为负数(a < b)，则result最终=1；如果result为正数(a > b)，则result最终=0
        result = (result>>31) & 1;
        return (1 - result) * a + result * b;
    }

    public int getMax_v2(int a, int b) {
        b = a - b;
        a -= b & (b >> 31);
        return a;
    }
}