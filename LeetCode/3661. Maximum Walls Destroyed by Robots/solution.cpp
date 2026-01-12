class Solution {
public:
    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        int n = robots.size(), m = walls.size();
        sort(walls.begin(), walls.end());

        // 机器人从左到右排序
        const int INF = 2e9;
        typedef pair<int, int> pii;
        vector<pii> vec;
        for (int i = 0; i < n; i++) vec.push_back({robots[i], distance[i]});
        // 左右加入两个哨兵节点，以免处理边界
        vec.push_back({-INF, 0});
        vec.push_back({INF, 0});
        sort(vec.begin(), vec.end());

        // 二分求区间 [l, r] 里有多少墙壁
        auto gao = [&](int l, int r) -> int {
            if (l > r) return 0;
            return upper_bound(walls.begin(), walls.end(), r) - lower_bound(walls.begin(), walls.end(), l);
        };

        int f[n + 1][2], g[n + 1];
        f[0][0] = f[0][1] = g[0] = 0;
        for (int i = 1; i <= n; i++) {
            // t：往左射最多摧毁多少墙壁
            int t = gao(max(vec[i - 1].first + 1, vec[i].first - vec[i].second), vec[i].first - 1);
            f[i][0] = f[i - 1][0] + t;
            // tot：当前机器人和上一个机器人之间一共有多少墙壁
            int tot = gao(vec[i - 1].first + 1, vec[i].first - 1);
            f[i][0] = max(f[i][0], f[i - 1][1] - g[i - 1] + min(tot, g[i - 1] + t));

            // g[i]：往右射最多摧毁多少墙壁
            g[i] = gao(vec[i].first + 1, min(vec[i + 1].first - 1, vec[i].first + vec[i].second));
            f[i][1] = max(f[i - 1][0], f[i - 1][1]) + g[i];
        }

        int ans = max(f[n][0], f[n][1]);
        // 还要加上和机器人重叠的墙壁数，这些墙壁总会被摧毁
        for (int i = 1; i <= n; i++) ans += gao(vec[i].first, vec[i].first);
        return ans;
    }
};