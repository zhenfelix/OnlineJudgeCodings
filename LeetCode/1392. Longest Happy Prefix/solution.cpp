// class Solution {
// public:
//     string longestPrefix(string s) {
//         int n = s.length();
//         vector<int> nxt(n+1,-1);
//         nxt[1] = 0;
//         for (int i = 1; i < n; i++){
//             int j = nxt[i];
//             while (j != -1 && s[i] != s[j])
//                 j = nxt[j];
//             nxt[i+1] = j+1;
//         }
//         return s.substr(0,nxt[n]);
//     }
// };

// const int maxn = 1e5+5;
// int fail[maxn];

// class Solution {
// public:
//     string longestPrefix(string s) {
//         int n = s.length();
//         fail[0] = -1, fail[1] = 0;
//         for (int i = 1; i < n; i++){
//             int j = fail[i];
//             while (j != -1 && s[i] != s[j])
//                 j = fail[j];
//             fail[i+1] = j+1;
//         }
//         return s.substr(0,fail[n]);
//     }
// };

// using ll = long long;

// const int MOD = 1e9+7;

// class Solution {
// public:
//     string longestPrefix(string s) {
//         unordered_map<int,vector<int>> mp;
//         int n = s.length(), res = 0;
//         ll sums = 0, base = 257, q = 1;
//         for (int i = 0; i < n-1; i++, q = (q*base)%MOD){
//             sums = (sums+s[i]*q)%MOD;
//             mp[sums].push_back(i+1);
//         }
//         sums = 0;
//         for (int i = n-1; i > 0; i--){
//             sums = (sums*base+s[i])%MOD;
//             if (mp.count(sums)){
//                 while (!mp[sums].empty() && mp[sums].back() > n-i)
//                     mp[sums].pop_back();
//                 if (!mp[sums].empty() && mp[sums].back() == n-i && s.substr(0,n-i) == s.substr(i))
//                     res = n-i;
//             }
//         }
//         return s.substr(0,res);
//     }
// };


// using ll = long long;
// using pp = pair<int,int>;

// const int MOD1 = 1e9+7;
// const int MOD2 = 1e9+1;

// class Solution {
// public:
//     string longestPrefix(string s) {
//         map<pp,int> mp;
//         int n = s.length(), res = 0;
//         ll sums1 = 0, sums2 = 0, base1 = 257, base2 = 127, q1 = 1, q2 = 1;
//         for (int i = 0; i < n-1; i++, q1 = (q1*base1)%MOD1, q2 = (q2*base2)%MOD2){
//             sums1 = (sums1+s[i]*q1)%MOD1;
//             sums2 = (sums2+s[i]*q2)%MOD2;
//             mp[{sums1,sums2}] = i+1;
//         }
//         sums1 = 0, sums2 = 0;
//         for (int i = n-1; i > 0; i--){
//             sums1 = (sums1*base1+s[i])%MOD1;
//             sums2 = (sums2*base2+s[i])%MOD2;
//             if (mp.count({sums1,sums2})){
//                 res = n-i;
//             }
//         }
//         return s.substr(0,res);
//     }
// };


class Solution {
public:
    string longestPrefix(string s) {
        int n = s.size();
        int prefix = 0, suffix = 0;
        int base = 31, mod = 1000000007, mul = 1;
        int happy = 0;
        for (int i = 1; i < n; ++i) {
            prefix = ((long long)prefix * base + (s[i - 1] - 97)) % mod;
            suffix = (suffix + (long long)(s[n - i] - 97) * mul) % mod;
            if (prefix == suffix) {
                happy = i;
            }
            mul = (long long)mul * base % mod;
        }
        return s.substr(0, happy);
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/longest-happy-prefix/solution/zui-chang-kuai-le-qian-zhui-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。