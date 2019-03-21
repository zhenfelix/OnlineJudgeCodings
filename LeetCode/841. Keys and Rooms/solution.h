class Solution {
public:
    void dfs(vector<bool> &visited, vector<vector<int>>& rooms, int x){
        for(auto y: rooms[x]){
            if(!visited[y]){
                visited[y]=true;
                dfs(visited, rooms, y);
                }
        }
        return;
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n=rooms.size();
        vector<bool> visited(n,false);
        visited[0]=true;
        dfs(visited, rooms, 0);
        for(auto v: visited)if(v==false)return false;
        return true;
    }
};