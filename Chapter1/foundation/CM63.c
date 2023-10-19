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