const int N = 505;
int s[N][N], g[N][N], f[N][N], mxl[N][N], mxr[N][N];
class Solution {
public:
	int stoneGameV(vector<int>& a) {
		int n = a.size();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				f[i][j] = g[i][j] = s[i][j] = 0;
				mxl[i][j] = mxr[i][j] = 0;
			}
		}
		for (int i = 0; i < n; i++) {
			s[i][i] = a[i];
            g[i][i] = i;
            for (int j = i + 1; j < n; j++) {
                s[i][j] = s[i][j - 1] + a[j];
                int now = g[i][j - 1];
                while (s[i][j] - s[i][now] > s[i][now]) {
                    now++;
                }
                g[i][j] = now;
            }
		}
        
		for (int len = 1; len <= n; len++) {
			for (int l = 0; l + len - 1 < n; l++) {
				int r = l + len - 1;
				int mid = g[l][r];
				int ls = s[l][mid];
				int rs = s[mid + 1][r];
				if (ls == rs) {
					f[l][r] = max(f[l][r], mxl[l][mid]);
					f[l][r] = max(f[l][r], mxr[mid + 1][r]);
				} else {
					if (mid > l) {
						int ls = s[l][mid - 1];
						f[l][r] = max(f[l][r], mxl[l][mid - 1]);
					}
					if (mid < r) {
						int rs = s[mid + 1][r];
						f[l][r] = max(f[l][r], mxr[mid + 1][r]);
					}
				}
				int v = f[l][r] + s[l][r];
				if (l == r) {
					mxl[l][r] = mxr[l][r] = v;
				} else {
					mxl[l][r] = max(v, mxl[l][r - 1]);
					mxr[l][r] = max(v, mxr[l + 1][r]);
				}
			}
		}
		return f[0][n - 1];
	}
};
