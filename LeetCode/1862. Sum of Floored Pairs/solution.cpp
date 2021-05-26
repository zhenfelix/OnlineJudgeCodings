typedef long long LL;

const int N = 100010, MOD = 1e9 + 7;

int s[N];

class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        memset(s, 0, sizeof s);
        for (auto x: nums) s[x] ++ ;
        for (int i = 1; i < N; i ++ ) s[i] += s[i - 1];
        int res = 0;
        
        for (int i = 1; i < N; i ++ ) {
            for (int j = 1; j * i < N; j ++ ) {
                int l = j * i, r = min(N - 1, (j + 1) * i - 1);
                int sum = (LL)(s[r] - s[l - 1]) * j % MOD;
                res = (res + (LL)sum * (s[i] - s[i - 1])) % MOD;
            }
        }
        return res;
    }
};

