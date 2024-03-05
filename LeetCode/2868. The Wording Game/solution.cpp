template<typename T>
auto autov(const T &v, int n) { return vector<T>(n,v);}

template<typename T, typename ...D>
auto autov(const T &v, int n, D ...m) {return vector<decltype(autov(v,m...))>(n,autov(v,m...)); }


class Solution {
public:
    bool canAliceWin(vector<string>& a, vector<string>& b) {
        function<void(vector<string>&, vector<string>&, vector<int>&, vector<int>&)> calc = 
                        [&] (vector<string>& source, vector<string>& target, vector<int>& L, vector<int>& R) {
                            int n = source.size(), m = target.size();
                            for (int i = 0, l = 0, r = 0; i < n; ++i) {
                                while (l < m && target[l] <= source[i]) ++l;
                                while (r < m && target[r][0] <= source[i][0]+1) ++r;
                                L[i] = l, R[i] = r;
                            }
                        };
        vector<int> la(a.size()), ra(a.size()), lb(b.size()), rb(b.size());
        calc(a,b,la,ra);
        calc(b,a,lb,rb);
        int n = max(a.size(),b.size());
        // vector<vector<int>> dp(2,vector<int>(n+1,-1));
        auto dp = autov(-1,2,n+1);
        function<int(int,int)> dfs = [&] (int i, int flag) {
            int &res = dp[flag][i];
            if (res != -1) return res;
            if (flag == 0) {
                if (i >= a.size()) return 0;
                res = dfs(la[i],flag^1)-dfs(ra[i],flag^1) == 0;
                res += dfs(i+1,flag);
            }
            else {
                if (i >= b.size()) return 0;
                res = dfs(lb[i],flag^1)-dfs(rb[i],flag^1) == 0;
                res += dfs(i+1,flag);
            }
            return res;
        };
        return dfs(0,0)-dfs(1,0) == 1;

    }
};