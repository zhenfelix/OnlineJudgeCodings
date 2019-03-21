Ïclass Solution {
public:
    void dfs(vector<vector<int>> &A, int i, int j){
        int m=A.size(), n=A[0].size();
        if(i<0||j<0||i>=m||j>=n||A[i][j]!=1)return;
        A[i][j]=2;
        dfs(A,i+1,j);dfs(A,i-1,j);dfs(A,i,j+1);dfs(A,i,j-1);
        return;
    }
    void mark(vector<vector<int>> &A){
        int m=A.size(), n=A[0].size();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(A[i][j]==1){
                    dfs(A,i,j);
                    return;
                }
            }
        }
    }
    bool expand(vector<vector<int>>& A, int i, int j, int cc){
        int m=A.size(), n=A[0].size();
        if(i<0||j<0||i>=m||j>=n)return false;
        if(A[i][j]==0){
            A[i][j]=cc+1;
            return false;
        }
        return A[i][j]==1;
    } 
    int shortestBridge(vector<vector<int>>& A) {
        int m=A.size(), n=A[0].size();
        mark(A);
        for(int cc=2;;cc++){
            for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(A[i][j]==cc&&(expand(A,i,j-1,cc)||expand(A,i,j+1,cc)||expand(A,i-1,j,cc)||expand(A,i+1,j,cc)))return cc-2;
            }
        }
        }
    }
};

//C++ BFS Island Expansion + UF Bonus
//https://leetcode.com/problems/shortest-bridge/discuss/189293/C++-BFS-Island-Expansion-+-UF-Bonus