class Solution {
public:
    vector<int> subarrayMajority(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), q = queries.size();
        typedef pair<int, int> pii;

        // 离散化
        map<int, int> mp;
        for (int x : nums) mp[x] = 1;
        int m = 0;
        for (auto &p : mp) p.second = m++;
        for (int &x : nums) x = mp[x];
        int who[m];
        for (auto &p : mp) who[p.second] = p.first;

        // 记录每种元素出现的所有下标
        vector<int> pos[m];
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);
        // 二分求区间 [l, r] 里，元素 x 出现了几次
        auto calc = [&](int x, int l, int r) {
            return upper_bound(pos[x].begin(), pos[x].end(), r) - lower_bound(pos[x].begin(), pos[x].end(), l);
        };

        // 块大小
        int BLK = n * n / (q * max(1, __lg(n)));
        BLK = sqrt(max(1, BLK));

        // 暴力枚举，预处理 f[i][j] 表示第 i 个块到第 j 个块的最小众数
        pii f[(n - 1) / BLK + 1][(n - 1) / BLK + 1];
        int freq[m];
        for (int i = 0; i < n; i += BLK) {
            memset(freq, 0, sizeof(freq));
            pii p = {0, 0};
            for (int j = i; j < n; j++) {
                int t = ++freq[nums[j]];
                p = max(p, pii(t, -nums[j]));
                if (j % BLK == BLK - 1 || j + 1 == n) f[i / BLK][j / BLK] = p;
            }
        }

        vector<int> ans;
        for (auto &qry : queries) {
            int l = qry[0], r = qry[1];
            int bl = l / BLK, br = r / BLK;
            // 可能性 1：答案就是中间完整的块的最小众数
            pii p = {0, 0};
            if (bl + 1 <= br - 1) p = f[bl + 1][br - 1];
            // 可能性 2：答案是左边不完整的块里的某个元素
            for (int i = l; i < BLK * (bl + 1) && i <= r; i++) {
                int t = calc(nums[i], l, r);
                p = max(p, pii(t, -nums[i]));
            }
            // 可能性 2：答案是右边不完整的块里的某个元素
            for (int i = r; i >= BLK * br && i >= l; i--) {
                int t = calc(nums[i], l, r);
                p = max(p, pii(t, -nums[i]));
            }
            if (p.first >= qry[2]) ans.push_back(who[-p.second]);
            else ans.push_back(-1);
        }
        return ans;
    }
};