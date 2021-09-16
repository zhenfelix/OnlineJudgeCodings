class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size()+1, tot = 0, cur = 0;
        for (int i = 1; i <= n; i++)
            tot ^= i;
        for (int i = 0; i < n/2; i++)
            cur ^= encoded[i*2+1];
        vector<int> ans(n);
        ans[0] = tot^cur;
        for (int i = 0; i < n-1; i++)
            ans[i+1] = ans[i]^encoded[i];
        return ans;
    }
};