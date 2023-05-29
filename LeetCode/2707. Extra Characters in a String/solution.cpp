class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        // 用 unordered_set 保存字典，方便快速查询
        unordered_set<string> st;
        for (auto &word : dictionary) st.insert(word);

        int n = s.size();
        const int INF = 1e9;
        int f[n + 1];
        for (int i = 1; i <= n; i++) f[i] = INF;
        f[0] = 0;

        // 套用 dp 方程
        for (int i = 1; i <= n; i++) {
            f[i] = f[i - 1] + 1;
            for (int j = 0; j < i; j++) {
                // 构造子串
                string t;
                for (int k = j; k < i; k++) t.push_back(s[k]);
                // 查询子串是否在字典里
                if (st.count(t)) f[i] = min(f[i], f[j]);
            }
        }
        return f[n];
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/fQ58lb/view/6vKWNF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。