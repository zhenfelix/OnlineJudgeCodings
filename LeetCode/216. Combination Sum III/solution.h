class Solution {
public:
    void dfs(int idx, int k, int n, vector<int> &tmp, vector<vector<int>> &ans){
        if(k==0){
            if(n==0){
                ans.push_back(tmp);
            }
            return;
        }
        for(int i=idx+1;i<=9;i++){
                tmp.push_back(i);
                dfs(i,k-1,n-i,tmp,ans);
                tmp.pop_back();
            
        }
        return;
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> tmp;
        vector<vector<int>> ans;
        dfs(0,k,n,tmp,ans);
        return ans;
    }
};