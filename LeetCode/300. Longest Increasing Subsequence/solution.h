// class Solution {
// public:
//     int lengthOfLIS(vector<int>& nums) {
//         int len=nums.size();
//         if(len==0)return 0;
//         vector<int> ans(len,1);
//         int res=0;
//         for(int i=0;i<len;i++){
//             for(int j=0;j<i;j++){
//                 if(nums[j]<nums[i])ans[i]=max(ans[i],ans[j]+1);
//             }
//             res=max(res,ans[i]);
//         }
//         // int a=0;
//         // for(auto aa: ans)if(aa>a)a=aa;
//         return res;
//     }
// };

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        
        vector<int> list;
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (list.size() == 0 || list[list.size()-1] < nums[i])
            {
                list.push_back(nums[i]);
            }
            else
            {
                int idx=lower_bound(list.begin(),list.end(),nums[i])-list.begin();
                
                list[idx] = nums[i];
            }
        }
        return list.size();
    }
};

// lower bound implementation >= target
// int lo = 0, hi = list.size()-1;
                
//                 while (lo < hi)
//                 {
//                     int mid = (lo+(hi-lo)/2);
//                     if (list[mid] < nums[i])
//                     {
//                         lo = mid+1;
//                     }
//                     else
//                     {
//                         hi = mid;
//                     }
//                 }
                