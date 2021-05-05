#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int n = 100;
const int m = 10000;

class Solution
{
public:
    int cheatingDetector(vector<vector<bool>> &results)
    {
        vector<int> cnt(m, 0);
        for (int j = 0; j < m; j++)
        {
            for (int i = 0; i < n; i++)
            {
                cnt[j] += results[i][j];
            }
        }
        vector<int> idx(m);
        for (int j = 0; j < m; j++)
        {
            idx[j] = j;
        }
        sort(idx.begin(), idx.end(), [&](int a, int b) { return cnt[a] < cnt[b]; });
        vector<double> abnormal(n, 0);
        for (int i = 0; i < n; i++)
        {
            int zeros = 0, ones = 0;
            // flog << i << " th row invs: " << invs;
            for (auto j : idx)
            {
                if (!results[i][j])
                {
                    zeros++;
                    abnormal[i] += ones;
                }
                else
                {
                    ones++;
                }
            }
            abnormal[i] /= (zeros+1)*(ones+1);
            // flog << ", after : " << zeros << endl;
        }
        vector<int> player(n);
        for (int i = 0; i < n; i++)
        {
            player[i] = i;
        }
        // sort(player.begin(), player.end(), [&](int a, int b) { return abnormal[a] > abnormal[b]; });
        return 1 + (*max_element(player.begin(), player.end(), [&](int a, int b) { return abnormal[a] < abnormal[b]; }));
        // for (int i = 0; i < n; i++)
        //     flog << player[i] + 1 << " : " << abnormal[player[i]] << "; ";
        // flog << endl;
        // return player[0] + 1;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/codejam/2021-qualification/test_data_e/test_set_2/ts2_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/codejam/2021-qualification/test_data_e/test_set_2/ts2_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    vector<int> vec;
    Solution sol;
    int T, P, idx = 1;

    cin >> T >> P;
    while (T--)
    {
        vector<vector<bool>> results(n, vector<bool>(m, false));
        string line;
        for (int i = 0; i < n; i++)
        {
            cin >> line;
            for (int j = 0; j < m; j++)
            {
                if (line[j] == '1')
                    results[i][j] = true;
            }
        }
        cout << "Case #" << idx++ << ": " << sol.cheatingDetector(results) << endl;
    }
}