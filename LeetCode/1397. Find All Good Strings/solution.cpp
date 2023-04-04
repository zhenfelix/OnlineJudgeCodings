#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<int> kmp(string &pattern)
{
    int sz = pattern.size();
    vector<int> fail(sz + 1, -1);
    int j = -1;
    for (int i = 0; i < sz; i++)
    {
        char ch = pattern[i];
        while (j != -1 && pattern[j] != ch)
        {
            j = fail[j];
        }
        j++;
        fail[i + 1] = j;
    }
    return fail;
}

class Solution
{
public:
    int findGoodStrings(int n, string s1, string s2, string evil)
    {
        const int MOD = 1e9 + 7;
        vector<int> fail = kmp(evil);
        int m = evil.length();
        vector<vector<int>> fmp(26, vector<int>(m + 1, -1));
        for (int ch = 0; ch < 26; ch++)
        {
            for (int j = 0; j < m; j++)
            {
                int t = j;
                while (t != -1 && evil[t] != ch + 'a')
                {
                    t = fail[t];
                }
                t++;
                fmp[ch][j] = t;
            }
            fmp[ch][m] = m;
        }
        int tot = (m + 1) * 4;
        vector<ll> dp(tot, 1), ndp(tot, 0);
        for (int i = 0; i < 4; i++)
        {
            dp[i * (m + 1) + m] = 0;
        }
        for (int i = n - 1; i >= 0; i--)
        {
            for (int cur = 0; cur < 4; cur++)
            {
                char hi = (cur & 1) ? s2[i] : 'z';
                char lo = (cur & 2) ? s1[i] : 'a';
                for (int j = 0; j <= m; j++)
                {
                    ndp[cur * (m + 1) + j] = 0;
                    for (char ch = lo; ch <= hi; ch++)
                    {
                        int nxt = cur;
                        int tmp = 0;
                        if (ch == lo)
                        {
                            tmp |= 2;
                        }
                        if (ch == hi)
                        {
                            tmp |= 1;
                        }
                        nxt &= tmp;
                        ndp[cur * (m + 1) + j] = (ndp[cur * (m + 1) + j] + dp[nxt * (m + 1) + fmp[ch-'a'][j]]) % MOD;
                    }
                }
            }
            swap(dp, ndp);
        }
        return dp[3 * (m + 1)];
    }
};


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