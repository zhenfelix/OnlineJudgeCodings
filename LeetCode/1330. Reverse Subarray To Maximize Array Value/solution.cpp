const int inf = 0x3f3f3f3f;

class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        int n = nums.size(), sums = 0, delta = 0, mi = inf, mx = -inf;
        for (int i = 1; i < n; i++){
            sums += abs(nums[i]-nums[i-1]);
            delta = max(delta, abs(nums[i]-nums[0])-abs(nums[i]-nums[i-1]));
            delta = max(delta, abs(nums[i-1]-nums[n-1])-abs(nums[i-1]-nums[i]));
            delta = max(delta, (min(nums[i-1],nums[i])-mi)*2);
            delta = max(delta, (mx-max(nums[i-1],nums[i]))*2);
            mi = min(mi,max(nums[i-1],nums[i]));
            mx = max(mx,min(nums[i-1],nums[i]));
        }
        return sums+delta;
    }
};