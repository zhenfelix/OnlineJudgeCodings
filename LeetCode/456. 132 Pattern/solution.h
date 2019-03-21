// class Solution {
// public:
//     bool find132pattern(vector<int>& nums) {
//         int n=nums.size(), low=INT_MAX;
//         if(n<3)return false;
//         for(int j=0;j<n-1;j++){
//             low=min(low,nums[j]);
//             for(int k=j+1;k<n;k++)if(nums[k]>low && nums[j]>nums[k])return true;
//         }
//         return false;
//     }
// };

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n=nums.size();
        vector<int> vecmin(nums);
        stack<int> st;
        if(n<3)return false;
        vecmin[0]=nums[0];
        for(int i=1;i<n;i++)vecmin[i]=min(vecmin[i-1],vecmin[i]);
        for(int j=n-1;j>0;j--){
            if(nums[j]>vecmin[j]){
                while(!st.empty() && st.top()<=vecmin[j])st.pop();
                if(!st.empty() && st.top()<nums[j])return true;
                st.push(nums[j]);
            }
        }
        return false;
    }
};
//you can also use array as stack