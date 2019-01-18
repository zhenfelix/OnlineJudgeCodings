class MinStack {
public:
    vector<int> s;
    vector<int> smin;
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        s.push_back(x);
        if(smin.size()==0||x<smin.back())smin.push_back(x);
        else smin.push_back(smin.back());
    }
    
    void pop() {
        s.pop_back();
        smin.pop_back();
    }
    
    int top() {
        return s.back();
    }
    
    int getMin() {
        return smin.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */