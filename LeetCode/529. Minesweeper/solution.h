class Solution {
    vector<int> dx{-1,-1,-1,0,0,1,1,1};
    vector<int> dy{-1,0,1,-1,1,-1,0,1};
public:
    void dfs(vector<vector<char>>& board, int x, int y){
        int m=board.size();
        int n=board[0].size();
        // if(board[x][y]=='M')return 1;
        // if(board[x][y]!='E')return 0;
        int sums=0;
        board[x][y]='B';
        for(int k=0;k<8;k++){
            int xx=x+dx[k], yy=y+dy[k];
            if(xx>=0&&xx<m&&yy>=0&&yy<n&&board[xx][yy]=='M')sums+=1;
        }
        if(sums>0){board[x][y]='0'+sums;return;}
        
        for(int k=0;k<8;k++){
            int xx=x+dx[k], yy=y+dy[k];
            if(xx>=0&&xx<m&&yy>=0&&yy<n&&(board[xx][yy]=='E'))dfs(board,xx,yy);
        }
        
        return;
    }
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int x=click[0],y=click[1];
        int m=board.size();
        int n=board[0].size();
        if(board[x][y]=='M'){board[x][y]='X';return board;}
        // vector<vector<bool>> visited(m, vector<bool>(n,false));
        dfs(board,x,y);
        return board;
    }
};