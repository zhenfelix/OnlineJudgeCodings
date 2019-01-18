// class Solution {
// public:
//     int findDuplicate(vector<int>& nums) {
//         int pre=0,sum=0;

//         for(int i=0;i<nums.size();i++){
//             // if(nums[i]<0)return i+1;
//             if(nums[abs(nums[i])-1]<0)return abs(nums[i]);
//             nums[abs(nums[i])-1]=-nums[abs(nums[i])-1];
//         }
//         return 0;
//     }
// };

class Solution {
public:
    //
    // This problem can be transfromed to "Linked List Cycle" problem.
    // There are two pointers, one goes one step, another goes two steps.
    //
    // Refer to: https://en.wikipedia.org/wiki/Cycle_detection
    //
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int one = n;
        int two = n;

       do{
            one = nums[one-1];
            two = nums[nums[two-1]-1];
        } while(one != two); 
        
        //find the start point of the cycle
        one = n;
        while(one != two){
            one = nums[one-1];
            two = nums[two-1];
        }
        
        return one;
    }
};