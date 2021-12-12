class SORTracker {
public:
    bool first;
    set<pair<int,string>> st;
    set<pair<int,string>>::iterator cur;
    SORTracker() {
        first = true;
    }
    
    void add(string name, int score) {
        st.insert({-score,name});
        if (!first && (score > -cur->first || (score == -cur->first && name < cur->second))){
            cur = prev(cur);
        }
    }
    
    string get() {
        if (first){
            first = false;
            cur = st.begin();
        }
        else{
            cur = next(cur);
        }
        return cur->second;
    }
};

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker* obj = new SORTracker();
 * obj->add(name,score);
 * string param_2 = obj->get();
 */

class SORTracker {
    set<pair<int, string>> s;
    set<pair<int, string>>::iterator cur;

public:
    SORTracker() {
        s.emplace(0, ""); // 哨兵
        cur = s.begin();
    }

    void add(string name, int score) {
        pair<int, string> p = {-score, name};
        s.insert(p);
        if (p < *cur) --cur;
    }

    string get() {
        return cur++->second;
    }
};


// 作者：endlesscheng
// 链接：https://leetcode-cn.com/problems/sequentially-ordinal-rank-tracker/solution/qiao-miao-li-yong-cha-xun-de-te-shu-xing-7eyg/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。