class Solution {
    vector<int> L, R, V;
    string S;
    void update(int idx, int pos, int lo, int hi, char ch){
        if (lo >= hi){
            S[pos] = ch;
            return;
        }
        if (lo <= pos && pos <= hi){
            int mid = (lo+hi)/2;
            update(idx*2+1, pos, lo, mid, ch);
            update(idx*2+2, pos, mid+1, hi, ch);
            V[idx] = max(V[idx*2+1], V[idx*2+2]);
            if (S[mid] == S[mid+1])
                V[idx] = max(V[idx], R[idx*2+1]+L[idx*2+2]);
            L[idx] = L[idx*2+1];
            if (L[idx] == mid-lo+1 && S[mid] == S[mid+1])
                L[idx] += L[idx*2+2];
            R[idx] = R[idx*2+2];
            if (R[idx] == hi-mid && S[mid] == S[mid+1])
                R[idx] += R[idx*2+1];
        }
        return;
    }
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        int n = s.length();
        L.assign(n*4, 1);
        R.assign(n*4, 1);
        V.assign(n*4, 1);
        S = s;
        vector<int> ans;
        for (int i = 0; i < n; i++){
            update(0, i, 0, n-1, s[i]);
        }
        int K = queryIndices.size();
        for (int k = 0; k < K; k++){
            update(0, queryIndices[k], 0, n-1, queryCharacters[k]);
            ans.push_back(V[0]);
        }
        return ans;
    }
};




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



class Solution {
    using PII = pair<int, int>;
public:
    vector<int> longestRepeating(string s, string s2, vector<int>& q) {
        vector<PII> idx;
        int n = int(s.size()), k = int(s2.size());
        for (int i = 0; i < n; ++i) {
            if (idx.empty() || s[idx.back().first] != s[i]) {
                idx.emplace_back(i, 1);
            } else {
                idx.back().second ++;
            }
        }
        map<int, int> seg;
        multiset<int> st;
        for (auto &[x, y]: idx) seg[x] = y, st.emplace(y);
        auto Cut = [&](int i) -> void {
            if (i < 0 || i >= n) return;
            if (!seg.count(i)) {
                auto it = prev(seg.lower_bound(i));
                auto [x, y] = *it;
                st.extract(y);
                seg[x] = i - x;
                seg[i] = y - (i - x);
                st.emplace(i - x);
                st.emplace(y - (i - x));
            }
        };

        auto Union = [&](int j) -> void {
            if (j <= 0 || j >= n) return;
            auto it = seg.lower_bound(j);
            int i = prev(it)->first;
            if (s[i] == s[j]) {
                st.extract(seg[i]);
                st.extract(seg[j]);
                st.emplace(seg[i] + seg[j]);
                seg[i] += seg[j];
                seg.erase(j);
            }
        };

        vector<int> ans(k);
        for (int i = 0; i < k; ++i) {
            char a = s2[i];
            int j = q[i];
            if (s[j] == a) {
                ans[i] = *st.rbegin();
                continue;
            }
            s[j] = a;
            Cut(j), Cut(j + 1);
            Union(j), Union(j + 1);
            ans[i] = *st.rbegin();
        }
        return ans;
    }
};


// 作者：megurine
// 链接：https://leetcode.cn/problems/longest-substring-of-one-repeating-character/solution/ke-duo-li-shu-by-megurine-4erh/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。