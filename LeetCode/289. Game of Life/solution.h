// class Solution {
// public:
//     void gameOfLife(vector<vector<int>>& board) {
//         int m=board.size(),n=board[0].size();
//         vector<int> dx{1,1,1,0,0,-1,-1,-1},dy{1,0,-1,1,-1,1,0,-1};
//         for(int i=0;i<m;i++){
//             for(int j=0;j<n;j++){
//                 int cc=0;
//                 for(int k=0;k<8;k++)if(i+dx[k]>=0&&i+dx[k]<m&&j+dy[k]>=0&&j+dy[k]<n)if(board[i+dx[k]][j+dy[k]]==1||board[i+dx[k]][j+dy[k]]==-2)cc++;
//                 if((cc>3||cc<2)&&board[i][j]==1)board[i][j]=-2;
//                 else if(cc==3&&board[i][j]==0)board[i][j]=-1;
//                 else;
//             }
//         }
//         for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(board[i][j]<0)board[i][j]+=2;
//         return;
//     }
// };

class Solution {
public:
    vector<int> dir={-1,0,1};
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size(), n = m ? board[0].size() : 0;
        for (int i=0; i<m; ++i) {
            for (int j=0; j<n; ++j) {
                int count = 0;
                for (int I=max(i-1, 0); I<min(i+2, m); ++I)//本位也参与了计数
                    for (int J=max(j-1, 0); J<min(j+2, n); ++J)//直接控制上限与下限，并变换方向；
                        count += board[I][J] & 1;//只有int中最后1bit参与运算，状态位被忽略
                if (count == 3 || count - board[i][j] == 3)//包括两种情况：1.本位为1，周围有2个；2.本位为0，周围有三个；3.本位为1，周围有三个；
                    board[i][j] |= 2;//下一回合置为1
            }
        }
        for (int i=0; i<m; ++i)
            for (int j=0; j<n; ++j)
                board[i][j] >>= 1;
    }
};