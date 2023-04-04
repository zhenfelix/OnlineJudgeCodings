class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {
        int inf = 0x3f3f3f3f;
        int n = postorder.size();
        vector<int> st, lc(n,-1);
        for (int i = 0; i < n; i++){
            while(!st.empty() && postorder[st.back()] > postorder[i]) st.pop_back();
            if (!st.empty()) lc[i] = st.back();
            st.push_back(i);
        }
        function<bool(int,int,int,int)> dfs = [&](int l, int r, int lo, int hi) -> bool{
            if (l > r) return true;
            if (postorder[r] <= lo || postorder[r] >= hi) return false;
            return dfs(l,lc[r],lo,postorder[r]) && dfs(lc[r]+1,r-1,postorder[r],hi);
        };
        return dfs(0,n-1,-inf,inf);

    }
};