class Solution
{
public:
    bool isPathCrossing(string path)
    {
        vector<int> dx(256,0), dy(256,0);
        dx['E'] = 1, dx['W'] = -1, dy['N'] = -1, dy['S'] = 1;
        set<pair<int,int>> visited;
        visited.insert({0,0});
        int x=0, y=0;
        for(auto ch: path){
            x += dx[ch];
            y += dy[ch];
            if(visited.find({x,y})!=visited.end())return true;
            visited.insert({x,y});
        }
        return false;

    }
};