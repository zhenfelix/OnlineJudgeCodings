class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        vector<int> nums = arr;
        sort(nums.begin(), nums.end());
        unordered_map<int,int> mp;
        for (int i = n-1; i >= 0; i--)mp[nums[i]] = i;
        int res = 0, reach = -1;
        for (int i = 0; i < n; ++i)
        {
            if (i > reach)res += 1;
            reach = max(reach, mp[arr[i]]);
            mp[arr[i]] += 1;
        }
        return res;
        
    }
};