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