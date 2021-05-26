class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        int n = nums.size();
        int MOD = 1000000007;
        vector<int> idx, left, right;
        vector<long long> presums;
        presums.push_back(0);
        for (int i = 0; i < n; i++){
            idx.push_back(i);
            left.push_back(i);
            right.push_back(i);
            presums.push_back(presums.back()+nums[i]);
        }
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums[a] < nums[b];
        });
        vector<int> st;
        for (int i = 0; i < n; i++){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                left[i] = left[st.back()];
                st.pop_back();
            }
            st.push_back(i);
        }
        for (int i = n-1; i >= 0; i--){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                right[i] = right[st.back()];
                st.pop_back();
            }
            st.push_back(i);
        }
        long long res = 0;
        for (auto i : idx){
            res = max(res, nums[i]*(presums[right[i]+1]-presums[left[i]]));
        }
        return res%MOD;
    }
};