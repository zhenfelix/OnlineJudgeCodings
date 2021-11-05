class MinStack {
public:
    vector<int> st, mst;
    MinStack() {
        st.clear();
        mst.clear();
    }
    
    void push(int val) {
        st.push_back(val);
        if (mst.empty() || mst.back() >= val)
            mst.push_back(val);
        else
            mst.push_back(mst.back());
    }
    
    void pop() {
        st.pop_back();
        mst.pop_back();
    }
    
    int top() {
        return st.back();
    }
    
    int getMin() {
        return mst.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


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