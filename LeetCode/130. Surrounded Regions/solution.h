// class Solution {
// public:
//     bool dfs(vector<vector<char>> &board, int i, int j){
//         if(i<0||j<0||i>=board.size()||j>=board[0].size())return false;
        
//         if(board[i][j]=='O'){
//             board[i][j]='Y';
//             bool f1=dfs(board,i+1,j);
//             bool f2=dfs(board,i-1,j);
//             bool f3=dfs(board,i,j+1);
//             bool f4=dfs(board,i,j-1);
//             return f1&&f2&&f3&&f4;
//         }
//         return true;
//     }
//     void flip(vector<vector<char>> &board, int i, int j){
//         if(board[i][j]=='X')return;
//         board[i][j]='X';
//         flip(board,i+1,j) ; flip(board,i-1,j) ; flip(board,i,j+1) ; flip(board,i,j-1);
//         return;
//     }
//     void solve(vector<vector<char>>& board) {
//         for(int i=0;i<board.size();i++){
//             for(int j=0;j<board[0].size();j++){
//                 if(board[i][j]=='O'){
//                    if(dfs(board,i,j))flip(board,i,j);
//                 }
//                 if(board[i][j]=='Y'){
//                     board[i][j]='O';
//                 }
//             }
//         }
//         return;
//     }
// };


class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int i,j;
        int row=board.size();
        if(!row)
            return;
        int col=board[0].size();

        for(i=0;i<row;i++){
            check(board,i,0,row,col);
            if(col>1)
                check(board,i,col-1,row,col);
        }
        for(j=1;j+1<col;j++){
            check(board,0,j,row,col);
            if(row>1)
                check(board,row-1,j,row,col);
        }
        for(i=0;i<row;i++)
            for(j=0;j<col;j++)
                if(board[i][j]=='O')
                    board[i][j]='X';
        for(i=0;i<row;i++)
            for(j=0;j<col;j++)
                if(board[i][j]=='1')
                    board[i][j]='O';
    }
    void check(vector<vector<char> >&vec,int i,int j,int row,int col){
        if(vec[i][j]=='O'){
            vec[i][j]='1';
            if(i>1)
                check(vec,i-1,j,row,col);
            if(j>1)
                check(vec,i,j-1,row,col);
            if(i+1<row)
                check(vec,i+1,j,row,col);
            if(j+1<col)
                check(vec,i,j+1,row,col);
        }
    }
};