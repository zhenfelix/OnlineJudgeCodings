class MyCalendarThree {
public:
    map<int,int> diff;
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        diff[start]++;
        diff[end]--;
        int res = 0;
        int cur = 0;
        for (auto [k,v] : diff){
            cur += v;
            res = max(res,cur);
        }
        return res;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */