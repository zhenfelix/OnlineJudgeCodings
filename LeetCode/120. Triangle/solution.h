class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n=triangle.size();
        vector<int> ans(n,0);
        for(auto row: triangle){
            vector<int> tmp_ans;
            
            for(int i=0;i<row.size();i++){
                int tmp=INT_MAX;
                if(i-1>=0&&i-1<row.size()-1)tmp=min(tmp,ans[i-1]);
                if(i>=0&&i<row.size()-1)tmp=min(tmp,ans[i]);
                // if(i+1>=0&&i+1<row.size()-1)tmp=min(tmp,ans[i+1]);
                if(tmp==INT_MAX)tmp=0;
                tmp_ans.push_back(tmp+row[i]);
            }
            ans=tmp_ans;
        }
        int tmp=INT_MAX;
        for(auto x: ans)tmp=min(tmp,x);
        return tmp;
    }
};