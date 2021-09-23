// using pp = pair<int,int>;
// const int pb = 1e5+3;

// vector<pp> dirs = {{-1,0},{1,0},{0,-1},{0,1}};
// string sp = "WESN";

// class Solution {
// public:
//     bool isPathCrossing(string path) {
//         map<char,int> mp;
//         for (int i = 0; i < 4; i++)
//             mp[sp[i]] = i;
//         int x = 0, y = 0;
//         unordered_set<int> seen;
//         seen.insert(x*pb+y);
//         for (auto ch : path){
//             int idx = mp[ch];
//             auto [dx,dy] = dirs[idx];
//             x += dx; y += dy;
//             if (seen.find(x*pb+y) != seen.end())
//                 return true;
//             seen.insert(x*pb+y);
//         }
//         return false;

//     }
// };


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