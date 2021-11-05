using pp = pair<double,int>;

const double pi = 3.1415926;

class Solution {
public:
    int numPoints(vector<vector<int>>& points, int r) {
        int n = points.size(), res = 0;
        for (int i = 0; i < n; i++){
            vector<pp> diff;
            int cnt = 0, x = points[i][0], y = points[i][1];
            for (int j = 0; j < n; j++){
                if (points[i] == points[j]){
                    cnt++;
                    continue;
                }
                int xx = points[j][0], yy = points[j][1];
                double R = sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy));
                if (R > r*2)
                    continue;
                double theta = acos(R/(r*2)), phi = atan2(yy-y,xx-x);
                diff.push_back({phi-theta,-1});
                diff.push_back({phi+theta,1});
            }
            sort(diff.begin(), diff.end());
            int m = diff.size();
            for (int j = 0; j < m; j++){
                auto [angle, delta] = diff[j];
                diff.push_back({angle+pi*2,delta});
            }
            res = max(res, cnt);
            for (auto &[angle,delta] : diff){
                cnt -= delta;
                res = max(res, cnt);
            }
        }
        return res;
    }
};