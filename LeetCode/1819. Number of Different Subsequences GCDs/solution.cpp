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


class Solution {
public:
    inline int gcd(int i, int j) {
        return i == 0 ? j : gcd(j % i, i);
    }

    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        int max_elem = *max_element(nums.begin(), nums.end());
        vector<int> dp(max_elem + 10, 0);
        for (int num : nums)
            dp[num] = num;
        
        int ans = 0;
        for (int i = max_elem; i >= 1; i--) {
            for (int j = i; j <= max_elem; j = j + i){
                if (dp[j] == j){
                    dp[i] = gcd(dp[i], j);
                }
                if (dp[i] == i){
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
};


class Solution {
public:
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        int c = *max_element(nums.begin(), nums.end());
        vector<int> g(c + 1);
        
        for (int x: nums) {
            for (int y = 1; y * y <= x; ++y) {
                if (x % y == 0) {
                    if (!g[y]) {
                        g[y] = x;
                    }
                    else {
                        g[y] = gcd(g[y], x);
                    }
                    if (y * y != x) {
                        int z = x / y;
                        if (!g[z]) {
                            g[z] = x;
                        }
                        else {
                            g[z] = gcd(g[z], x);
                        }
                    }
                }
            }
        }
        
        int ans = 0;
        for (int i = 1; i <= c; ++i) {
            if (g[i] == i) {
                ++ans;
            }
        }
        return ans;
    }
};


// 作者：zerotrac2
// 链接：https://leetcode-cn.com/problems/number-of-different-subsequences-gcds/solution/xu-lie-zhong-bu-tong-zui-da-gong-yue-shu-lrka/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        unordered_set<int> seen(nums.begin(), nums.end());
        int mx = *max_element(nums.begin(), nums.end());
        int res = 0;
        for (int i = 1; i <= mx; i++){
            int cur = -1;
            for (int j = i; j <= mx; j = j + i){
                if (seen.find(j) == seen.end())
                    continue;
                cur = cur == -1 ? j : gcd(cur, j);
                if (cur == i){
                    res++;
                    break;
                }
            }
        }
        return res;
    }
};


// class Solution {
// public:
//     int countDifferentSubsequenceGCDs(vector<int>& nums) {
//         set<int> st;
//         for (auto x : nums){
//             if (st.find(x) != st.end())
//                 continue;
//             set<int> tmp;
//             for (auto it = st.begin(); it != st.end(); it++){
//                 tmp.insert(gcd(*it, x));
//             }
//             for (auto it = tmp.begin(); it != tmp.end(); it++){
//                 st.insert(*it);
//             }
//             st.insert(x);
//         }
//         return st.size();
//     }
// };
