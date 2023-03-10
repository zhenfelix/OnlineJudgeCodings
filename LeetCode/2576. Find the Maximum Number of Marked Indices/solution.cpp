class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater{});
        //for (int t : nums) cout << t << " "; cout << endl;
        int ret = 0;
        for (int i = 0, n = nums.size(), j = (n + 1) / 2; j < n; ++j) {
            if (nums[i] >= nums[j] * 2) {
                ++i;
                ret += 2;
            }
        }
        return ret;
    }
};