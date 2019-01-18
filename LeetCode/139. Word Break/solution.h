class Solution {
public:
    bool helper(string &s, vector<bool> &dp, unordered_set<string> &dict){
        for(int i=1;i<=s.length();i++){
            for(int j=i-1;j>=0;j--){
                if(dp[j]&&dict.find(s.substr(j,i-j))!=dict.end()){
                    dp[i]=true;
                    break;//optimization
                }
            }
        }
        return dp.back();
    }
    bool wordBreak(string s, vector<string>& wordDict) {
        int n=s.length();
        vector<bool> dp(n+1,false);
        unordered_set<string> dict;
        dp[0]=true;
        for(int i=0;i<wordDict.size();i++)dict.insert(wordDict[i]);
        return helper(s,dp,dict);
    }
};