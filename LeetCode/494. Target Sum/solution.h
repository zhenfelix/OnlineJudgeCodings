// class Solution {
// public:
//     void dfs(vector<int>& nums, int S, int idx, int &cc){
//         if(idx==nums.size()){if(S==0)cc++;return;}
//         dfs(nums,S+nums[idx],idx+1,cc);
//         dfs(nums,S-nums[idx],idx+1,cc);
//         return;
//     }
//     int findTargetSumWays(vector<int>& nums, int S) {
//         int cc=0;
//         dfs(nums,S,0,cc);
//         return cc;
//     }
// };
//brute force


// class Solution {
// public:
//     void dfs(vector<int>& nums, vector<int>& sums, int S, int idx, int &cc){
//         if(idx==nums.size()){
//             if(S==0)cc++;
//             return;
//         }
//         if(S>sums[idx]||S<-sums[idx])return;
//         dfs(nums,sums,S+nums[idx],idx+1,cc);
//         dfs(nums,sums,S-nums[idx],idx+1,cc);
//         return;
//     }
//     static bool cmp(int x, int y){return x>y;}
//     int findTargetSumWays(vector<int>& nums, int S) {
//         int cc=0;
//         sort(nums.begin(),nums.end(),cmp);
//         vector<int> sums=nums;
//         for(int i=sums.size()-2;i>=0;i--)sums[i]+=sums[i+1];
//         dfs(nums,sums,S,0,cc);
//         return cc;
//     }
// };
//brute force with branch pruning


class Solution {
public:
    static bool cmp(int x, int y){return x>y;}
    int findTargetSumWays(vector<int>& nums, int S) {
        sort(nums.begin(),nums.end(),cmp);
        vector<int> sums=nums;
        unordered_map<int,int>count;
        count[0]=1;
        for(int i=sums.size()-2;i>=0;i--)sums[i]+=sums[i+1];
        for(int i=0;i<nums.size();i++){
            unordered_map<int,int>tmp;
            for(unordered_map<int,int>::iterator p=count.begin();p!=count.end();p++){
                if((p->first-sums[i]>S)||(p->first+sums[i]<S))continue;
                tmp[p->first+nums[i]]+=count[p->first];
                tmp[p->first-nums[i]]+=count[p->first];
            }
            count=tmp;
        }
        return count[S];
    }
};
// dynamic programing and O(n) space solution

// class Solution {
// public:
//     static bool cmp(int x, int y){return x>y;}
//     int findTargetSumWays(vector<int>& nums, int S) {
//         sort(nums.begin(),nums.end(),cmp);
//         vector<int> sums=nums;
//         for(int i=sums.size()-2;i>=0;i--)sums[i]+=sums[i+1];
//         vector<int>count(2001,0);
//         count[1000]=1;
//         for(int i=0;i<nums.size();i++){
//             vector<int>tmp(2001,0);
//             for(int j=0;j<=2000;j++){
//                 if((j-sums[i]>S+1000)||(j+sums[i]<S+1000)||(count[j]==0))continue;
//                 tmp[j+nums[i]]+=count[j];
//                 tmp[j-nums[i]]+=count[j];
//             }
//             count=tmp;
//         }
//         if(abs(S)>1000)return 0;
//         return count[S+1000];
//     }
// };