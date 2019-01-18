#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         if(nums.size()==0)return 0;
//         int a=nums[0],b=0;
//         int pa=a,pb=b;
//         for(int i=1;i<nums.size();i++){
//             a=max(pb+nums[i],pa+nums[i]-nums[i-1]);
//             b=max(pa,pb);
//             pa=a;pb=b;
//         }
//         return a>b?a:b;
//     }
// };

// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         int ans=0,pre=0;
//         bool flag=true;
//         for(int i=0;i<nums.size();i++){
//             if(flag){
//                 if(pre+nums[i]>ans){
//                     int tmp=ans;
//                     ans=pre+nums[i];
//                     pre=tmp;
//                 }
//                 else flag=false;
//             }
//             else{
//                 pre=ans;
//                 ans=ans+nums[i];
//                 flag=true;
//             }
//         }
//         return ans;
//     }
// };


// class Solution {
// public:
//     int rob(vector<int>& nums) {
        
//         vector<int> ans(nums.size(),0);
        
//         for(int i=0;i<nums.size();i++){
//             if(i==0)ans[i]=nums[i];
//             else if(i==1)ans[i]=max(ans[i-1],nums[i]);
//             else ans[i]=max(ans[i-1],ans[i-2]+nums[i]);
//         }
//         if(nums.size()>0) return ans.back();
//         return 0;
//     }
// };


class Solution {
public:
    int rob(vector<int>& nums) {
        int ans=0,pre=0;
        for(int i=0;i<nums.size();i++){
            int tmp=ans;
            ans=max(pre+nums[i],ans);
            pre=tmp;
        }
        return ans;
    }
};