using pii = pair<int,int>;
using ll = long long;
class Solution {
public:
    vector<double> honeyQuotes(vector<vector<int>>& handle) {
        vector<double> ans;
        ll s = 0, s2 = 0;
        int cnt = 0;
        for (auto h : handle){
            if (h[0] <= 2){
                if (h[0] == 1){
                    s += h[1];
                    s2 += h[1]*h[1];
                    cnt += 1;
                }
                else{
                    s -= h[1];
                    s2 -= h[1]*h[1];
                    cnt -= 1;
                }
            }
            else{
                if (cnt <= 0){
                    ans.push_back(-1);
                }
                else{
                    double e = (double)s/cnt;
                    if (h[0] == 3){
                        ans.push_back(e);
                    }
                    else{

                        ans.push_back((double)s2/cnt-e*e);
                    }
                }
                
            }
        }
        return ans;
    }
};