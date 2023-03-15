# lcp32

class Solution {

public:

    int findMinimumTime(vector<vector<int>>& tasks) {

        int mx = 0;

        for (auto &vec : tasks) mx = max(mx, vec[1]);



        vector<int> e[mx + 2], v[mx + 2];

        // 第一个不等式

        for (int i = 1; i <= mx; i++) {

            e[i].push_back(i - 1);

            v[i].push_back(0);

        }

        // 第二个不等式

        for (int i = 0; i < mx; i++) {

            e[i].push_back(i + 1);

            v[i].push_back(1);

        }

        // 第三个不等式

        for (auto &vec : tasks) {

            e[vec[1]].push_back(vec[0] - 1);

            v[vec[1]].push_back(-vec[2]);

        }



        // 差分约束要建立超级源点

        int S = mx + 1;

        for (int i = 0; i <= mx; i++) {

            e[S].push_back(i);

            v[S].push_back(0);

        }



        // SPFA

        const int INF = 1e9;

        queue<int> q;

        int dis[mx + 2];

        for (int i = 0; i <= mx + 1; i++) dis[i] = INF;

        bool vis[mx + 2];

        memset(vis, 0, sizeof(vis));



        q.push(S); dis[S] = 0; vis[S] = true;

        while (!q.empty()) {

            int sn = q.front(); q.pop();

            vis[sn] = false;

            for (int i = 0; i < e[sn].size(); i++) {

                int fn = e[sn][i], val = v[sn][i];

                if (dis[fn] <= dis[sn] + val) continue;

                dis[fn] = dis[sn] + val;

                if (vis[fn]) continue;

                q.push(fn); vis[fn] = true;

            }

        }



        return dis[mx] - dis[0];

    }

};

// 作者：TsReaper
// 链接：https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/solutions/2163154/chai-fen-yue-shu-by-tsreaper-swhm/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。