class Solution {
public:
    string longestPalindrome(string s) {
        string ans="";
        int n=s.length();
        for(int i=0;i<n;i++){
            for(int j=0;(i-j>=0)&&(i+j<=n-1)&&(s[i-j]==s[i+j]);j++){
                if(2*j+1>ans.length())ans=s.substr(i-j,2*j+1);
            }
        }
        for(int i=0;i<n-1;i++){
            for(int j=1;(i-j+1>=0)&&(i+j<=n-1)&&(s[i-j+1]==s[i+j]);j++){
                if(2*j>ans.length())ans=s.substr(i-j+1,2*j);
            }
        }
        return ans;
    }
};