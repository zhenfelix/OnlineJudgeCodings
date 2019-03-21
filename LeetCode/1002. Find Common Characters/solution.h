class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        int n=A.size();
        vector<vector<int>> CharNums(n,vector<int>(26,0));
        vector<string> ans;
        
        for(int i=0;i<n;i++){
            for(auto &ch: A[i])CharNums[i][ch-'a']++;
        }
        for(int j=0;j<26;j++){
            int cc=INT_MAX;
            for(int i=0;i<n;i++){
                cc=min(cc,CharNums[i][j]);
            }
            while(cc--)ans.push_back(string(1,'a'+j));
        }
        return ans;
    }
};