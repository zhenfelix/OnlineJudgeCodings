int f[1005][1005][2] = {0};
class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int mod = 1e9 + 7;
        
        for(int i = 0; i <= zero; ++i)
            f[i][0][0] = (i <= limit), f[i][0][1] = 0;
        for(int j = 0; j <= one; ++j) 
            f[0][j][0] = 0, f[0][j][1] = (j <= limit);
        
        int sum1[one + 1];
        for(int j = 0; j <= one; ++j) sum1[j] = f[0][j][1];
        
        for(int i = 1; i <= zero; ++i) {
            for(int j = 1, sum0 = f[i][0][0]; j <= one; ++j) {
                f[i][j][0] = sum1[j];
                f[i][j][1] = sum0;
                
                sum0 = (sum0 + f[i][j][0]) % mod;
                if(j - limit >= 0) 
                    sum0 = (sum0 + mod - f[i][j-limit][0]) % mod;
                
                sum1[j] = (sum1[j] + f[i][j][1]) % mod;
                if(i - limit >= 0) 
                    sum1[j] = (sum1[j] + mod - f[i-limit][j][1]) % mod;
            }
        }
        
        return (f[zero][one][0] + f[zero][one][1]) % mod;
    }
};


作者：newhar
链接：https://leetcode.cn/circle/discuss/SZyTo4/view/mv9LwV/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。