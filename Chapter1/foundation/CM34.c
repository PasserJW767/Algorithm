// 现以斜率和截距的形式给出直角坐标系上的两条直线，即double s1，double s2，double y1，double y2，分别代表直线1和2的斜率(即s1,s2)和截距(即y1,y2)，请返回一个bool，判断这两条直线会不会相交（重合也算）。

// 测试样例：
// 3.14,3.14,1,2
// 返回：false


class CrossLine {
public:
    bool checkCrossLine(double s1, double s2, double y1, double y2) {
        // write code here
        // if(s1 == s2){
        //     if(y1 == y2){
        //         return true;
        //     }
        //     return false;
        // }
        // return true;
        double epson = 1e-10;
        if(abs(s1-s2) < epson && abs(y1-y2) < epson)
            return true;
        if(abs(s1-s2) > epson)
            return true;
        return false;
    }
};