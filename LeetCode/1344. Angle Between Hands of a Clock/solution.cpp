class Solution {
public:
    double angleClock(int hour, int minutes) {
        int a = 720/12*hour+720/12/60*minutes%720;
        int b = 720/60*minutes%720;
        return (double)min((b-a+720)%720,(a-b+720)%720)/2;
    }
};