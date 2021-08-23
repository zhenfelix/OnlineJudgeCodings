class Solution {
public:
    vector<int> recoverArray(int n, vector<int>& sums) {
        int BIAS = 0;
        for (int x : sums) BIAS = min(BIAS, x);
        BIAS = -BIAS;

        multiset<int> st;
        for (int x : sums) st.insert(x + BIAS);

        st.erase(st.begin());
        vector<int> ans;
        ans.push_back(*st.begin());

        for (int i = 1; i < n; i++) {
            for (int msk = 0; msk < (1 << i); msk++) if (msk >> (i - 1) & 1) {
                int sm = 0;
                for (int j = 0; j < i; j++) if (msk >> j & 1) sm += ans[j];
                st.erase(st.find(sm));
            }
            ans.push_back(*st.begin());
        }

        for (int i = 0; i < (1 << n); i++) {
            int sm = 0;
            for (int j = 0; j < n; j++) if (i >> j & 1) sm += ans[j];
            if (sm == BIAS) {
                for (int j = 0; j < n; j++) if (i >> j & 1) ans[j] = -ans[j];
                break;
            }
        }
        return ans;
    }
};


// 作者：tsreaper
// 链接：https://leetcode-cn.com/problems/find-array-given-subset-sums/solution/ti-jie-cong-zi-ji-de-he-huan-yuan-shu-zu-q9qw/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。