class Solution {
public:
    int getAnswer(vector<int>& nums, int left, int right) {
        if (left > right) {
            return -1;
        }
        int mid = (right - left) / 2 + left;
        int leftAnswer = getAnswer(nums, left, mid - 1);
        if (leftAnswer != -1) {
            return leftAnswer;
        } else if (nums[mid] == mid) {
            return mid;
        }
        return getAnswer(nums, mid + 1, right);
    }

    int findMagicIndex(vector<int>& nums) {
        return getAnswer(nums, 0, (int) nums.size() - 1);
    }
};


作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/magic-index-lcci/solution/mo-zhu-suo-yin-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。