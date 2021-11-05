A star剪枝效果并不明显

using pii = pair<int, int>;
using tiii = tuple<int, int, int>;
vector<pii> dxy = {{2, 1}, {1, 2}, {-2, 1}, {-1, 2}, {2, -1}, {1, -2}, {-2, -1}, {-1, -2}};
class Solution
{
public:
    int minKnightMoves(int x, int y)
    {
        auto h = [&](int xx, int yy)
        {
            return (abs(xx - x) + abs(yy - y)) / 3;
        };
        auto hash = [](int xx, int yy)
        {
            return ((xx + 1000) * 1000 + (yy + 1000));
        };
        // function<pair<int,int>(int)> rhash = [](int k){
        //     return make_pair(k/1000,k%1000);
        // };
        priority_queue<tiii, vector<tiii>, greater<>> pq;
        pq.push({h(0, 0), 0, 0});
        unordered_map<int, int> gscore;
        gscore[hash(0, 0)] = 0;
        while (!pq.empty())
        {
            auto [f, xx, yy] = pq.top();
            pq.pop();
            if (gscore[hash(xx, yy)] + h(xx, yy) < f)
                continue;
            // cout << xx << " " << yy << endl;
            if (xx == x && yy == y)
                return f;
            for (auto [dx, dy] : dxy)
            {
                dx += xx;
                dy += yy;
                int g = gscore[hash(xx, yy)] + 1;
                if (!gscore.count(hash(dx, dy)) || g < gscore[hash(dx, dy)])
                {
                    gscore[hash(dx, dy)] = g;
                    pq.push({g + h(dx, dy), dx, dy});
                }
            }
        }
        return -1;
    }
};


bfs利用方向性，对称性和边界性联合剪枝
尤其是方向性，我们只需要考虑落点在连线附近的
将visited替换成unordered_map可以实现线性复杂度

class Solution
{
public:
    int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
    int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

    int minKnightMoves(int x, int y)
    {
        int steps = 0;
        queue<pair<int, int>> q;
        x = abs(x);
        y = abs(y);
        if (y > x)
            swap(x,y);
        x = x + 2;
        y = y + 2;
        vector<vector<int>> visited(x + 4, vector<int>(y + 4, -1));
        q.push({2, 2});
        visited[2][2] = 0;
        while (!q.empty())
        {
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                // check all the node in queue
                int curX = q.front().first;
                int curY = q.front().second;
                q.pop();
                // cout << curX << " " << curY << " " << steps << endl;
                if (curX == x && curY == y)
                {
                    return steps;
                }
                for (int j = 0; j < 8; j++)
                {
                    int a = curX + dx[j];
                    int b = curY + dy[j];
                    int by = x == 2 ? b : (y-2)*(a-2)/(x-2)+2;
                    // if (a >= 0 && a <= x + 2 && b >= 0 && b <= y + 2 && !visited[a][b])
                    if (a >= 0 && a <= x + 2 && b >= 0 && b <= y + 2 && b >= by-4 && b <= by+4 && visited[a][b] == -1)
                    {
                        q.push({a, b});
                        visited[a][b] = steps+1;
                    }
                }
            }
            // for (int i = 0; i < visited.size(); i++){
            //     for (int j = 0; j < visited[0].size(); j++){
            //         printf("%5d ", visited[i][j]);
            //     }
            //     printf("\n");
            // }
            // printf("\n");
            steps++;
        }
        return -1;
    }
};