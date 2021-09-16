class Solution {
public:
    int maxProduct(string s) {
        int n = s.length();
        auto check = [&](int state){
            vector<int> arr;
            for (int i = 0; i < n; i++)
                if ((state>>i)&1)
                    arr.push_back(i);
            int m = arr.size();
            int left = 0, right = m-1;
            while (left < right){
                if (s[arr[left]] != s[arr[right]])
                    return false;
                left++;right--;
            }
            return true;
        };
        vector<bool> dp(1<<n);
        vector<int> len(1<<n);
        int mask = (1<<n)-1, res = 0;
        for (int a = 0; a < (1<<n); a++){
            dp[a] = check(a);
            if (dp[a])
                len[a] = __builtin_popcount(a);
        }
        for (int a = 1; a < (1<<n); a++){
            if (dp[a]){
                int r = mask^a;
                for (int b = r; b; b = (b-1)&r){
                    if (dp[b]){
                        res = max(res, len[a]*len[b]);
                    }
                }
            }
        }
        return res;
        
    }
};


// class Solution {
// public:
//     int maxProduct(string s) {
//         int n = s.length();
//         auto check = [&](int state){
//             vector<int> arr;
//             for (int i = 0; i < n; i++)
//                 if ((state>>i)&1)
//                     arr.push_back(i);
//             int m = arr.size();
//             int left = 0, right = m-1;
//             while (left < right){
//                 if (s[arr[left]] != s[arr[right]])
//                     return false;
//                 left++;right--;
//             }
//             return true;
//         };
//         vector<bool> dp(1<<n);
//         int mask = (1<<n)-1, res = 0;
//         for (int a = 0; a < (1<<n); a++)
//             dp[a] = check(a);
//         for (int a = 1; a < (1<<n); a++){
//             if (dp[a]){
//                 int r = mask^a;
//                 int na = __builtin_popcount(a);
//                 for (int b = r; b; b = (b-1)&r){
//                     if (dp[b]){
//                         int nb = __builtin_popcount(b);
//                         res = max(res, na*nb);
//                     }
//                 }
//             }
//         }
//         return res;
        
//     }
// };