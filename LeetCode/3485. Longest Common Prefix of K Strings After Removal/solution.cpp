class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words, int K) {
        // 字典树的节点
        struct Node {
            // cnt：子树里有几个代表字符串结束的点
            // dep：该节点的深度
            int cnt, dep;
            // ch[c]：下一个字符是 c 会走到哪个节点
            array<int, 26> ch;

            // 初始化一个深度为 d 的节点
            Node(int d) {
                cnt = 0;
                dep = d;
                for (int i = 0; i < 26; i++) ch[i] = -1;
            }
        };
        vector<Node> trie;

        auto newNode = [&](int d) {
            int idx = trie.size();
            Node node(d);
            trie.push_back(node);
            return idx;
        };
        newNode(0);

        // 把字符串 s 加入字典树
        auto add = [&](string &s) {
            int now = 0;
            for (char c : s) {
                trie[now].cnt++;
                int nxt = trie[now].ch[c - 'a'];
                if (nxt < 0) nxt = newNode(trie[now].dep + 1);
                now = trie[now].ch[c - 'a'] = nxt;
            }
            trie[now].cnt++;
        };
        for (auto &s : words) add(s);

        typedef pair<int, int> pii;
        // 把所有子树里至少有 k 个字符串结束点的节点加入 set
        set<pii> st;
        for (int i = 0; i < trie.size(); i++) if (trie[i].cnt >= K) st.insert({trie[i].dep, i});

        // 计算如果删了字符串 s，答案是多少
        auto calc = [&](string &s) {
            int ret = 0, now = 0;
            for (char c : s) {
                // 把路径上的点从 set 里删掉
                if (trie[now].cnt >= K) st.erase({trie[now].dep, now});
                // 路径上的点单独计算答案，此时子树里的要求变成 k + 1
                if (trie[now].cnt > K) ret = max(ret, trie[now].dep);
                now = trie[now].ch[c - 'a'];
            }
            if (trie[now].cnt >= K) st.erase({trie[now].dep, now});
            if (trie[now].cnt > K) ret = max(ret, trie[now].dep);
            // 再和 set 里其它未被影响的点做比较
            if (!st.empty()) ret = max(ret, prev(st.end())->first);

            // 把路径上的点再加回 set 里
            now = 0;
            for (char c : s) {
                if (trie[now].cnt >= K) st.insert({trie[now].dep, now});
                now = trie[now].ch[c - 'a'];
            }
            if (trie[now].cnt >= K) st.insert({trie[now].dep, now});
            return ret;
        };
        vector<int> ans;
        for (auto &s : words) ans.push_back(calc(s));
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/longest-common-prefix-of-k-strings-after-removal/solutions/3613633/zi-dian-shu-by-tsreaper-wdv9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。