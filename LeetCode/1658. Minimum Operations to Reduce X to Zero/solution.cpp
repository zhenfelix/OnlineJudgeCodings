class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        int sums = 0, cur = 0;
        for (auto num : nums)
            sums += num;
        int y = sums - x;
        if (y < 0)
            return -1;
        if (y == 0)
            return n;
        int left = 0, res = -1;
        for (int right = 0; right < n; right++){
            cur += nums[right];
            while (cur > y)
                cur -= nums[left++];
            if (cur == y)
                res = max(res, right-left+1);
        }
        return res == -1 ? -1 : n-res;

    }
};