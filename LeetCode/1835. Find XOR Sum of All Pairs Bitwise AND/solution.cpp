// class Solution {
// public:
//     int getXORSum(vector<int>& arr1, vector<int>& arr2) {
//         vector<int> cnt(32,0);
//         int res = 0;
//         for (auto x: arr1)
//         {
//             for (int i = 0; i < 32; i++)
//                 if (x & (1<<i))
//                     cnt[i]++;
//         }
//         for (auto x : arr2)
//         {
//             int tmp = 0;
//             for (int i = 0; i < 32; i++)
//                 if ((x & (1<<i)) && (cnt[i]&1))
//                     tmp |= (1<<i);
//             res ^= tmp;
//         }
//         return res;
//     }
// };

// class Solution {
// public:
//     int getXORSum(vector<int>& arr1, vector<int>& arr2) {
//         int ans = 0;
//         for(int i = 0; i < 30; i++){
//             int c1 = 0, c2 = 0;
//             for(int x : arr1){
//                 c1 ^= getBit(x, i);
//             }
//             if (!c1)
//                 continue;
//             for(int x : arr2){
//                 c2 ^= (c1 & getBit(x, i));
//             }
//             if(c2){
//                 ans |= 1 << i;
//             }
//         }
//         return ans;
//     }
    
//     int getBit(int a, int i){
//         return (a >> i) & 1;
//     }
// };

// class Solution {
// public:
//     int getXORSum(vector<int>& arr1, vector<int>& arr2) {
//         int tot1 = accumulate(arr1.begin(), arr1.end(), 0, bit_xor<int>());
//         int tot2 = accumulate(arr2.begin(), arr2.end(), 0, bit_xor<int>());
//         return tot1 & tot2;
//     }
// };

class Solution{
public:
    int getXORSum(vector<int>& a, vector<int>& b) {
    int res = 0, xa = accumulate(begin(a), end(a), 0, [](int s, int i) { return s ^ i; });
    for (auto n : b)
        res = res ^ (xa & n);
    return res;
}
};