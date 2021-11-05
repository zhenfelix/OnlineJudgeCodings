using pii = pair<int, int>;
using ll = long long;
const int MOD = 1e9 + 7;

class Solution
{
public:
    vector<int> mul_vec(vector<vector<int>> &a, vector<int> &x)
    {
        int row = a.size();
        vector<int> y(row, 0);
        for (int i = 0; i < row; i++)
        {
            for (int k = 0; k < row; k++)
            {
                y[i] = (y[i] + (ll)a[i][k] * x[k]) % MOD;
            }
        }
        return y;
    }
    vector<vector<int>> mul(vector<vector<int>> &a, vector<vector<int>> &b)
    {
        int row = a.size();
        vector<vector<int>> c(row, vector<int>(row, 0));
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < row; j++)
            {
                for (int k = 0; k < row; k++)
                {
                    c[i][j] = (c[i][j] + (ll)a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }
    vector<int> quick_mul(vector<vector<vector<int>>> &as, int p, vector<int> x)
    {
        int row = as[0].size();
        for (int i = 0; i < 32; i++){
            if ((p>>i)&1){
                x = mul_vec(as[i], x);
            }
        }
        return x;
    }

    int electricityExperiment(int row, int col, vector<vector<int>> &position)
    {
        vector<pii> pos;
        int n = position.size();
        for (int i = 0; i < n; i++)
        {
            pos.push_back({position[i][1], position[i][0]});
        }
        sort(pos.begin(), pos.end());
        vector<vector<int>> mat(row, vector<int>(row, 0));
        for (int i = 0; i < row; i++)
        {
            for (int j = max(0, i - 1); j < min(row, i + 2); j++)
            {
                mat[i][j] = 1;
            }
        }
        vector<vector<vector<int>>> mats;
        mats.push_back(mat);
        for (int i = 0; i < 31; i++){
            mats.push_back(mul(mats.back(), mats.back()));
        }
        vector<int> dp(row, 1);
        int pc = pos[0].first;
        for (auto [c, r] : pos)
        {
            dp = quick_mul(mats, c - pc, dp);
            pc = c;
            for (int i = 0; i < row; i++)
            {
                if (i != r)
                    dp[i] = 0;
            }
        }
        return dp[pos.back().second];
    }
};