class Solution {
public:
    vector<int> dx{0,0,-1,1};
    vector<int> dy{-1,1,0,0};
    bool search(vector<vector<char>>& board, vector<vector<bool>>& visit, string &word, int i, int j, int idx){
        // if(idx==word.length())return true;
        if(board[i][j]!=word[idx])return false;
        if(idx==word.length()-1)return true;
        visit[i][j]=true;
        for(int k=0;k<4;k++){
            int ii=i+dx[k],jj=j+dy[k];
            if(ii>=0&&ii<board.size()&&jj>=0&&jj<board[0].size()&&(!visit[ii][jj]))if(search(board,visit,word,ii,jj,idx+1))return true;
        }
        visit[i][j]=false;
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int m=board.size();
        if(m==0)return false;
        int n=board[0].size();
        vector<vector<bool>> visit(m, vector<bool>(n,false));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(search(board,visit,word,i,j,0))return true;
            }
        }
        return false;
    }
};


// class Solution {
// private:
//     bool dfs(vector<vector<char>>& board, int row, int col, const string &word, int start, int M, int N, int sLen)
//     {
//         char curC;
//         bool res = false;
//         if( (curC = board[row][col]) != word[start]) return false;
//         if(start==sLen-1) return true;
//         board[row][col] = '*';
//         if(row>0) res = dfs(board, row-1, col, word, start+1, M, N, sLen);
//         if(!res && row < M-1) res = dfs(board, row+1, col, word, start+1, M, N, sLen);
//         if(!res && col > 0)   res = dfs(board, row, col-1, word, start+1, M, N, sLen);
//         if(!res && col < N-1) res = dfs(board,  row, col+1, word, start+1, M, N, sLen);
//         board[row][col] = curC;
//         return res;
//     }
    
// public:
//     bool exist(vector<vector<char>>& board, string word) {
//         int M,N,i,j,sLen = word.size();
//         if( (M=board.size()) && (N=board[0].size()) && sLen)
//         {
//             for(i=0; i<M; ++i)
//                 for(j=0; j<N; ++j)
//                     if(dfs(board, i, j, word, 0, M, N, sLen)) return true;
//         }
//         return false;
//     }
// };