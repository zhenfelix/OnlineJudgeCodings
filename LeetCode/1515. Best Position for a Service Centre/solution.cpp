using pp = pair<int,int>;
vector<pp> dxy = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,0},{0,1},{1,-1},{1,0},{1,1}};

class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {

        auto calc = [&](double xx, double yy){
            double d = 0;
            for (auto p : positions)
                d += sqrt((xx-p[0])*(xx-p[0])+(yy-p[1])*(yy-p[1]));
            return d;
        };


        double cx = 0, cy = 0, scale = 200, res = DBL_MAX;
        for (;scale > 1e-6;){
            double tmp = DBL_MAX, px = 0, py = 0;
            scale *= 0.7;
            for (auto [dx, dy] : dxy){
                double x = cx + dx*scale, y = cy + dy*scale;
                double tot = calc(x,y);
                if (tot < tmp){
                    tmp = tot;
                    px = x;
                    py = y;
                }
            }
            cx = px, cy = py;
            // double decrease = res-tmp;
            res = min(res, tmp);
            // if (decrease > 0 && decrease < 1e-5)
            //     break;
        }
        return res;
    }
};

//爬山法
// OJ: https://leetcode.com/contest/weekly-contest-197/problems/best-position-for-a-service-centre/
// Author: github.com/lzl124631x
class Solution {
    double dist(vector<int> &a, vector<double> &b) {
        return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2));
    }
    double all(vector<vector<int>> &A, vector<double> &p) {
        double ans = 0;
        for (auto &a : A) ans += dist(a, p);
        return ans;
    }
    const int dirs[4][2] = {{0,1},{0,-1},{-1,0},{1,0}};
public:
    double getMinDistSum(vector<vector<int>>& A) {
        double ans = DBL_MAX;
        vector<double> p(2, 0);
        double step = 100, eps = 1e-6;
        while (step > eps) {
            bool found = false;
            for (auto &dir : dirs) {
                vector<double> next = {p[0] + step * dir[0], p[1] + step * dir[1]};
                double d = all(A, next);
                if (d < ans) {
                    ans = d;
                    p = next;
                    found = true;
                    break;
                }
            }
            if (!found) step /= 2;
        }
        return ans;
    }
};


class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        double eps = 1e-7;
        double alpha = 1;
        double decay = 1e-3;
        
        int n = positions.size();
        // 调整批大小
        int batchSize = n;
        
        double x = 0.0, y = 0.0;
        for (const auto& pos: positions) {
            x += pos[0];
            y += pos[1];
        }
        x /= n;
        y /= n;
        
        // 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        auto getDist = [&](double xc, double yc) {
            double ans = 0;
            for (const auto& pos: positions) {
                ans += sqrt((pos[0] - xc) * (pos[0] - xc) + (pos[1] - yc) * (pos[1] - yc));
            }
            return ans;
        };
        
        mt19937 gen{random_device{}()};

        while (true) {
            // 将数据随机打乱
            shuffle(positions.begin(), positions.end(), gen);
            double xPrev = x;
            double yPrev = y;

            for (int i = 0; i < n; i += batchSize) {
                int j = min(i + batchSize, n);
                double dx = 0.0, dy = 0.0;
                // 计算导数，注意处理分母为零的情况
                for (int k = i; k < j; ++k) {
                    const auto& pos = positions[k];
                    dx += (x - pos[0]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps);
                    dy += (y - pos[1]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps);
                }
                x -= alpha * dx;
                y -= alpha * dy;

                // 每一轮迭代后，将学习率进行衰减
                alpha *= (1.0 - decay);
            }
            
            // 判断是否结束迭代
            if (sqrt((x - xPrev) * (x - xPrev) + (y - yPrev) * (y - yPrev)) < eps) {
                break;
            }
        }
        
        return getDist(x, y);
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/best-position-for-a-service-centre/solution/fu-wu-zhong-xin-de-zui-jia-wei-zhi-by-leetcode-sol/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        double eps = 1e-7;

        // 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        auto getDist = [&](double xc, double yc) {
            double ans = 0;
            for (const auto& pos: positions) {
                ans += sqrt((pos[0] - xc) * (pos[0] - xc) + (pos[1] - yc) * (pos[1] - yc));
            }
            return ans;
        };

        // 固定 xc，使用三分法找出最优的 yc
        auto checkOptimal = [&](double xc) {
            double yLeft = 0.0, yRight = 100.0;
            while (yRight - yLeft > eps) {
                double yFirst = (yLeft + yLeft + yRight) / 3;
                double ySecond = (yLeft + yRight + yRight) / 3;
                if (getDist(xc, yFirst) < getDist(xc, ySecond)) {
                    yRight = ySecond;
                }
                else {
                    yLeft = yFirst;
                }
            }
            return getDist(xc, yLeft);
        };
        
        double xLeft = 0.0, xRight = 100.0;
        while (xRight - xLeft > eps) {
            // 左 1/3 点
            double xFirst = (xLeft + xLeft + xRight) / 3;
            // 右 1/3 点
            double xSecond = (xLeft + xRight + xRight) / 3;
            if (checkOptimal(xFirst) < checkOptimal(xSecond)) {
                xRight = xSecond;
            }
            else {
                xLeft = xFirst;
            }
        }

        return checkOptimal(xLeft);
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/best-position-for-a-service-centre/solution/fu-wu-zhong-xin-de-zui-jia-wei-zhi-by-leetcode-sol/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <vector>

using namespace std;

// BEGIN NO SAD
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define f first
#define s second
typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> pii;
// END NO SAD
// REMEMBER CLEAR GLOBAL STATE

const int NUM_ITER = 50;

double x[100];
double y[100];
int n;

double solve(double xx, double yy) {
  double ret = 0;
  for(int i = 0; i < n; i++) {
    double a = x[i] - xx;
    double b = y[i] - yy;
    ret += sqrt(a*a+b*b);
  }
  return ret;
}

double xsolve(double xx) {
  double ymin = 0;
  double ymax = 100;
  double ret = 2e9;
  for(int q = 0; q < NUM_ITER; q++) {
    double a = .51*ymin + .49*ymax;
    double b = .49*ymin + .51*ymax;
    double as = solve(xx, a);
    double bs = solve(xx, b);
    if(as < bs) {
      ret = min(ret, as);
      ymax = b;
    }
    else {
      ret = min(ret, bs);
      ymin = a;
    }
  }
  return ret;
}

class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        n = sz(positions);
        for(int i = 0; i < n; i++) {
          x[i] = positions[i][0];
          y[i] = positions[i][1];
        }  
        double lhsx = 0;
        double rhsx = 100;
        double ret = 2e9;
        for(int q = 0; q < NUM_ITER; q++) {
          double a = .51 * lhsx + .49 * rhsx;
          double b = .51 * rhsx + .49 * lhsx;
          double as = xsolve(a);
          double bs = xsolve(b);
          if(as < bs) {
            rhsx = b;
            ret = min(ret, as);
          }
          else {
            lhsx = a;
            ret = min(ret, bs);
          }
        }
        return ret;
    }
};







