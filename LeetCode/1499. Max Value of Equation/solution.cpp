using pp = pair<int,int>;
const int inf = 0x3f3f3f3f;
const int maxn = 1e5+5;

int x[maxn], xy[maxn];

class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        int res = -inf; 
        int n = points.size();
        for (int left = 0, right = -1, i = 0; i < n; i++){
            int x2 = points[i][0], y2 = points[i][1];
            while (left <= right && x[left] < x2-k)
                left++;
            if (left <= right){
                // cout << x1 << " " << xy1 << " " << x2 << " " << y2 << endl;
                res = max(res, xy[left]+x2+y2);
            }
            
            while (left <= right && xy[right] <= y2-x2)
                right--;
            right++;
            x[right] = x2;
            xy[right] = y2-x2;
        }
        return res;
    }
};


class Solution {
public:

    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        deque<pair<int, int>> dq;
        int ans = INT_MIN;
        for (auto& j : points) {
            while (!dq.empty() && j[0] - dq.front().second > k) dq.pop_front();
            if (!dq.empty()) ans = max(ans, j[0] + j[1] + dq.front().first);
            while (!dq.empty() && dq.back().first <= j[1] - j[0]) dq.pop_back();
            dq.push_back({j[1] - j[0], j[0]});
        }
        return ans;
    }
};



using pp = pair<int,int>;
const int inf = 0x3f3f3f3f;
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        int res = -inf; 
        int n = points.size();
        deque<pp> q;
        for (int i = 0; i < n; i++){
            int x2 = points[i][0], y2 = points[i][1];
            while (!q.empty() && q.front().second < x2-k)
                q.pop_front();
            if (!q.empty()){
                auto [xy1, x1] = q.front();
                // cout << x1 << " " << xy1 << " " << x2 << " " << y2 << endl;
                res = max(res, xy1+x2+y2);
            }
            
            while (!q.empty() && q.back().first <= y2-x2)
                q.pop_back();
            q.push_back({y2-x2,x2});
        }
        return res;
    }
};



// using pp = pair<int,int>;
// const int inf = 0x3f3f3f3f;

// class Solution {
// public:
//     int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
//         int res = -inf; 
//         int n = points.size();
//         priority_queue<pp,vector<pp>> q;
//         for (int left = 0, right = 0; left < n; left++){
//             while (right < n && points[right][0]-points[left][0] <= k){
//                 q.push({points[right][1]+points[right][0],points[right][0]});
//                 right++;
//             }
//             while (!q.empty() && q.top().second <= points[left][0])
//                 q.pop();
//             if (q.empty())
//                 continue;
//             auto [xy2,x2] = q.top(); 
//             int x1 = points[left][0], y1 = points[left][1];
//             // cout << x1 << " " << y1 << " " << xy2 << endl;
//             res = max(res, xy2+y1-x1);
//         }
//         return res;
//     }
// };