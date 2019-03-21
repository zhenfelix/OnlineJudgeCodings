// class Solution {
// public:
//     bool maxOut(int i, vector<int> &nums){
//         int n=nums.size();
//         if(i>=n)return false;
//         for(int j=n-1;j>i;j--){
//             if(nums[j]>nums[j-1])swap(nums[j],nums[j-1]);
//         }
//         return true;
//     }
//     int thirdMax(vector<int>& nums) {
//         int n=nums.size();
//         set<int> s;
//         for(int i=0;i<n;i++){
//             if(!maxOut(i, nums))break;
//             s.insert(nums[i]);
//             if(s.size()==3)return nums[i];
//         }
//         return nums[0];
//     }
// };


class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long first, second, third;
        first=second=third=LONG_MIN;
        for (auto num : nums) {
            if(num<=third || num==second || num==first) continue;
            third=num;
            if(third>second) swap(third, second);
            if(second>first) swap(second, first);
        }
        return (third==LONG_MIN) ? first : third;
    }

};

