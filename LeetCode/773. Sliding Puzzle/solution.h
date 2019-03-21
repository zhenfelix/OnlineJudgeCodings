class Solution {
public:
    vector<int> dx{0,0,-1,1};
    vector<int> dy{-1,1,0,0};
    pair<int,int> find0(vector<vector<int>>& board){
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++)if(board[i][j]==0)return make_pair(i,j);
        }
        return make_pair(-1,-1);
    }
    vector<vector<int>> move(vector<vector<int>> board, int x, int y, int xx, int yy){
        board[x][y]=board[xx][yy];
        board[xx][yy]=0;
        return board;
    }
    vector<vector<vector<int>>> neighbor(vector<vector<int>>& board){
        vector<vector<vector<int>>> ans;
        pair<int,int> xy=find0(board);
        int x=xy.first;int y=xy.second;
        for(int k=0;k<4;k++){
            int xx=x+dx[k];
            int yy=y+dy[k];
            if(xx<0||yy<0||xx>=board.size()||yy>=board[0].size())continue;
            ans.push_back(move(board,x,y,xx,yy));
        }
        return ans;
    }
    int slidingPuzzle(vector<vector<int>>& board) {
        vector<vector<int>> init{{1,2,3},{4,5,0}};
        set<vector<vector<int>>> visited;
        queue<vector<vector<int>>> q;
        int step=0;
        q.push(init);
        visited.insert(init);
        while(!q.empty()){
            int n=q.size();
            while(n--){
                vector<vector<int>> b=q.front();
                q.pop();
                if(b==board)return step;
                vector<vector<vector<int>>> neis=neighbor(b);
                for(auto nei: neis){
                    if(visited.find(nei)==visited.end()){
                        q.push(nei);
                        visited.insert(nei);
                    }
                }
            }
            step++;
        }
        return -1;
    }
};

