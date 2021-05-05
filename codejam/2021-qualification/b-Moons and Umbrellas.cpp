#include <bits/stdc++.h>

using namespace std;

const int inf = 0x3f3f3f3f;

class Solution
{
public:
    long long minCost(string &s, int cj, int jc)
    {
        int j = 0, c = 0;
        if (s[0] == 'J')
            c = inf;
        if (s[0] == 'C')
            j = inf;
        for (char ch : s.substr(1))
        {
            if (ch == 'J')
            {
                j = (c == inf ? j : min(c + cj, j));
                c = inf;
            }
            else if (ch == 'C')
            {
                c = (j == inf ? c : min(j + jc, c));
                j = inf;
            }
            else
            {
                int old_c = c, old_j = j;
                c = (old_j == inf ? old_c : min(old_j + jc, old_c));
                j = (old_c == inf ? old_j : min(old_c + cj, old_j));
            }
        }
        return min(c, j);
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    freopen("input", "r", stdin);
    Solution sol;
    int T, x, y, idx = 1;
    cin >> T;
    while (T--)
    {
        cin >> x >> y;
        string s;
        cin >> s;

        cout << "Case #" << idx++ << ": " << sol.minCost(s, x, y) << "\n";
    }
}