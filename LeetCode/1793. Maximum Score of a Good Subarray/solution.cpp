class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        for (int i = nums[k], l = k, r = k; i >= 1; --i) {
            while (l > 0 && nums[l - 1] >= i) --l;
            while (r + 1 < n && nums[r + 1] >= i) ++r;
            ans = max(ans, (r - l + 1) * i);
        }
        return ans;
    }
};


class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size(), res = 0;
        vector<int> left(n), right(n);
        for (int i = 0; i < n; i++){
            left[i] = i;
            right[i] = i;
        }
        vector<int> st;
        for (int i = 0; i < n; i++){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            if (st.empty())
                left[i] = 0;
            else
                left[i] = st.back()+1;
            // cout << left[i] << endl;
            st.push_back(i);
        }
        st.clear();
        for (int i = n-1; i >= 0; i--){
            while (!st.empty() && nums[st.back()] >= nums[i]){
                st.pop_back();
            }
            if (st.empty())
                right[i] = n-1;
            else
                right[i] = st.back()-1;
            // cout << right[i] << endl;
            st.push_back(i);
        }
        for (int i = 0; i < n; i++)
            if (left[i] <= k && k <= right[i])
                res = max(res, nums[i]*(right[i]-left[i]+1));
        return res;

    }
};