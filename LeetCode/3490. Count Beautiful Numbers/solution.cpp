unordered_map<long long, int> f;

class Solution {
public:
    int beautifulNumbers(int l, int r) {
        // 把状态映射到一个整数，方便用哈希表保存
        auto calcMsk = [&](int pos, int prod, int sm) {
            long long ret = pos;
            ret = ret * ((long long) 1e9) + prod;
            ret = ret * 100 + sm;
            return ret;
        };

        vector<int> A;
        // 数位 DP
        auto dp = [&](this auto &&dp, int pos, int prod, int sm, bool full) {
            if (pos < 0) {
                if (sm == 0) return 0;
                return prod % sm == 0 ? 1 : 0;
            }
            long long msk = calcMsk(pos, prod, sm);
            if (!full && f.count(msk)) return f[msk];
            int ret = 0;

            int R = (full ? A[pos] : 9);
            for (int i = 0; i <= R; i++) {
                int nxtProd = prod * i;
                // sm == 0 且 i == 0，说明还在前导零，因此乘积先不改变
                if (sm == 0 && i == 0) nxtProd = prod;
                ret += dp(pos - 1, nxtProd, sm + i, full && i == R);
            }
            if (!full) f[msk] = ret;
            return ret;
        };

        auto gao = [&](int x) {
            if (x == 0) return 0;
            A.clear();
            for (; x; x /= 10) A.push_back(x % 10);
            return dp(A.size() - 1, 1, 0, true);
        };
        return gao(r) - gao(l - 1);
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/count-beautiful-numbers/solutions/3613934/shu-wei-dp-by-tsreaper-4nl8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。