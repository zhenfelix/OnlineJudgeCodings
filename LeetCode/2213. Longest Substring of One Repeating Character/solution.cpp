class Solution {
    typedef pair<int, int> pii;
    multiset<int> lens;
    set<pii> st[26];

    // 加入 c 的连续字符串 [L, R)
    set<pii>::iterator add(int c, int L, int R) {
        lens.insert(R - L);
        return st[c].insert(pii(L, R)).first;
    }

    // 删除 c 的连续字符串 [L, R)
    void del(int c, int L, int R) {
        lens.erase(lens.find(R - L));
        st[c].erase(st[c].find(pii(L, R)));
    }

    // 从 idx 处拆除字符 c 的连续字符串
    void brk(int c, int idx) {
        // 找到包含 idx 的区间
        auto it = prev(st[c].lower_bound(pii(idx + 1, idx)));
        int L = it->first, R = it->second;
        // 拆成两个区间
        del(c, L, R);
        if (L < idx) add(c, L, idx);
        if (idx + 1 < R) add(c, idx + 1, R);
    }

    // 合并两个区间（若它们连续）
    void merge(int c, set<pii>::iterator it0, set<pii>::iterator it1, set<pii>::iterator &output) {
        int L0 = it0->first, R0 = it0->second, L1 = it1->first, R1 = it1->second;
        if (R0 == L1) del(c, L0, R0), del(c, L1, R1), output = add(c, L0, R1);
    }

    // 在 idx 处插入字符 c
    void ins(int c, int idx) {
        auto it = add(c, idx, idx + 1);
        // 尝试和左边的区间合并
        if (it != st[c].begin()) merge(c, prev(it), it, it);
        // 尝试和右边的区间合并
        if (next(it) != st[c].end()) merge(c, it, next(it), it);
    }

public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        int n = s.size(), Q = queryCharacters.size();
        vector<int> ans;
        // 加入原字符串中所有字符
        for (int i = 0; i < n; i++) ins(s[i] - 'a', i);
        for (int q = 0; q < Q; q++) {
            int idx = queryIndices[q];
            char c = queryCharacters[q];
            // 不改变原字符串，跳过
            if (s[idx] == c) { ans.push_back(*lens.rbegin()); continue; }
            // 破坏该位置原本的连续字符串
            brk(s[idx] - 'a', idx);
            // 插入新字符
            ins(c - 'a', idx);
            // 统计答案
            s[idx] = c;
            ans.push_back(*lens.rbegin());
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode-cn.com/circle/discuss/P2iS4B/view/RMKHxb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。