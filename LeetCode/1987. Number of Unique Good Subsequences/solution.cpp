class Solution {
public:
    int numberOfUniqueGoodSubsequences(string s) {
        int n = s.size();
        int dp0 = 0, dp1 = 0, mod = 1e9 + 7, has0 = 0;
        for(int i = n-1; i >= 0; --i) {
            if(s[i] == '0') {
                has0 = 1;
                dp0 = (dp0 + dp1 + 1) % mod;
            } else {
                dp1 = (dp0 + dp1 + 1) % mod;
            }
        }
        return (dp1 + has0) % mod;
    }
};


作者：newhar
链接：https://leetcode-cn.com/problems/number-of-unique-good-subsequences/solution/dong-tai-gui-hua-jing-dian-ti-mu-de-bian-n4h3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。