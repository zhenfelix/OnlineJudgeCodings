using ll = long long;

class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        vector<ll> presums = {0};
        for (auto c : candiesCount)
            presums.push_back(presums.back()+c);
        vector<bool> ans;
        for (auto q : queries){
            int t = q[0], day = q[1], cap = q[2];
            ll lo = presums[t]/cap, hi = presums[t+1];
            if ((lo <= day) && (day < hi))
                ans.push_back(true);
            else
                ans.push_back(false);
        }
        return ans;
    }
};