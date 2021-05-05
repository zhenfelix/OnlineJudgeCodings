// class Solution {
// public:
//     int countDifferentSubsequenceGCDs(vector<int>& nums) {
//         vector<bool> cnts(200001, false);
//         int m = 0;
//         for (auto i : nums) {
//             m = max(m, i);
//             cnts[i] = true;
//         }
        
//         for (int i = m; i >= 1; --i) {
//             if (cnts[i]) continue;
//             int cgcd = 0;
//             for (int j = 1; (j*i) <= m; ++j) {
//                 if (cnts[j*i]) {
//                     cgcd = (!cgcd) ? j : gcd(cgcd, j);
//                     if (cgcd == 1) {
//                         cnts[i] = true;
//                         break;
//                     }
//                 }
//             }
//         }
//         int res = 0;
//         for (auto i : cnts) {
//             if (i) ++res;
//         }
//         return res;
//     }
// };

// class Solution {
// public:
//     inline int gcd(int i, int j) {
//         return i == 0 ? j : gcd(j % i, i);
//     }

//     int countDifferentSubsequenceGCDs(vector<int>& nums) {
//         int max_elem = *max_element(nums.begin(), nums.end());
//         vector<bool> visited(max_elem + 10, false);
//         for (int i : nums) {
//             visited[i] = true;
//         }
        
//         int ans = 0;
//         for (int i=1; i<=max_elem; i++) {
//             int g = 0;
//             for (int j=i; j<=max_elem; j+=i) {
//                 if (visited[j]) {
//                     g = gcd(g, j);
//                     if (g == i) {
//                         ans++;
//                         break;
//                     }
//                 }
//             }
//         }
//         return ans;
//     }
// };


class Solution {
public:
    inline int gcd(int i, int j) {
        return i == 0 ? j : gcd(j % i, i);
    }

    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        int max_elem = *max_element(nums.begin(), nums.end());
        vector<int> dp(max_elem + 10, 0);
        
        int ans = 0;
        for (int num: nums) {
            for (int i = 1; i*i <= num; ++i)
            {
                if(num%i == 0)
                {
                    dp[i] = gcd(dp[i], num);
                    dp[num/i] = gcd(dp[num/i], num);
                }
            }
        }
        for (int i=1; i< max_elem+1; i++)if(dp[i] == i) ans++;
        return ans;
    }
};