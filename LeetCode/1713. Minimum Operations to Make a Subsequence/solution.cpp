class Solution {
public:
    int minOperations(vector<int> &target, vector<int> &arr) {
        int n = target.size();
        unordered_map<int, int> pos;
        for (int i = 0; i < n; ++i) {
            pos[target[i]] = i;
        }
        vector<int> d;
        for (int val : arr) {
            if (pos.count(val)) {
                int idx = pos[val];
                auto it = lower_bound(d.begin(), d.end(), idx);
                if (it != d.end()) {
                    *it = idx;
                } else {
                    d.push_back(idx);
                }
            }
        }
        return n - d.size();
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/solution/de-dao-zi-xu-lie-de-zui-shao-cao-zuo-ci-hefgl/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        int n = arr.size(), m = target.size();
        unordered_map<int,vector<int>> mp;
        for (int i = n-1; i >= 0; i--)
            mp[arr[i]].push_back(i);
        vector<int> lis;
        for (auto x : target){
            if (mp.find(x) == mp.end())
                continue;
            for (auto y : mp[x]){
                int idx = lower_bound(lis.begin(), lis.end(), y) - lis.begin();
                if (idx == lis.size())
                    lis.push_back(0);
                lis[idx] = y;
            }
            
        }
        return m-lis.size();
    }
};
