class Solution {
public:
    long long continuousSubarrays(vector<int> &nums) {
        long long ans = 0;
        multiset<int> s;
        int left = 0, n = nums.size();
        for (int right = 0; right < n; right++) {
            s.insert(nums[right]);
            while (*s.rbegin() - *s.begin() > 2)
                s.erase(s.find(nums[left++]));
            ans += right - left + 1;
        }
        return ans;
    }
};


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/501Jzp/view/uQITil/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。