class Solution {
public:
    int superEggDrop(int k, int n) {
        std::vector<int> dp(k+1,0);
        int move = 0;
        while(dp[k]<n){
            move++;
            for(int i=k;i>0;i--){
                dp[i] += dp[i-1]+1;
            }
        }
        return move;
    }
};