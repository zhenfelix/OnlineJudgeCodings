class Solution {
public:
int dp[71][70 * 70 + 1] = {[0 ... 70][0 ... 70 * 70] = INT_MAX};
int dfs(vector<set<int>>& m, int i, int sum, int target) {
    if (i >= m.size())
        return abs(sum - target);
    if (dp[i][sum] == INT_MAX)
        for (auto it = begin(m[i]); it != end(m[i]); ++it) {
            dp[i][sum] = min(dp[i][sum], dfs(m, i + 1, sum + *it, target));
            if (dp[i][sum] == 0 || sum + *it > target)
                break;
        }
    return dp[i][sum];
}
int minimizeTheDifference(vector<vector<int>>& mat, int target) {
    vector<set<int>> m;
    for (auto &row : mat)
        m.push_back(set<int>(begin(row), end(row)));
    return dfs(m, 0, 0, target);
}
};



class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& A, int target) {
        int n=A.size();
        int m=A[0].size();
        int mi = 0;
        for (auto &row : A){
            mi += (*std::min_element(row.begin(), row.end()));
        }
        if (mi >= target)
            return mi-target;

        bitset<1605> F[n];
        F[0]=0;
        for (int i=0;i<m;++i) F[0][A[0][i]]=1;
        for (int i=1;i<n;++i)
        {
            F[i]=0;
            for (int j=0;j<m;++j)
                F[i]|=F[i-1]<<A[i][j];
        }
        int ans=1600;
        for (int i=1;i<=1600;++i)
            if (F[n-1][i])
                ans=min(ans,abs(target-i));
        return ans;
    }
};

// 作者：LighTcml
// 链接：https://leetcode-cn.com/problems/minimize-the-difference-between-target-and-chosen-elements/solution/jian-dan-bei-bao-dp-by-lightcml-eukp/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& A, int target) {
        int n=A.size();
        int m=A[0].size();
        bitset<5000> F[n];
        F[0]=0;
        for (int i=0;i<m;++i) F[0][A[0][i]]=1;
        for (int i=1;i<n;++i)
        {
            F[i]=0;
            for (int j=0;j<m;++j)
                F[i]|=F[i-1]<<A[i][j];
        }
        int ans=4900;
        for (int i=1;i<=4900;++i)
            if (F[n-1][i])
                ans=min(ans,abs(target-i));
        return ans;
    }
};

// 作者：LighTcml
// 链接：https://leetcode-cn.com/problems/minimize-the-difference-between-target-and-chosen-elements/solution/jian-dan-bei-bao-dp-by-lightcml-eukp/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。