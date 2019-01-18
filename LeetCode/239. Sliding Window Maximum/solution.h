// class Solution {
// public:
//     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
//         vector<int> maxV,ans;
//         if(nums.size()==0){
//             return ans;
//         }
//         maxV.push_back(nums[k-1]);
//         for(int i=1;i<k;i++){
//             int tmp=max(nums[k-1-i],maxV.back());
//             maxV.push_back(tmp);
//         }
//         ans.push_back(maxV.back());
//         for(int i=k;i<nums.size();i++){
//             for(int j=k-1;j>0;j--){
//                 maxV[j]=max(maxV[j-1],nums[i]);
//             }
//             maxV[0]=nums[i];
//             ans.push_back(maxV.back());
//         }
//         return ans;
//     }
// };
//Solution: store successive rightMost max values

// class Solution {
// public:
//     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//         int len=nums.size();
//         vector<int> leftMax(len,0),rightMax(len,0),ans;
//         if(nums.empty())return ans;
//         for(int i=0;i<nums.size();i++){
//             if(i%k==0){
//                 leftMax[i]=nums[i];
//             }
//             else{
//                 leftMax[i]=max(nums[i],leftMax[i-1]);
//             }
//             if((len-1-i)%k==0||i==0){
//                 rightMax[len-1-i]=nums[len-1-i];
//             }
//             else{
//                 rightMax[len-1-i]=max(nums[len-1-i],rightMax[len-i]);
//             }
//         }
//         for(int i=k-1;i<len;i++){
//             ans.push_back(max(leftMax[i],rightMax[i-k+1]));
//         }
//         return ans;
//     }
// };

//two pass and seperate windows Solution


// class Monoqueue
// {
//     deque<pair<int,int>> dq;
// public:
//     void push(int x){
//         int count=0;
//         while(!dq.empty() && dq.back().first<x){
//             count+=dq.back().second+1;
//             dq.pop_back();
//         }
//         dq.push_back(make_pair(x,count));
//         return;
//     }
//     int max(){
//         return dq.front().first;
//     }
//     void pop(){
//         if(dq.front().second>0)dq.front().second--;
//         else dq.pop_front();
//         return;
//     }
// };


// struct Solution {
// public:
//     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//         vector<int> ans;
//         if(nums.empty())return ans;
//         Monoqueue mq;
//         for(int i=0;i<k;i++){
//             mq.push(nums[i]);
//         }
//         ans.push_back(mq.max());
//         for(int i=k;i<nums.size();i++){
//             mq.push(nums[i]);
//             mq.pop();
//             ans.push_back(mq.max());
//         }
//         return ans;
//     }
// };

//This is a typical monotonic queue problem
//https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem
//why is struct way fast than class



class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        for (int i=0; i<nums.size(); i++) {
            if (!dq.empty() && dq.front() == i-k) dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i])
                dq.pop_back();
            dq.push_back(i);
            if (i>=k-1) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};