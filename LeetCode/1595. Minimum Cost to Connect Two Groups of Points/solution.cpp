class Solution {
public:
    int m,n;
    int memo[13][1<<12][2];
    int connectTwoGroups(vector<vector<int>>& cost) {
        m=cost.size();
        n=cost[0].size();
        memset(memo,-1,sizeof(memo));
        return dfs(cost,0,0,0);
    }
    
    int dfs(vector<vector<int>>& cost, int idx ,int used, int part){
        if(part==0 && idx==m){
            if(memo[idx][used][part]!=-1) return memo[idx][used][part];
            int res=dfs(cost,0,used,1);
            return  memo[idx][used][part]= res;
        }
        if(part==1 && idx==n){
            return 0;
        }
        
        if(memo[idx][used][part] !=-1) return memo[idx][used][part] ;
        int res=INT_MAX;
        if(part==0){
            for(int i=0;i<n;i++){
            
                int next=dfs(cost,idx+1,used|(1<<i),part);
                if(next==INT_MAX) continue;
                res=min(res,cost[idx][i]+next);
            
            }
        }else{
            if((used&(1<<idx)) !=0) res=dfs(cost,idx+1,used,1);
            else {
                for(int i=0;i<m;i++){
                    int next=dfs(cost,idx+1,used,1);
                    if(next==INT_MAX) continue;
                    res=min(res,cost[i][idx]+next);
                }
            }
        }
        
        
        return memo[idx][used][part] = res;
        
    }
};