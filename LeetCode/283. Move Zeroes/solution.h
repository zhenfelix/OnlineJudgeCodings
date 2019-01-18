#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     void moveZeroes(vector<int>& nums) {
//         int end=nums.size();
//         end--;
//         int len=end;
//         for(int i=len;i>=0;i--){
//             if(nums[i]==0){
//                 int j=i;
//                 while(j<end){
//                     swap(nums[j],nums[j+1]);
//                     j++;
//                 }
//                 end--;
//             }
//         }
//     }
// };
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastZero = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                int current = nums[i];
                nums[i] = nums[lastZero];
                nums[lastZero] = current;
                lastZero++;
            }
        }  
    }
};