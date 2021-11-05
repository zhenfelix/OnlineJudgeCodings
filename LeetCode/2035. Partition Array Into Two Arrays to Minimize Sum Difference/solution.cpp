class Solution {
public:
    int minimumDifference(vector<int>& nums) {
        for (auto &num : nums)
            num *= 2;
        
        int n = nums.size() / 2;
        int sum = 0;
        for (int num : nums)
            sum += num;
        
        vector<unordered_set<int>> left(n + 1), right(n + 1);
        left[0].insert(0), right[0].insert(0);
        for (int i = 0; i < n; ++i) {
            for (int j = i; j >= 0; --j) {
                for (int val : left[j])
                    left[j + 1].insert(val + nums[i]);
            }
        }
        
        for (int i = n; i < n * 2; ++i) {
            for (int j = i - n; j >= 0; --j) {
                for (int val : right[j])
                    right[j + 1].insert(val + nums[i]);
            }
        }
        
        vector<vector<int>> ls(n + 1), rs(n + 1);
        for (int i = 0; i <= n; ++i) {
            ls[i] = vector<int>(left[i].begin(), left[i].end());
            rs[i] = vector<int>(right[i].begin(), right[i].end());
            sort(ls[i].begin(), ls[i].end());
            sort(rs[i].begin(), rs[i].end());
        }
        
        int target = sum / 2;
        int dist = INT_MAX;
        for (int i = 0; i <= n; ++i) {
            int llen = ls[i].size(), rlen = rs[n - i].size();
            int pl = 0, pr = rlen - 1;
            while (pl < llen && pr >= 0) {
                int curr = ls[i][pl] + rs[n - i][pr];
                dist = min(dist, abs(curr - target));
                if (curr < target)
                    pl++;
                else
                    pr--;
            }
        }
        
        return dist;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/2ELXyY/view/DxDKIC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。