class Solution {
public:
    int minOperations(string s, int K) {
        int n = s.size();

        int dis[n + 1];
        memset(dis, -1, sizeof(dis));
        // 按奇偶性把所有节点加入有序集合
        set<int> st[2];
        for (int i = 0; i <= n; i++) st[i & 1].insert(i);

        // 计算当前字符串有几个 0，这是我们的出发节点
        int S = 0;
        for (char c : s) if (c == '0') S++;
        queue<int> q;
        q.push(S); dis[S] = 0; st[S & 1].erase(S);

        while (!q.empty()) {
            int sn = q.front(); q.pop();
            // 计算变化的范围
            // 最多选 min(K, sn) 个 0，以及最多选 min(K, n - sn) 个 1
            int l = min(K, sn);
            l = (K - l) - l;
            int r = min(K, n - sn);
            r = r - (K - r);

            // 将指定范围里还未访问过的节点取出来，然后删除
            auto &tmp = st[(sn + l) & 1];
            auto it = tmp.lower_bound(sn + l);
            while (it != tmp.end()) {
                if (*it > sn + r) break;
                q.push(*it);
                dis[*it] = dis[sn] + 1;
                tmp.erase(it++);
            }
        }

        return dis[0];
    }
};