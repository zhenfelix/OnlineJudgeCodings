
using ll = long long;

const int MOD = 1e9 + 7;

class Solution
{
public:
    string s, pattern;
    int n, m;
    bool equal;
    vector<vector<vector<int>>> dp;
    vector<int> fail;

    void kmp()
    {
        fail.assign(m + 1, -1);
        fail[1] = 0;
        int j = 0;
        for (int i = 1; i < m; i++)
        {
            while (j != -1 && pattern[i] != pattern[j])
                j = fail[j];
            fail[i + 1] = j + 1;
            j++;
        }
    }

    int match(int j, char ch)
    {
        while (j != -1 && pattern[j] != ch)
            j = fail[j];
        return j + 1;
    }

    int dfs(int i, int j, int greater)
    {
        if (j == m)
            return 0;
        if (i == n)
        {
            if (greater == 0)
                return equal;
            return 1;
        }
        if (dp[greater][i][j] != -1)
            return dp[greater][i][j];
        dp[greater][i][j] = greater == 1 ? 0 : dfs(i + 1, match(j, s[i]), 0);
        char start = greater == 1 ? 'a' : s[i] + 1;
        char finish = 'z';
        for (char ch = start; ch <= finish; ch++)
            dp[greater][i][j] = ((ll)dp[greater][i][j] + dfs(i + 1, match(j, ch), 1)) % MOD;
        return dp[greater][i][j];
    }
    int findGoodStrings(int n, string s1, string s2, string evil)
    {
        pattern = evil;
        m = pattern.length();
        this->n = n;
        kmp();
        s = s1;
        equal = true;
        dp.assign(2, vector<vector<int>>(n, vector<int>(m, -1)));
        int lo = dfs(0, 0, 0);
        s = s2;
        equal = false;
        dp.assign(2, vector<vector<int>>(n, vector<int>(m, -1)));
        int hi = dfs(0, 0, 0);
        return (lo - hi + MOD) % MOD;
    }
};