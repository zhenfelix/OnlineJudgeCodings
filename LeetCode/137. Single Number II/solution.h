#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x2=0,x1=0,mask;
        for(int i: nums){
            x2=x2^(x1&i);
            x1=x1^i;
            mask=~(x2&x1);
            x2=x2&mask;
            x1=x1&mask;
        }
        return x1;
    }
};

//https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers


// solution B
// class Solution {
// public:
//     int singleNumber(vector<int>& nums) {
//         vector<int> bits(32, 0);
//         for (int i = 0; i < nums.size(); ++i) {
//             for (int j = 0; j < 32; ++j) {
//                 bits[j] += ((nums[i] >> j) & 1);
//             }
//         }
//         int res = 0;
//         for (int i = 0; i < 32; ++i) {
//             if (bits[i] % 3 == 1) {
//                 //cout << i << " " << res << endl;
//                 res += (1 << i);
//             }
//         }
//         return res;
//     }
// };