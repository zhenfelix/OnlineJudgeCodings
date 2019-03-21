// class Solution {
// public:
//     int dx[4]={0,0,-1,1};
//     int dy[4]={-1,1,0,0};
//     void dfs(vector<vector<bool>> &visited, vector<vector<int>>& image, int x, int y, int newColor, int oldColor){
//         if(x<0||y<0||x>=image.size()||y>=image[0].size())return;
//         if(!visited[x][y] && image[x][y]==oldColor){
//             int oldColor=image[x][y];
//         visited[x][y]=true;
//         image[x][y]=newColor;
//         for(int k=0;k<4;k++){
//             int xx=x+dx[k];
//             int yy=y+dy[k];
//             dfs(visited,image,xx,yy,newColor,oldColor);
//         }
//         }
//         return;
//     }
//     vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
//         int oldColor=image[sr][sc];
//         vector<vector<bool>> visited(image.size(),vector<bool>(image[0].size(), false));
//         dfs(visited,image,sr,sc,newColor,oldColor);
//         return image;
//     }
// };

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (image[sr][sc]==newColor) {
            return image;
        }
        fill(image,sr,sc,image[sr][sc],newColor);
        return image;
    }
private:
    void fill(vector<vector<int>>& image, int row, int col, int color, int newColor) {
        if (row<0 | row>=image.size() || col<0 || col>=image[0].size() || image[row][col]!=color) {
            return;
        }
        image[row][col]=newColor;
        fill(image,row+1,col,color,newColor);
        fill(image,row-1,col,color,newColor);
        fill(image,row,col+1,color,newColor);
        fill(image,row,col-1,color,newColor);
    }
};