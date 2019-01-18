class Solution {
public:
    int numTrees(int n) {
        if(n==1||n==0)return 1;
        vector<int> ans(n+1,1);
        for(int i=2;i<=n;i++){
            ans[i]=0;
            for(int j=1;j<=i;j++){
                ans[i]+=(ans[j-1]*ans[i-j]);
            }
        }
        return ans.back();
    }
};

// class Solution {
// public:
//     int numTrees(int n) {
//         long C = 1;
//     for (int i = 0; i < n; ++i) {
//       C = C * 2 * (2 * i + 1) / (i + 2);
//     }
//     return (int) C;        
//     }
// };