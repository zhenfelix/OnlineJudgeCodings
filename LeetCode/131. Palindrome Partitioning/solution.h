// class Solution {
// public:
//     bool ispd(string &s, int i, int j){
//         while(i<j){
//             if(s[i]!=s[j])return false;
//             i++;j--;
//         }
//         return true;
//     }
//     void backtrack(string &s, int start, vector<vector<string>> &ans, vector<string> &tmp){
//         if(start==s.length()){
//             ans.push_back(tmp);
//             return;
//         }
//         for(int i=start;i<s.length();i++){
//             if(ispd(s,start,i)){
//                 tmp.push_back(s.substr(start,i-start+1));
//                 backtrack(s,i+1,ans,tmp);
//                 tmp.pop_back();
//             }
//         }
//         return;
//     }
//     vector<vector<string>> partition(string s) {
//         vector<vector<string>> ans;
//         vector<string> tmp;
//         backtrack(s,0,ans,tmp);
//         return ans;
//     }
// };


class Solution {
public:
    vector<vector<string>> partition(string s) {
        int sz = s.size();
        vector<vector<bool>> pal(sz, vector<bool>(sz, false));
        for (int i = sz-1; i >= 0; --i)
            for (int j = i; j < sz; ++j) {
                if (s[i] == s[j] && (j-i<2 || pal[i+1][j-1]))//这里有些细节，即为什么不用检查i+1越界
                    pal[i][j] = true;
            }
        
        vector<vector<string>> res;
        vector<string> temp;
        backtrack(res, temp, 0, sz-1, pal, s);
        return res;
    }
private:
    void backtrack(vector<vector<string>> &res, vector<string> &temp, int beg, const int& end, const vector<vector<bool>> &pal, const string& s) {
        if (beg > end) {
            res.push_back(temp);
            return;
        }
        
        for (int j = beg; j <= end; ++j){
            if (pal[beg][j]) {
                temp.push_back(s.substr(beg, j-beg+1));
                backtrack(res, temp, j+1, end, pal,s );
                temp.pop_back();
            }
        }
            
    }
};//DP+backtrack