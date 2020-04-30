class Solution {
public:
    void upd(int &x,int y) {
        x = max(x, y);
    }
    int domino(int n, int m, vector<vector<int>>& broken) {
        int mp[10];
        int f[10][1<<8];
        for (int i=0;i<n;i++) {
            mp[i] = 0;
        }
        for (auto t:broken) {
            mp[t[0]] |= (1 << t[1]);
        }
        mp[n+1] = (1<<m) - 1;
        int ans = 0;
        memset(f,0,sizeof(f));
        //printf("%d %d\n",mp[0],mp[1]);
        for (int i=0;i<n;i++) {
            for (int j=0;j<(1<<m);j++) {
                if ((j & mp[i]) != mp[i]) {
                    continue;
                }
                if (i == n - 1) {
                    ans = max(ans, f[i][j]);
                }
                //printf("f[%d][%d]=%d\n",i,j,f[i][j]);
                for (int l=0;l<m-1;l++) {
                    if ((j & (1 << l)) == 0 && (j & (1 << (l + 1))) == 0) {
                        upd(f[i][j | (1 << l) | (1 << (l + 1))], f[i][j] + 1);
                    }  
                }
            }
            for (int j=0;j<(1<<m);j++) {
                if ((j & mp[i]) != mp[i]) {
                    continue;
                }
                for (int l=0;l<(1<<m);l++) {
                    if ((j & l) == 0 && (mp[i+1] & l) == 0) {
                        upd(f[i+1][mp[i+1] | l], f[i][j] + __builtin_popcount(l));
                    }
                }
            }
        }
        return ans;
    }
};