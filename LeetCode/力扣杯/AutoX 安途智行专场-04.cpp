using pii = pair<int,int>;
using ll = long long;


class Solution {
    struct Point
    {
        int x;
        int y;
        Point(int a, int b): x(a), y(b){};
    };

    bool onseg(Point p, Point q, Point r)
    {
        if (q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
            q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y)) return true;
        return false;
    }

    int angle(Point p, Point q, Point r)
    {
        ll val = (ll) (q.y - p.y) * (r.x - q.x) -
                (ll) (q.x - p.x) * (r.y - q.y);

        if (val == 0) return 0; 

        return (val > 0)? 1: 2; 
    }

    bool ss(Point p1, Point q1, Point p2, Point q2)
    {

        int o1 = angle(p1, q1, p2);
        int o2 = angle(p1, q1, q2);
        int o3 = angle(p2, q2, p1);
        int o4 = angle(p2, q2, q1);

        if (o1 != o2 && o3 != o4)
            return true;

        if (o1 == 0 && onseg(p1, p2, q1)) return true;

        if (o2 == 0 && onseg(p1, q2, q1)) return true;

        if (o3 == 0 && onseg(p2, p1, q2)) return true;

        if (o4 == 0 && onseg(p2, q1, q2)) return true;

        return false; 
    }

    bool cc(Point p, Point q, int pr, int qr){
        ll x = p.x-q.x, y = p.y-q.y, r1 = qr+pr, r2 = qr-pr;
        if (x*x+y*y > r1*r1) return false;
        if (x*x+y*y < r2*r2) return false;
        return true;
    }

    bool cs(Point c, ll r, Point sa, Point sb){
        ll ax = sa.x-c.x, ay = sa.y-c.y, bx = sb.x-c.x, by = sb.y-c.y;
        bool a = ax*ax+ay*ay < r*r;
        bool b = bx*bx+by*by < r*r;
        // if (r == 1875 && sa.x == 692 && sa.y == 3820 && sb.x == 1201 && sb.y == 7377) cout << "found" << c.x << c.y << endl;
        if (a&b) return false;
        if (a^b) return true;
        ll x = sa.x-sb.x, y = sa.y-sb.y;
        ll p = x*by-y*bx;
        ll q = x*x+y*y;
        // cout << p << " " << q << " " << r << endl;
        // if (p*p > q*r*r) return false;
        double tmp = (double)abs(p)/r;
        if (tmp*tmp > (double)abs(q)) return false;
        ll angle1 = -bx*x-by*y;
        ll angle2 = ax*x+ay*y;
        // if (r == 1875 && sa.x == 692 && sa.y == 3820 && sb.x == 1201 && sb.y == 7377) cout << angle1 << " " << angle2 << endl;

        if ((angle1 >= 0) && (angle2 >= 0)) return true;
        return false;
    }

    vector<int> parent;
    int find(int cur){
        if (parent[cur] != cur) parent[cur] = find(parent[cur]);
        return parent[cur];
    }
    void connect(int u, int v){
        int ru = find(u), rv = find(v);
        if (ru != rv) parent[ru] = rv;
        return;
    }
public:
    vector<bool> antPass(vector<vector<int>>& geometry, vector<vector<int>>& path) {
        int n = geometry.size(), m = path.size();
        vector<vector<bool>> mat(n, vector<bool>(n, false));
        parent.resize(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++){
            for (int j = i+1; j < n; j++){
                auto u = geometry[i];
                auto v = geometry[j];
                int tu = u.size(), tv = v.size();
                if (tu+tv == 8){
                    if (ss(Point(u[0],u[1]), Point(u[2],u[3]), Point(v[0],v[1]), Point(v[2],v[3]))){
                        connect(i,j);
                        // cout << i << " " << j << endl;
                    }
                }
                else if (tu+tv == 6){
                    if (cc(Point(u[0],u[1]),Point(v[0],v[1]),u[2],v[2])){
                        connect(i,j);
                        // cout << i << " " << j << endl;
                    }
                }
                else{
                    if (tu == 4) swap(u,v);
                    if (cs(Point(u[0],u[1]),u[2],Point(v[0],v[1]),Point(v[2],v[3]))){
                        connect(i,j);
                        // cout << i << " " << j << endl;
                    }
                }
            }
        }
        vector<bool> res;
        for (auto &p : path){
            int u = p[0], v = p[1];
            if (find(u) == find(v)) res.push_back(true);
            else res.push_back(false);
        }
        return res;
    }
};
