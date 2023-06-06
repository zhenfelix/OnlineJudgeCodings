class Solution {
public:
    int count(string num1, string num2, int min_sum, int max_sum) {
        const int MOD = 1e9 + 7;
        string A;
        long long f[25][2][410];
        
        function<long long(int, int, int)> dp = [&](int pos, int full, int sm) {
            if (pos == -1) {
                if (sm >= min_sum && sm <= max_sum) return 1LL;
                else return 0LL;
            }

            if (f[pos][full][sm] >= 0) return f[pos][full][sm];
            long long &ret = f[pos][full][sm];
            ret = 0;
            int R = full ? A[pos] - '0' : 9;
            for (int i = 0; i <= R && sm + i <= max_sum; i++) {
                ret = (ret + dp(pos - 1, full && i == R, sm + i)) % MOD;
            }
            return ret;
        };

        reverse(num2.begin(), num2.end());
        A = num2;
        for (int i = 0; i < A.size(); i++) for (int j = 0; j <= max_sum; j++) f[i][0][j] = f[i][1][j] = -1;
        long long X = dp(A.size() - 1, 1, 0);

        reverse(num1.begin(), num1.end());
        num1[0]--;
        for (int i = 0; i < num1.size(); i++) {
            char &t = num1[i];
            if (t == '0' - 1) t = '9', num1[i + 1]--;
        }
        A = num1;
        for (int i = 0; i < A.size(); i++) for (int j = 0; j <= max_sum; j++) f[i][0][j] = f[i][1][j] = -1;
        long long Y = dp(A.size() - 1, 1, 0);
        return (X - Y + MOD) % MOD;
    }
};