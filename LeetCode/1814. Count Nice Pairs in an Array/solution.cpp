// const int MOD = 1e9+7;

// class Solution {
// public:
//     int rev(int x){
//         int y = 0;
//         while (x){
//             y *= 10;
//             y += (x%10);
//             x /= 10;
//         }
//         return y;
//     }
    
//     int countNicePairs(vector<int>& nums) {
//         int res = 0;
//         unordered_map<int,int> cc;
//         for (auto &x : nums){
//             int val = x - rev(x);
//             res += cc[val];
//             cc[val]++;
//             res %= MOD;
//         }
//         return res;
//     }
// };


class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        long count = 0;
        int mod = (int)1e9 + 7;
        unordered_map<long, long> map;
        for (int num : nums) {
            long tmp = num - getRecv(num);
            map[tmp]++;
        }
        for (auto it = map.begin(); it != map.end(); it++) {
            long time = it->second;
            count += (time * (time - 1) / 2) % mod;
        }
        return (int)count % mod;
    }

    long getRecv(int num) {
        int res = 0;
        while (num) {
            res = res * 10 + num % 10;
            num = num / 10;
        }
        return res;
    }
};
