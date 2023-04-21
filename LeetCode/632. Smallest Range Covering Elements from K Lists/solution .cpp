class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<int> ans {(int)(-1e5),(int)(1e5)};
        set<tuple<int,int,int>> q;
        int k = nums.size();
        for (int i = 0; i < k; i++) q.insert({nums[i][0],i,0});
        while (q.size() == k) {
            auto [lo,i,j] = *q.begin();
            auto [hi,ii,jj] = *q.rbegin();
            if (hi-lo < ans[1]-ans[0]) ans = {lo,hi};
            q.erase(q.begin());
            if (j+1 < nums[i].size()) q.insert({nums[i][j+1],i,j+1});
        }
        return ans;
    }
};