class Solution {
public:
    int minGroupsForValidAssignment(vector<int>& nums) {
        int n = nums.size();
        // 统计每种数的出现次数
        unordered_map<int, int> mp;
        for (int x : nums) mp[x]++;

        // 计算 min(s)，并把每种数的出现次数提取出来
        int mn = n;
        vector<int> vec;
        for (auto &p : mp) vec.push_back(p.second), mn = min(mn, p.second);

        int ans = n;
        // 枚举组的最小大小
        for (int k = 1; k <= mn; k++) {
            int cnt = 0;
            // 对每种数单独计算分组情况
            for (auto s : vec) {
                // 如题解所述的分类讨论
                int d = s / (k + 1), r = s % (k + 1);
                if (r == 0) cnt += d;
                else if (d + r >= k) cnt += d + 1;
                else {
                    cnt = -1; break;
                }
            }
            if (cnt >= 0) ans = min(ans, cnt);
        }
        return ans;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/haZ1d7/view/dUbwkm/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。