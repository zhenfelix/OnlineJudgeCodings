// class Solution {
// public:
//     void dfs(vector<int> &nums, vector<bool> &visit, int root){
//         int n=nums.size();
//         visit[root]=true;
//         for(int i=root-nums[root];i<n&&i<=root+nums[root];i++){
//             if(i<0)continue;
//             if(visit[i]==false)dfs(nums,visit,i);
//         }
//         return;
//     }
//     bool canJump(vector<int>& nums) {
//         int n=nums.size();
//         vector<bool> visit(n,false);
//         dfs(nums,visit,0);
//         return visit[n-1]==true;
//     }
// };
// time exceed limit

class Solution {
public:

    bool canJump(vector<int>& nums) {
        int n=nums.size(),reach=0,i=0;
        
        for(;i<n&&i<=reach;i++){
            reach=max(reach,i+nums[i]);
        }
        return i==n;
    }
};