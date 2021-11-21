class RangeFreqQuery {
    unordered_map<int, vector<int>> mp;
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < arr.size(); ++i) 
            mp[arr[i]].emplace_back(i);
    }
    
    int query(int left, int right, int value) {
        if (!mp.count(value))
            return 0;
        
        auto &v = mp[value];
        auto r = upper_bound(v.begin(), v.end(), right);
        auto l = lower_bound(v.begin(), v.end(), left);
        return r - l;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/sfeav2/view/eQBxyC/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。