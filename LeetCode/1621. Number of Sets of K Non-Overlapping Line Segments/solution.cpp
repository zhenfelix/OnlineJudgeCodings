// class Solution
// {
// public:
//     int numberOfSets(int n, int k)
//     {
//         const int MOD = 1e9 + 7;
//         vector<vector<long long>> zeros(n + 1, vector<long long>(n + 1, 0)), ones(n + 1, vector<long long>(n + 1, 0));
        
//         for (int i = 2; i <= n; i++)
//         {
//             zeros[i][0] = 1;
//             ones[i][i - 1] = 1;
//             zeros[i][i - 2] = 1;
//         }
//         for (int i = 2; i <= n; i++)
//         {
//             for (int j = 1; j <= i - 2; j++)
//             {
//                 ones[i][j] = ones[i - 1][j] + ones[i - 1][j - 1] + zeros[i - 1][j - 1];
//                 ones[i][j] %= MOD;
//                 if (j < i - 2)
//                 {
//                     zeros[i][j] = ones[i - 1][j] + zeros[i - 1][j];
//                     zeros[i][j] %= MOD;
//                 }
//             }
//         }
//         return (zeros[n][k] + ones[n][k]) % MOD;
//     }
// };

using ll = long long;
class Solution
{
public:
    int numberOfSets(int n, int k)
    {
        const int MOD = 1e9 + 7;
        vector<vector<int>> zeros(n + 1, vector<int>(k + 1, 0)), ones(n + 1, vector<int>(k + 1, 0));
        
        for (int i = 2; i <= n; i++)
        {
            zeros[i][0] = 1;
            if (i-1 <= k)
                ones[i][i - 1] = 1;
            if (i-2 <= k)
                zeros[i][i - 2] = 1;
            for (int j = 1; j <= min(i - 2,k); j++)
            {
                ones[i][j] = (static_cast<ll>(ones[i - 1][j]) + ones[i - 1][j - 1] + zeros[i - 1][j - 1])%MOD;
                if (j < i - 2)
                {
                    zeros[i][j] = (static_cast<ll>(ones[i - 1][j]) + zeros[i - 1][j])%MOD;
                }
            }
        }
        return (static_cast<ll>(zeros[n][k]) + ones[n][k]) % MOD;
    }
};