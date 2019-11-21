#include <cstdio>
#include <algorithm>
using namespace std;

class Solution {
public:
    int tilingRectangle(int n, int m) {
        
        int f[30][30];
        memset(f,1,sizeof(f));
        for(int i=0;i<=n;i++)f[i][0] = 0;
        for(int i=0;i<=m;i++)f[0][i] = 0;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                for(int k=1;k<=min(i,j);k++){
                    int i2 = i-k;
                    int j1 = j-k;
                    for(int i1=0;i1<=i2;i1++){
                        for(int j2=j1;j2<=j;j2++){
                            f[i][j] = min(f[i][j],f[i1][j2] + f[i2][j-j2] + f[i-i1][j1] + f[i2-i1][j2-j1] + 1);
                            if (i==19 && j == 17 && i2 == 5 && i1 == 3) {
                                printf("f[i][j]: %d i1: %d i2: %d j1: %d j2: %d\n", f[i][j],i1,i2,j1,j2);
                            }
                        }
                    }
                    
                }
            }
            
        }
//        for (int i = 0; i <= max(m,n); i++) {
//            for (int j = 0; j <= max(m,n); j++) {
//                printf("%d %d %d\n", i, j, f[i][j]);
//            }
//        }
        return f[n][m];
    }
};


int main(){
    int n, m;
//    freopen("input.txt", "r", stdin);
//    scanf("%d%d", &n, &m);
    Solution s;
//    for (int n = 1; n <= 100; n++) {
//        for (int m = 1; m <= n; m++) {
//            printf("%d %d: ", n, m);
//            printf("%d\n", s.tilingRectangle(n, m));
//        }
//    }
    n = 17;
    m = 16;
    printf("%d\n", s.tilingRectangle(n, m));
    return 0;
    
}
