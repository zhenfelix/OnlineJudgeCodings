using ll = long long;
class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        int n = nums.size();
        ll res = LONG_MAX;
        vector<int> idx;
        vector<ll> presums = {0};
        for (int i = 0; i < n; i++)
            if (nums[i])
                idx.push_back(i), presums.push_back(presums.back()+i);
        int m = idx.size();
        for (int right = k-1; right < m; right++){
            int mid = right-k/2;
            int pos = idx[mid], left = mid - (k-1)/2;
            ll left_sums = static_cast<ll>(pos+pos-(mid-left))*(mid-left+1)/2-(presums[mid+1]-presums[left]);
            ll right_sums = presums[right+1]-presums[mid+1]-static_cast<ll>(pos+1+pos+(right-mid))*(right-mid)/2;
            res = min(res, left_sums+right_sums);
        }
        return res;
    }
};