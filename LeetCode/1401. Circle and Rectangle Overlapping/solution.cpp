class Solution {
public:
    int dis2(int x1, int y1, int x2, int y2){
        return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
    }
    bool checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2) {
        if (x1 > x_center+radius || x2 < x_center-radius || y1 > y_center+radius || y2 < y_center-radius)
            return false;
        int r2 = radius*radius;
        if (x1 > x_center && y1 > y_center && dis2(x_center,y_center,x1,y1) > r2)
            return false;
        if (x1 > x_center && y2 < y_center && dis2(x_center,y_center,x1,y2) > r2)
            return false;
        if (x2 < x_center && y1 > y_center && dis2(x_center,y_center,x2,y1) > r2)
            return false;
        if (x2 < x_center && y2 < y_center && dis2(x_center,y_center,x2,y2) > r2)
            return false;
        return true;
    }
};