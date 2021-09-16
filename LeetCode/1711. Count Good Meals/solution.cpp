// class Solution {
// public:
//     int countPairs(vector<int>& deliciousness) {
//         int MOD = 1e9+7, res = 0;
//         unordered_map<int,int> cc;
//         for (auto x : deliciousness){
//             for (int i = 0; i <= 21; i++){
//                 res += cc[(1<<i)-x];
//                 res %= MOD;
//             }
//             cc[x]++;
//         }
//         return res;
//     }
// };


// class Solution {
// public:
//     int countPairs(vector<int>& deliciousness) {
//         int MOD = 1e9+7, res = 0;
//         int mx = (*max_element(deliciousness.begin(), deliciousness.end()))*2;
//         unordered_map<int,int> cc;
//         for (auto x : deliciousness){
//             for (int y = 1; y <= mx; y <<= 1){
//                 res += cc[y-x];
//                 res %= MOD;
//             }
//             cc[x]++;
//         }
//         return res;
//     }
// };


class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        int MOD = 1e9+7, res = 0;
        int mx = (*max_element(deliciousness.begin(), deliciousness.end()))*2;
        unordered_map<int,int> cc;
        for (auto x : deliciousness){
            for (int y = 1; y <= mx; y <<= 1){
                res += cc.count(y-x)?cc[y-x]:0;
                res %= MOD;
            }
            cc[x]++;
        }
        return res;
    }
};