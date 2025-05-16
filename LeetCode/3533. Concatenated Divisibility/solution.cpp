class Solution {
public:
    vector<int> concatenatedDivisibility(vector<int>& nums, int K) {
        int n = nums.size();
        // 给 nums 排序，方便我们枚举到最小的可行转移就退出
        sort(nums.begin(), nums.end());

        // 计算 x 十进制表示的长度
        auto calc = [&](int x) {
            int ret = 0;
            for (; x; x /= 10) ret++;
            return ret;
        };

        // len[msk]：msk 表示的数的总长
        int len[1 << n];
        for (int i = 0; i < (1 << n); i++) {
            len[i] = 0;
            for (int j = 0; j < n; j++) if (i >> j & 1) len[i] += calc(nums[j]);
        }
        int mx = len[(1 << n) - 1];

        // P[i]：10 ** i 的值
        long long P[mx + 1];
        P[0] = 1;
        for (int i = 1; i <= mx; i++) P[i] = P[i - 1] * 10 % K;

        typedef pair<int, int> pii;
        // from 数组记录一下当前状态是由哪个状态转移来的，方便最后构造方案
        pii from[1 << n][K];
        for (int i = 0; i < (1 << n); i++) for (int k = 0; k < K; k++) from[i][k] = {-1, -1};
        from[0][0] = {0, 0};
        for (int i = 1; i < (1 << n); i++) for (int k = 0; k < K; k++) {
            for (int j = 0; j < n; j++) if (i >> j & 1) {
                int ii = i ^ (1 << j);
                // 假设 f[ii][kk] 可以转移给 f[i][k]，则转移后取模的值就是
                // k == ((10 ** len[ii]) * nums[j] + kk) % K
                // 移项就能算出 kk 的值
                int kk = P[len[ii]] * nums[j] % K;
                kk = (k - kk + K) % K;
                // 找到第一个可行的转移就退出
                if (from[ii][kk].first >= 0) { from[i][k] = {j, kk}; break; }
            }
        }

        if (from[(1 << n) - 1][0].first < 0) return {};
        // 构造答案
        vector<int> ans;
        for (int i = (1 << n) - 1, k = 0; i > 0; ) {
            pii p = from[i][k];
            ans.push_back(nums[p.first]);
            i = i ^ (1 << p.first);
            k = p.second;
        }
        return ans;
    }
};