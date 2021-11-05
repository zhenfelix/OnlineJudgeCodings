// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         vector<vector<int>> res;
//         unordered_set<int> mp;
//         int n = nums.size();
//         sort(nums.begin(), nums.end());
//         for (int i = 0; i < n; i++){
//             for (int j = i+1; j < n; j++){
//                 if (mp.count(-nums[i]-nums[j])){
//                     res.push_back({-nums[i]-nums[j],nums[i],nums[j]});
//                 }
//             }
//             mp.insert(nums[i]);
//         }
//         if (res.empty()) return {};
//         sort(res.begin(), res.end());
//         int j = 1;
//         for (int i = 1; i < res.size(); i++){
//             if (res[i] != res[i-1]) res[j++] = res[i];
//         }
//         res.resize(j);
//         return res;
//     }
// };


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        unordered_map<int,int> mp;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; i++) mp[nums[i]] = i;
        for (int i = 0; i < n; i++){
            if (i && nums[i] == nums[i-1]) continue;
            for (int j = i+1; j < n; j++){
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int target = -nums[i]-nums[j];
                if (mp.count(target) && mp[target] > j){
                    res.push_back({nums[i],nums[j],target});
                }
            }
        }
        return res;
    }
};



class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int n = nums.size();
        for (int i = 0; i < n && nums[i] <= 0; i++){

            if (i && nums[i] == nums[i-1])
                continue;
            for (int left = i+1, right = n-1; left < right;){
                if (nums[left] + nums[right] > -nums[i])
                    right--;
                else if (nums[left] + nums[right] < -nums[i])
                    left++;
                else{
                    res.push_back({nums[i],nums[left],nums[right]});
                    while (left+1 < right && nums[left+1] == nums[left])
                        left++;
                    left++;
                    while (left < right-1 && nums[right-1] == nums[right])
                        right--;
                    right--;
                }
            }
        }
        return res;
    }
};

