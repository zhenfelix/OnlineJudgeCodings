class CountIntervals {
    typedef pair<int, int> pii;

    int ans = 0;
    set<pii> st;

public:
    CountIntervals() {
    }
    
    void add(int left, int right) {
        int L = left, R = right;
        // 这里 (R1, L1) >= (R2, L2)，若 R1 > R2 或 R1 = R2 且 L1 >= L2
        auto it = st.lower_bound(pii(left - 1, -2e9));
        while (it != st.end()) {
            if (it->second > right + 1) break;
            L = min(L, it->second);
            R = max(R, it->first);
            ans -= it->first - it->second + 1;
            st.erase(it++);
        }
        ans += R - L + 1;
        st.insert(pii(R, L));
    }
    
    int count() {
        return ans;
    }
};

// 作者：tsreaper
// 链接：https://leetcode.cn/problems/count-integers-in-intervals/solution/by-tsreaper-fc7p/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class CountIntervals {
public:
    map<int, int> m;
    int cnt = 0;
    void add(int left, int right) {
        auto it = m.upper_bound(left);
        if (it != begin(m) && prev(it)->second >= left)
            it = prev(it);
        for (; it != end(m) && it->first <= right; m.erase(it++)) {
            left = min(left, it->first);
            right = max(right, it->second);
            cnt -= it->second - it->first + 1;
        }
        cnt += right - left + 1;
        m[left] = right;
    }
    int count() { return cnt; }
};


class CountIntervals {
    set<pair<int, int>> st;
    int cnt;
public:
    CountIntervals() {
        cnt = 0;
    }
    
    void add(int left, int right) {
        auto it = st.upper_bound({left, INT_MIN});
        
        if(it != st.begin() && (--it)->second < left) {
            ++it;
        }
        
        while(it != st.end() && it->first <= right) {
            left = min(left, it->first);
            right = max(right, it->second);
            
            cnt -= (it->second - it->first + 1);
            it = st.erase(it);
        }
        
        st.insert({ left, right });
        cnt += (right - left + 1);
    }
    
    int count() {
        return cnt;
    }
};










class CountIntervals {
    int cnt;
    map<int,int> mp;
    map<int,int>::iterator it;
    bool flag;
public:
    CountIntervals(): cnt(0) {

    }
    
    void add(int left, int right) {
        // cout << left << " " << right << endl;
        cnt += right-left+1;
        
        if (mp.find(left) != mp.end()){
            it = mp.find(left);
            if (right <= mp[left]){
                cnt -= (right-left+1);
                return;
            }
            cnt -= (mp[left]-left+1);
            mp[left] = right;
        }
        else{
            auto tmp = mp.insert(pair<int,int>(left,right));
            it = tmp.first;
            // cout << it->first << " " << it->second << endl;
            if (it != mp.begin()){
                auto p = prev(it);
                auto [lo,hi] = *p;
                if (hi >= left){
                    if (hi > right){
                        cnt += hi-right;
                        right = hi;
                        mp[left] = right;
                    }
                    cnt -= (hi-left+1);
                    mp[lo] = left-1;
                }
            }
        }
        // for (auto p = mp.begin(); p != mp.end(); p++){
        //     cout << p->first << " " << p->second << "; ";
        // }
        // cout << cnt << endl;
        for (auto p = next(it); p != mp.end();){
            auto [lo,hi] = *p;
            if (lo > right)
                break;
            cnt -= (min(hi,right)-lo+1);
            if (hi > right){
                right = hi;
                mp[left] = right;
            }
            mp.erase(p++);
        }
        
        // for (auto p = mp.begin(); p != mp.end(); p++){
        //     cout << p->first << " " << p->second << "; ";
        // }
        // cout << cnt << endl;
    }
    
    int count() {
        return cnt;
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */



class CountIntervals {
public:
    set<int> st;
    unordered_map<int,int> mp;
    int cnt;
    CountIntervals() {
        cnt = 0;
    }
    
    void add(int left, int right) {
         // cout << left << " " << right << endl;
        auto [it, flag] = st.insert(left);
        
        if (flag) cnt += right-left+1;
        else cnt += max(0,right-mp[*it]);
        mp[*it] = max(mp[*it], right);
        if (it != st.begin()){
            it--;
            if (mp[*it] >= left){
                // cnt -= (min(mp[*it], right)-left+1);
                right = mp[*it];
                left = *it;
            }
            else{
                it++;
            }
        }
        it++;
        // cout << *it << "cnt " << cnt << left << right << endl;
        for (;it != st.end() && *it <= right;){
            cnt -= (min(mp[*it], right)-(*it)+1);
            right = max(right, mp[*it]);
            mp[left] = right;
            mp.erase(*it);
            st.erase(it++);
        }
        // cout << left << " " << right << " " << cnt << endl;
    }
    
    int count() {
        return cnt;
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */
