// class Solution {
    
// public:
//     bool isok(vector<vector<int>> &cc, int i, int j, int k){
//         int len=INT_MAX;
//         for(int ii=0;ii<26;ii++){
//             int tmp=cc[j][ii]-cc[i][ii];
//             if(tmp>0)len=min(len,tmp);
//             if(len<k)return false;
//         }
//         return true;
//     }
//     void helper(int &ans, vector<vector<int>> &cc, int i, int j, int k){
//         if(i>=j)return;
//         if(isok(cc,i,j,k))ans=max(ans,j-i);
//         helper(ans,cc,i+1,j,k);
//         helper(ans,cc,i,j-1,k);
//         return;
//     }
//     int longestSubstring(string s, int k) {
//         int len=s.length();
//         vector<int> tmp(26,0);
//         vector<vector<int>> cc;
//         cc.push_back(tmp);
//         for(int i=0;i<len;i++){
//             tmp[s[i]-'a']++;
//             cc.push_back(tmp);
//         }
//         int ans=0;
//         helper(ans,cc,0,len,k);
//         return ans;
//     }
// };
//brute force time excedeed

class Solution {
    
public:
    
    int longestSubstring(string s, int k) {
        vector<int> mp(26,0);
        for(auto ch: s)mp[ch-'a']++;
        int idx=0;
        while(idx<s.length()&&mp[s[idx]-'a']>=k)idx++;
        if(idx==s.length())return s.length();
        return max(longestSubstring(s.substr(0,idx),k),longestSubstring(s.substr(idx+1),k));
    }
};