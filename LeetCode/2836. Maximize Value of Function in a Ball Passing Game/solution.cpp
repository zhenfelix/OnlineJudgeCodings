using ll = long long;
const int N = 1e5 + 10;
const int L = 35;
int nxt[N][L];
ll val[N][L];
class Solution {
public:
    long long getMaxFunctionValue(vector<int>& a, long long k) {
        int n = a.size();
        for(int i=0; i<n; ++i){
            nxt[i][0] = a[i];
            val[i][0] = a[i];
        }
        for(int j=1; j<L; ++j){
            for(int i=0; i<n; ++i){
                nxt[i][j] = nxt[nxt[i][j-1]][j-1];
                val[i][j] = val[nxt[i][j-1]][j-1] + val[i][j-1];
            }
        }
        ll ans = 0;
        for(int i=0; i<n; ++i){
            ll cur = i;
            int u = i;
            for(int j=0; j<L; ++j){
                if(k >> j & 1){
                    cur += val[u][j];
                    u = nxt[u][j];
                }
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};


