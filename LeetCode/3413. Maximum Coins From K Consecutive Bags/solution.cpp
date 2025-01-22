class Solution {
public:
    long long maximumCoins(vector<vector<int>>& vec, int K) {
        int n = vec.size();
        long long ans = 0;
        // 防止溢出，改为用 long long 保存区间
        vector<array<long long, 3>> coins;
        for (auto &coin : vec) coins.push_back({coin[0], coin[1], coin[2]});
        
        // 计算区间 i 里一共有多少硬币
        auto calc = [&](int i) {
            return coins[i][2] * (coins[i][1] - coins[i][0] + 1);
        };
        
        auto gao = [&]() {
            sort(coins.begin(), coins.end());
            long long now = 0;
            // i：当前窗口的开头位于哪个区间的左端点
            // j：与当前窗口不相交的第一个区间在哪
            for (int i = 0, j = 0; i < n; i++) {
                // 双指针找到第一个不相交的区间
                while (j < n && coins[j][0] < coins[i][0] + K) {
                    now += calc(j);
                    j++;
                }
                // 注意窗口可能没有完全包含区间 j - 1，因此需要扣除未包含的部分
                long long det = max(0LL, coins[j - 1][1] - (coins[i][0] + K) + 1);
                ans = max(ans, now - det * coins[j - 1][2]);
                now -= calc(i);
            }
        };

        // 计算窗口开头与每个区间左端点重合时的情况
        gao();
        // 把所有区间“倒过来”，就能用相同的代码处理窗口结尾与每个区间右端点重合时的情况
        for (auto &coin : coins) {
            long long l = 1e9 - coin[1], r = 1e9 - coin[0];
            coin[0] = l; coin[1] = r;
        }
        gao();
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/maximum-coins-from-k-consecutive-bags/solutions/3039089/tan-xin-shuang-zhi-zhen-by-tsreaper-odxk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。