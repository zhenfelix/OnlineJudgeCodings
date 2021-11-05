class Solution {
public:
    int tot, m, n;
    unordered_map<int,int> mp;
    Solution(int m, int n) {
        tot = m*n;
        this->m = m;
        this->n = n;
        mp.clear();
    }
    
    vector<int> flip() {
        int r = rand()%tot;
        int t = mp.count(r) ? mp[r] : r;
        mp[r] = mp.count(tot-1) ? mp[tot-1] : tot-1;
        tot--;
        return {t/n,t%n};
    }
    
    void reset() {
        tot = m*n;
        mp.clear();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */