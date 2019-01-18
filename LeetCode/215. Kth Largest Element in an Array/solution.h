// class Solution {
// public:
//     int findKthLargest(vector<int>& nums, int k) {
//         priority_queue<int,vector<int>, greater<int>> pq;
//         int len=nums.size();
//         for(int i=0;i<len;i++){
//             pq.push(nums[i]);
//             while(pq.size()>k)pq.pop();
//         }
//         return pq.top();
//     }
// };

class Solution {
public:
    int helper(vector<int> &nums,int left,int right,int k){
        if(left==right)return nums[left];
        int small=left+1,front;
        for(front=left+1;front<=right;front++){
            if(nums[front]>nums[left])swap(nums[small],nums[front]),small++;
        }
        if(small==k)return nums[left];
        swap(nums[left],nums[small-1]);
        if(small>k)return helper(nums,left,small-1,k);
        else return helper(nums,small,right,k);
    }
    int findKthLargest(vector<int>& nums, int k) {
        return helper(nums,0,nums.size()-1,k);
    }
};

// static auto optimize = []() {
//     ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;
// }();

