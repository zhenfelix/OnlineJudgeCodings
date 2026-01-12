class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), B = sqrt(n);

        // 求乘法逆元
        const int MOD = 1e9 + 7;
        auto inv = [&](long long a) {
            long long b = MOD - 2, y = 1;
            for (; b; b >>= 1) {
                if (b & 1) y = (y * a) % MOD;
                a = a * a % MOD;
            }
            return y;
        };

        long long A[n];
        for (int i = 0; i < n; i++) A[i] = nums[i];
        typedef pair<int, long long> pil;
        vector<pil> vec[B + 1][B + 1];
        for (auto &qry : queries) {
            int l = qry[0], r = qry[1], K = qry[2], v = qry[3];
            if (K <= B) {
                // 步长不超过根号，先把操作记下来
                // 差分思想：记录操作开始的位置以及原运算，再记录操作结束的位置以及逆运算
                vec[K][l % K].push_back({l, v});
                vec[K][l % K].push_back({r + 1, inv(v)});
            } else {
                // 步长超过根号，暴力处理
                for (int i = l; i <= r; i += K) A[i] = A[i] * v % MOD;
            }
        }

        // 枚举每一类操作
        for (int k = 1; k <= B; k++) for (int m = 0; m < k; m++) {
            // 把操作按下标从左到右排序
            sort(vec[k][m].begin(), vec[k][m].end());
            // 扫描线维护当前乘积
            long long now = 1;
            // 枚举这一类里的所有下标
            for (int i = m, j = 0; i < n; i += k) {
                // 用扫描线进行需要的操作
                while (j < vec[k][m].size() && vec[k][m][j].first <= i) {
                    now = now * vec[k][m][j].second % MOD;
                    j++;
                }
                A[i] = A[i] * now % MOD;
            }
        }

        long long ans = 0;
        for (int i = 0; i < n; i++) ans ^= A[i];
        return ans;
    }
};