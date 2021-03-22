// class Solution {
// public:
//     vector<int> dx{0,0,-1,1};
//     vector<int> dy{-1,1,0,0};
//     pair<int,int> find0(vector<vector<int>>& board){
//         for(int i=0;i<board.size();i++){
//             for(int j=0;j<board[0].size();j++)if(board[i][j]==0)return make_pair(i,j);
//         }
//         return make_pair(-1,-1);
//     }
//     vector<vector<int>> move(vector<vector<int>> board, int x, int y, int xx, int yy){
//         board[x][y]=board[xx][yy];
//         board[xx][yy]=0;
//         return board;
//     }
//     vector<vector<vector<int>>> neighbor(vector<vector<int>>& board){
//         vector<vector<vector<int>>> ans;
//         pair<int,int> xy=find0(board);
//         int x=xy.first;int y=xy.second;
//         for(int k=0;k<4;k++){
//             int xx=x+dx[k];
//             int yy=y+dy[k];
//             if(xx<0||yy<0||xx>=board.size()||yy>=board[0].size())continue;
//             ans.push_back(move(board,x,y,xx,yy));
//         }
//         return ans;
//     }
//     int slidingPuzzle(vector<vector<int>>& board) {
//         vector<vector<int>> init{{1,2,3},{4,5,0}};
//         set<vector<vector<int>>> visited;
//         queue<vector<vector<int>>> q;
//         int step=0;
//         q.push(init);
//         visited.insert(init);
//         while(!q.empty()){
//             int n=q.size();
//             while(n--){
//                 vector<vector<int>> b=q.front();
//                 q.pop();
//                 if(b==board)return step;
//                 vector<vector<vector<int>>> neis=neighbor(b);
//                 for(auto nei: neis){
//                     if(visited.find(nei)==visited.end()){
//                         q.push(nei);
//                         visited.insert(nei);
//                     }
//                 }
//             }
//             step++;
//         }
//         return -1;
//     }
// };

// class Solution {
// public:
//     int slidingPuzzle(vector<vector<int>>& b) {
//         string target="123450",
//         begin=to_string(b[0][0])+to_string(b[0][1])+to_string(b[0][2])
//              +to_string(b[1][0])+to_string(b[1][1])+to_string(b[1][2]);
//         vector<vector<int>> nextMoves{{1,3},{0,2,4},{1,5},{0,4},{1,3,5},{2,4}};
//         unordered_set<string> visited{begin};
//         queue<string> q; q.push(begin);
//         for (int depth=0; !q.empty(); ++depth){
//             int size=(int)q.size();
//             for (int i=0; i<size; ++i){
//                 auto curr=q.front(); q.pop();
//                 if (curr==target) return depth;
//                 int zero=(int)curr.find("0");
//                 for (auto next: nextMoves[zero]){
//                     auto candidate=curr;
//                     swap(candidate[zero],candidate[next]);
//                     if (visited.find(candidate)==visited.end()){
//                         visited.insert(candidate);
//                         q.push(candidate);
//                     }
//                 }
//             }
//         }
//         return -1;
//     }
// };

class Solution{
    public:
    int slidingPuzzle(vector<vector<int>>& board) {
    int m = 2, n = 3;
    string start = "";
    string target = "123450";
    // 将 2x3 的数组转化成字符串
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            start.push_back(board[i][j] + '0');
        }
    }
    // 记录一维字符串的相邻索引
    vector<vector<int>> neighbor = {
        { 1, 3 },
        { 0, 4, 2 },
        { 1, 5 },
        { 0, 4 },
        { 3, 1, 5 },
        { 4, 2 }
    };
    
    /******* BFS 算法框架开始 *******/
    queue<string> q;
    unordered_set<string> visited;
    q.push(start);
    visited.insert(start);
    
    int step = 0;
    while (!q.empty()) {
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            string cur = q.front(); q.pop();
            // 判断是否达到目标局面
            if (target == cur) {
                return step;
            }
            // 找到数字 0 的索引
            int idx = 0;
            for (; cur[idx] != '0'; idx++);
            // 将数字 0 和相邻的数字交换位置
            for (int adj : neighbor[idx]) {
                string new_board = cur;
                swap(new_board[adj], new_board[idx]);
                // 防止走回头路
                if (!visited.count(new_board)) {
                    q.push(new_board);
                    visited.insert(new_board);
                }
            }
        }
        step++;
    }
    return -1;
    /******* BFS 算法框架结束 *******/
}
};

