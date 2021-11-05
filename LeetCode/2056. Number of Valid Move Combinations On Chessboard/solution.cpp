const int d[8][2] = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};

class Solution {
    vector<vector<int>> positions, possible;
    int n, ans = 0;
    vector<int> direction, step, xinit, yinit;
    
    bool valid(int x, int y) {
        return x >= 1 && x <= 8 && y >= 1 && y <= 8;
    }
    
    void check() {
        vector<int> x(xinit), y(yinit), s(step);
        bool go = true;
        while (go) {
            go = false;
            for (int i = 0; i < n; ++i) {
                if (s[i] > 0) {
                    s[i]--;
                    x[i] += d[direction[i]][0];
                    y[i] += d[direction[i]][1];
                }
                if (s[i])
                    go = true;
            }
            for (int i = 0; i < n; ++i)
                for (int j = i + 1; j < n; ++j)
                    if (x[i] == x[j] && y[i] == y[j])
                        return;
        }
        ans++;
    }
    
    void dfs(int i) {        
        if (i == n) {
            check();
        } else {
            direction.push_back(0);
            step.push_back(0);
            dfs(i + 1);
            direction.pop_back();
            step.pop_back();
            
            for (int j = 1; j < 8; ++j) {
                for (int k : possible[i]) {
                    int x = positions[i][0] + d[k][0] * j, y = positions[i][1] + d[k][1] * j;
                    if (valid(x, y)) {
                        direction.push_back(k);
                        step.push_back(j);
                        dfs(i + 1);
                        direction.pop_back();
                        step.pop_back();
                    }
                }
            }
        }
    }
public:
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        n = pieces.size();
        possible = vector<vector<int>>(n);
        this->positions = positions;
        xinit = vector<int>(n), yinit = vector<int>(n);
        for (int i = 0; i < n; ++i) {
            xinit[i] = positions[i][0], yinit[i] = positions[i][1];
            if (pieces[i] != "rook") {
                possible[i].emplace_back(1);
                possible[i].emplace_back(3);
                possible[i].emplace_back(5);
                possible[i].emplace_back(7);
            }
            if (pieces[i] != "bishop") {
                possible[i].emplace_back(0);
                possible[i].emplace_back(2);
                possible[i].emplace_back(4);
                possible[i].emplace_back(6);
            }
        }
        
        dfs(0);
        
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/HveixS/view/XH6soo/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。