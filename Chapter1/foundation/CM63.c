// 给定int a和intb，在不使用if-else等比较和判断运算符的情况下返回较大的那个数。若两数相同则返回任意一个。

// 测试样例：
// 1，2
// 返回：2

class Max {
public:
    int getMax(int a, int b) {
        // write code here
        // 判断a, b的相减结果
        int result = a - b;
        // result为负数(a < b，返回b)，这一行的结果为1；result为正数(a > b，返回a)，这一行的结果为0
        result = (result >> 31) & 1;
        return (1 - result) * a + result * b;
    }

    int getMax_v2(int a, int b){
        b = a - b;
        a -= b & (b >> 31);
        return a;
    }
};