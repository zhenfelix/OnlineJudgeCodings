class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        vector<int> st, left(n), right(n);
        for (int i = 0; i < n; i++){
            int idx = lower_bound(st.begin(), st.end(), nums[i]) - st.begin();
            if (idx == st.size())
                st.push_back(0);
            st[idx] = nums[i];
            left[i] = idx+1;
        }
        st.clear();
        for (int i = n-1; i >= 0; i--){
            int idx = lower_bound(st.begin(), st.end(), nums[i]) - st.begin();
            if (idx == st.size())
                st.push_back(0);
            st[idx] = nums[i];
            right[i] = idx+1;
        }
        int res = 0;
        for (int i = 1; i < n-1; i++){
            if (left[i] > 1 && right[i] > 1)
                res = max(res, left[i]+right[i]-1);
        }
        return n-res;

    }
};