class Solution {
public:
int minAbsoluteSumDiff(vector<int>& n1, vector<int>& n2) {
    long res = 0, gain = 0;
    set<int> s(begin(n1), end(n1));
    for (int i = 0; i < n1.size(); ++i) {
        long original = abs(n1[i] - n2[i]);
        res += original;
        // if (gain < original) 
        {
            auto it = s.lower_bound(n2[i]);
            if (it != end(s))
                gain = max(gain, original - abs(*it - n2[i]));
            if (it != begin(s))
                gain = max(gain, original - abs(*prev(it) - n2[i]));
        }
    }
    return (res - gain) % 1000000007;
}
};

class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), MOD = 1e9+7;
        long long tot = 0, res = LONG_MAX;
        set<int> st(nums1.begin(), nums1.end());
        for (int i = 0; i < n; i++){
            tot += abs(nums1[i]-nums2[i]);
        }
        for (int i = 0; i < n; i++){
            auto it = st.lower_bound(nums2[i]);
            int delta = INT_MAX;
            if (it != st.end())
                delta = min(delta, *it - nums2[i]);
            if (it != st.begin())
                delta = min(delta, nums2[i] - *(--it));
            res = min(res, tot+delta-abs(nums1[i]-nums2[i]));

        }
        return res%MOD;
    }
};