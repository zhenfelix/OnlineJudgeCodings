using ll = long long;
const int MOD = 1e9+7;
const int inf = 0x3f3f3f3f;

class Solution {
public:
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        ll dp1 = 0, dp2 = 0;
        int left = 0, right = 0;
        for (int i = -1, j = -1; i < n1 || j < n2;){
            if (left == right)
                dp1 = dp2 = max(dp1,dp2);
            int left_ = left, right_ = right;
            if (left_ <= right_){
                if (i+1 < n1){
                    left = nums1[i+1];
                    dp1 += left;
                }
                else
                    left = inf;
                i++;
            }
            if (left_ >= right_){
                if (j+1 < n2){
                    right = nums2[j+1];
                    dp2 += right;
                }
                else
                    right = inf;
                j++;
            }

        }
        return max(dp1,dp2)%MOD;
    }
};