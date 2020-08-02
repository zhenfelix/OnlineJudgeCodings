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
