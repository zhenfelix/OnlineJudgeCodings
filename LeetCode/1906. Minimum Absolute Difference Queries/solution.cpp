class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> index[101];
        int i = 0;
        for(auto x : nums) {
            index[x].push_back(i++);
        }
        vector<int> ans(queries.size());
        int j = 0;
        for(auto &q : queries) {
            int l = q[0], r = q[1];
            int prev = -1;
            int d = INT_MAX;
            for(int i = 1; i <= 100; i ++) {
                if(index[i].size() == 0) continue;
                int idx = lower_bound(index[i].begin(), index[i].end(), l) - index[i].begin();
                int idx2 = upper_bound(index[i].begin(), index[i].end(), r) - index[i].begin();
                if(idx2 <= idx) continue;
                if(prev != -1) {
                    d = min(i - prev, d);
                }
                if(d == 1) break; //early break, no answer better than 1
                prev = i;
            }
            ans[j] = d == INT_MAX ? -1 : d;
            j++;
        }
        return ans;
    }
};


class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        vector<vector<int>> positions(101);
        int n = nums.size(), m = queries.size();
        for (int i = 0; i < n; i++){
            positions[nums[i]].push_back(i);
        }
        vector<int> ans(m, 100);
        for (int i = 0; i < m; i++){
            int left = queries[i][0];
            int right = queries[i][1];
            vector<int> val = {-200};
            for (int j = 1; j <= 100; j++){
                int lo = lower_bound(positions[j].begin(), positions[j].end(), left) - positions[j].begin();
                int hi = upper_bound(positions[j].begin(), positions[j].end(), right) - positions[j].begin();
                if (hi-lo > 1 && hi-lo == right-left+1){
                    ans[i] = -1;
                    break;
                }
                else if (hi-lo > 0){
                    ans[i] = min(ans[i],j-val.back());
                    val.push_back(j);
                }
            }
        }
        return ans;
    }
};





class Solution {
private:
    // 元素 c 的最大值
    static constexpr int C = 100;

public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        // 前缀和
        vector<array<int, C + 1>> pre(n + 1);
        fill(pre[0].begin(), pre[0].end(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            copy_n(pre[i].begin(), C + 1, pre[i + 1].begin());
            ++pre[i + 1][nums[i]];
        }

        int q = queries.size();
        vector<int> ans;
        for (int i = 0; i < q; ++i) {
            int left = queries[i][0], right = queries[i][1];
            // last 记录上一个出现的元素
            // best 记录相邻两个元素差值的最小值
            int last = 0, best = INT_MAX;
            for (int j = 1; j <= C; ++j) {
                if (pre[left][j] != pre[right + 1][j]) {
                    if (last) {
                        best = min(best, j - last);
                    }
                    last = j;
                }
            }
            if (best == INT_MAX) {
                best = -1;
            }
            ans.push_back(best);
        }
        return ans;
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-absolute-difference-queries/solution/cha-xun-chai-jue-dui-zhi-de-zui-xiao-zhi-fjjq/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。