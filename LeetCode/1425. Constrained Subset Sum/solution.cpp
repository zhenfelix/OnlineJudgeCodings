const int maxn = 1e5+5;

int st[maxn];

class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int left = 0, right = -1, n = nums.size(), res = INT_MIN;
        for (int i = 0; i < n; i++){
            if (left <= right && st[left] < i-k)
                left++;
            int tmp = 0;
            if (left <= right)
                tmp = max(tmp, nums[st[left]]);
            nums[i] += tmp;
            res = max(res, nums[i]);
            while(left <= right && nums[st[right]] <= nums[i])
                right--;
            st[++right] = i;
            // cout << nums[i] << " " << left << " " << right << endl;
        }
        return res;
    }
};

