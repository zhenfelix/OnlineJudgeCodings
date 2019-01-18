// class Solution {
// public:
//     int hammingDistance(int x, int y) {
//         int ans=0;
//         x=x^y;
//         while(x){
//             if(x&1)ans++;
//             x=x>>1;
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int hammingDistance(int x, int y) {
        int dist = 0, n = x ^ y;
        while (n) {
            ++dist;
            n &= n - 1;
        }
        return dist;
    }
};