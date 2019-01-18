class Solution {
private:
    vector<string> mp{"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
public:
    void dfs(string &digits, vector<string> &ans, string &str, int idx){
        if(idx==digits.length()){
            ans.push_back(str);
            return;
        }
        string tmp=mp[digits[idx]-'2'];
        for(int i=0;i<tmp.size();i++){
            str[idx]=tmp[i];
            dfs(digits,ans,str,idx+1);
        }
        return;
    }
    vector<string> letterCombinations(string digits) {
        string str;
        vector<string> ans;
        if(digits.size()==0)return ans;
        for(int i=0;i<digits.size();i++)str+="0";
        dfs(digits,ans,str,0);
        return ans;
    }
};