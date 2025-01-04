class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        // 将 y 坐标离散化，方便一会儿用树状数组
        int n = xCoord.size(), m = 0;
        map<int, int> mp;
        for (int y : yCoord) mp[y] = 1;
        for (auto &p : mp) p.second = ++m;

        // 把同一条竖线上的点放在一起
        typedef pair<int, int> pii;
        map<int, vector<pii>> vert;
        for (int i = 0; i < n; i++) vert[xCoord[i]].push_back({mp[yCoord[i]], i});
        for (auto &p : vert) sort(p.second.begin(), p.second.end());

        // 树状数组模板开始

        int tree[m + 1];
        memset(tree, 0, sizeof(tree));
        auto lb = [&](int x) { return x & (-x); };

        auto add = [&](int pos) {
            for (; pos <= m; pos += lb(pos)) tree[pos]++;
        };

        auto query = [&](int pos) {
            int ret = 0;
            for (; pos > 0; pos -= lb(pos)) ret += tree[pos];
            return ret;
        };

        // 树状数组模板结束

        long long ans = -1;
        unordered_map<long long, pii> last;
        // 从左到右枚举竖线
        for (auto &p : vert) {
            auto &vec = p.second;
            for (int i = 0; i < vec.size(); i++) {
                add(vec[i].first);
                if (i == 0) continue;

                // 判断之前是否出现过两个相邻的点对，它们的 y 坐标也是 ya 和 yb
                int ya = yCoord[vec[i - 1].second], yb = yCoord[vec[i].second];
                // c++ unordered_map 不支持用 pair 作为 key，我们只能把它变成一个 long long 当 key
                long long key = ya * ((long long) 1e9) + yb;
                // 假设现在的竖线是 x = t，这里用树状数组求满足 x <= t，且 ya <= y <= yb 的点有几个
                int cnt = query(vec[i].first) - query(vec[i - 1].first - 1);
                if (last.count(key)) {
                    // oldX：矩形左边界的 x 坐标
                    // oldCnt：满足 x <= oldX，且 ya <= y <= yb 的点有几个
                    auto &[oldCnt, oldX] = last[key];
                    // cnt - oldCnt 就是满足 oldX < x <= t 且 ya <= y <= yb 的点有几个
                    // 根据题意，这里要算出 2 才是合法的矩形，这个 2 就是矩形的右上和右下两个顶点
                    // 可是这里没判断左边界上有没有其它点？
                    // 其实不用判断，因为 last 里保存的都是竖线上相邻的点，所以左边界上肯定没有其它点
                    if (cnt - oldCnt == 2) ans = max(ans, 1LL * (p.first - oldX) * (yb - ya));
                }
                // 用现在这个新的点对覆盖之前旧的点对
                last[key] = {cnt, p.first};
            }
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/rbmRgF/view/geh29K/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。