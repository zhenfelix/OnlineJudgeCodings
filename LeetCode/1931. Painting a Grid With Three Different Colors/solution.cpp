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