class Solution {
public:
    vector<int> distinctNumbers(vector<int>& nums, int k) {
        int n = nums.size(), j = 0, len = 0;
        vector<int> res;
        map<int,int> mp;
        for (int i = 0; i+k-1 < n; i++){
            for (; j < i+k; j++){
                mp[nums[j]]++;
                if (mp[nums[j]] == 1)
                    len++;
            }
            res.push_back(len);
            mp[nums[i]]--;
            if (mp[nums[i]] == 0)
                len--;
        }
        return res;
    }
};