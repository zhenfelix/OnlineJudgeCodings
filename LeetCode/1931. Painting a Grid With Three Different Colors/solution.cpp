class Solution {
public:
    int memo[1000][1024] = {};
    int m, n, MOD = 1e9 + 7;
    int colorTheGrid(int m, int n) {
        this->m = m; this->n = n;
        return dp(0, 0);
    }
    int dp(int c, int prevColMask) {
        if (c == n) return 1; // Found a valid way
        if (memo[c][prevColMask]) return memo[c][prevColMask];
        int ans = 0;
        vector<int> neighbors;
        dfs(0, prevColMask, 0, neighbors);
        for (int nei : neighbors)
            ans = (ans + dp(c + 1, nei)) % MOD;
        return memo[c][prevColMask] = ans;
    }
    void dfs(int r, int prevColMask, int curColMask, vector<int>& out) {
        if (r == m) { // Filled full color for a row
            out.push_back(curColMask);
            return;
        }
        for (int i = 1; i <= 3; ++i) // Try colors i in [1=RED, 2=GREEN, 3=BLUE]
            if (getColor(prevColMask, r) != i && (r == 0 || getColor(curColMask, r-1) != i))
                dfs(r + 1, prevColMask, setColor(curColMask, r, i), out);
    }
    int getColor(int mask, int pos) { // Get color of the `mask` at `pos`, 2 bit store 1 color
        return (mask >> (2 * pos)) & 3;
    }
    int setColor(int mask, int pos, int color) { // Set `color` to the `mask` at `pos`, 2 bit store 1 color
        return mask | (color << (2 * pos));
    }
};



class Solution
{
public:
    int colorTheGrid(int m, int n)
    {
        int MOD = 1e9+7;
        vector<pair<int, int>> valids;
        map<pair<int, int>, int> dp, ndp;
        int mask = (1 << m) - 1;
        for (int r = 0; r <= mask; r++)
        {
            for (int b = 0; b <= mask; b++)
            {
                int g = (mask ^ r) & (mask ^ b);
                if (r & b || (r >> 1) & r || (b >> 1) & b || (g >> 1) & g)
                    continue;
                valids.push_back({r, b});
                dp[{r, b}] = 1;
                // cout << r << " " << b << endl;
            }
        }
        for (int i = 1; i < n; i++)
        {
            for (auto &[cur_r, cur_b] : valids)
            {
                int cur_g = (mask ^ cur_r) & (mask ^ cur_b);
                for (auto &[nxt_r, nxt_b] : valids)
                {
                    int nxt_g = (mask ^ nxt_r) & (mask ^ nxt_b);
                    if (cur_r & nxt_r || cur_b & nxt_b || cur_g & nxt_g)
                        continue;
                    ndp[{nxt_r, nxt_b}] += dp[{cur_r, cur_b}];
                    ndp[{nxt_r, nxt_b}] %= MOD;
                }
            }
            swap(dp, ndp);
            ndp.clear();
        }
        int res = 0;
        for (auto &[k, v] : dp)
        {
            // cout << k.first << " " << k.second << " " << v << endl;
            res += v;
            res %= MOD;
        }
        return res;
    }
};