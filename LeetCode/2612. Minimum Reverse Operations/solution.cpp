class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int> &banned, int k) {
        unordered_set<int> ban{banned.begin(), banned.end()};
        set<int> sets[2];
        for (int i = 0; i < n; ++i)
            if (i != p && !ban.count(i))
                sets[i % 2].insert(i);
        sets[0].insert(n);
        sets[1].insert(n); // 哨兵

        vector<int> ans(n, -1);
        vector<int> q = {p};
        for (int step = 0; !q.empty(); ++step) {
            vector<int> nq;
            for (int i: q) {
                ans[i] = step;
                // 从 mn 到 mx 的所有位置都可以翻转到
                int mn = max(i + k - (i * 2 + 1), i - k + 1);
                int mx = min(i - k + ((n - 1 - i) * 2 + 1), i + k - 1);
                auto &s = sets[mn % 2];
                for (auto it = s.lower_bound(mn); *it <= mx; it = s.erase(it))
                    nq.push_back(*it);
            }
            q = move(nq);
        }
        return ans;
    }
};


// 作者：endlesscheng
// 链接：https://leetcode.cn/problems/minimum-reverse-operations/solution/liang-chong-zuo-fa-ping-heng-shu-bing-ch-vr0z/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



using pii = pair<int,int>;
class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        vector<bool> available(n+1,true);
        available[p] = false;
        available[n] = false;
        for (auto &b : banned) available[b] = false;
        vector<map<int,int>> tree(2);
        int j = -1;
        for (int i = 0; i < n; i++){
            if (!available[i]) {
                j = -1;
                continue;
            }
            if (j == -1) j = i;
            if (available[i] != available[i+1]){
                tree[0][i] = j;
                tree[1][i] = j;
            }
        }
        vector<int> dist(n,-1);
        dist[p] = 0;
        queue<int> q;
        q.push(p);
        while (!q.empty()){
            int cur = q.front();
            q.pop();
            int l = max(k-1-cur,cur-k+1);
            int r = min(2*n-1-k-cur,cur+k-1);
            int nxt = l;
            vector<pii> candidates;
            int flag = nxt&1;
            auto it = tree[flag].lower_bound(l);
            for (;it != tree[flag].end();it = tree[flag].erase(it)){
                auto [hi,lo] = *it;
                if (lo > r) break;
                if (lo < l) candidates.push_back({lo,l-1});
                if (hi > r) candidates.push_back({r+1,hi});
                nxt = max(nxt,lo);
                if ((nxt&1) != (l&1)) nxt++;
                while (nxt <= r && nxt <= hi){
                    q.push(nxt);
                    dist[nxt] = dist[cur]+1;
                    nxt += 2;
                }
            }
            for (auto [lo,hi] : candidates){
                if (lo <= hi) tree[flag].insert({hi,lo});
            }
        }
        return dist;
    }
};