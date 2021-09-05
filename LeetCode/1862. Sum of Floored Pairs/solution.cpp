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

const int maxn = 1e5+5;

class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        vector<int> cnt(maxn, 0), presums(maxn, 0);
        int res = 0, MOD = 1e9+7;
        for(auto &x : nums)
            cnt[x]++;
        for (int i = 1; i < maxn; i++)
            presums[i] = presums[i-1] + cnt[i];
        for(int i = 1; i < maxn; i++){
            if (cnt[i] == 0)
                continue;
            for (int j = i; j < maxn; j += i){
                int tmp = (long long) cnt[i]*(presums[min(j+i-1,maxn-1)]-presums[j-1])*j/i%MOD;
                res += tmp;
                res %= MOD;
            }
        }
        return res;
    }
};



// class Solution {
// public:
//     int sumOfFlooredPairs(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         long long res = 0;
//         int MOD = 1e9+7;
//         int n = nums.size();
//         for (int i = 0; i < n; i++){
//             int pre = lower_bound(nums.begin(), nums.end(), nums[i]) - nums.begin();;
//             for (int j = 2;;j++){
//                 int cur = lower_bound(nums.begin(), nums.end(), nums[i]*j) - nums.begin();
//                 res += (long long) (j-1)*(cur-pre);
//                 res %= MOD;
//                 pre = cur;
//                 if (cur >= n)
//                     break;
//             }
//         }
//         return res;
//     }
// };