const string dirs[4] = {"East", "North", "West", "South"};

class Robot {
    bool _moved;
    int _pos, _n;
    vector<int> _x, _y, _d;
public:
    Robot(int width, int height) {
        _moved = false;
        _n = (width + height - 2) * 2;
        _pos = 0;
        _x = vector<int>(_n);
        _y = vector<int>(_n);
        _d = vector<int>(_n);
        
        int x = 0, y = 0, i = 0;
        _d[0] = 3;
        for (int j = 1; j < width; ++j) {
            x++, i++;
            _x[i] = x, _y[i] = y, _d[i] = 0;
        }
        for (int j = 1; j < height; ++j) {
            y++, i++;
            _x[i] = x, _y[i] = y, _d[i] = 1;
        }
        for (int j = 1; j < width; ++j) {
            i++, x--;
            _x[i] = x, _y[i] = y, _d[i] = 2;
        }
        for (int j = 1; j < height - 1; ++j) {
            i++, y--;
            _x[i] = x, _y[i] = y, _d[i] = 3;
        }
    }
    
    void move(int num) {
        _moved = true;
        _pos = (_pos + num) % _n;
    }
    
    vector<int> getPos() {
        return {_x[_pos], _y[_pos]};
    }
    
    string getDir() {
        if (!_moved)
            return dirs[0];
        
        return dirs[_d[_pos]];
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/cj4dO9/view/Mwspom/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。