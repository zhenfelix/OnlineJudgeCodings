// class Solution {
// public:
//     vector<int> dx{0,0,-1,1};
//     vector<int> dy{-1,1,0,0};
//     bool check(int x, int y, vector<vector<int>>& grid){
//         if(x<0||y<0||x>=grid.size()||y>=grid[0].size())return false;
//         return grid[x][y]==1;
//     }
//     int orangesRotting(vector<vector<int>>& grid) {
//         int n=grid.size();
//         int m=grid[0].size();
//         int time=0;
//         queue<int> q;
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++)if(grid[i][j]==2)q.push(i*m+j);
//         }
//         q.push(-1);
//         while(!q.empty()){
//             int tmp=q.front();q.pop();
//             if(tmp==-1 && !q.empty()){
//                 time++;
//                 q.push(-1);
//             }
//             else if(tmp!=-1){
//                 int x=tmp/m;
//                 int y=tmp%m;
//                 for(int k=0;k<4;k++)if(check(x+dx[k], y+dy[k], grid)){
//                     grid[x+dx[k]][y+dy[k]]=2;
//                     q.push((x+dx[k])*m+(y+dy[k]));
//                 }
//             }
//         }
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++)if(grid[i][j]==1)return -1;
//         }
//         return time;
//     }
// };

