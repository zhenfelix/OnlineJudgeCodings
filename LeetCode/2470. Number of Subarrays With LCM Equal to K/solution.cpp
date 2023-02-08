# LC2447 2447. Number of Subarrays With GCD Equal to K


class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> q(n, vector<int>(2));
        int l,r;
        r = 0;
        int pre = -1, ans = 0;
        for (int i = 0; i < n; i++){
            int v = nums[i];
            if (k%v) {
                pre = i;
                r = 0;
                continue;
            }
            v = k/v;
            q[r][0] = i;
            q[r][1] = v;
            r++;
            l = 0;
            for (int j = 0; j < r; j++){
                q[j][1] = __gcd(q[j][1],v);
                if (q[l][1] != q[j][1]) l++;
                q[l][0] = q[j][0];
                q[l][1] = q[j][1];
                
            }
            r = l+1;
            if (q[0][1] == 1) ans += q[0][0]-pre;
        }
        return ans;
    }
};