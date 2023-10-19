import java.util.*;

public class CrossLine {
    public boolean checkCrossLine(double s1, double s2, double y1, double y2) {
        // write code here
        // if (s1 == s2) {
        //     if (y1 == y2) {
        //         return true;
        //     }
        //     return false;
        // }
        // return true;
        double epson = 1e-10;
        if(Math.abs(s1-s2) < epson && Math.abs(y1-y2) < epson)
            return true;
        if(Math.abs(s1-s2) > epson)
            return true;
        return false;
    }
}