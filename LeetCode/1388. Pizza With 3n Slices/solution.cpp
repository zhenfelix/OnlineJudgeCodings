class Solution {
public:
    int calculate(const vector<int>& slices) {
        int n = slices.size();
        int choose = (n + 1) / 3;
        vector<vector<int>> dp(n + 1, vector<int>(choose + 1));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= choose; ++j) {
                dp[i][j] = max(dp[i - 1][j], (i - 2 >= 0 ? dp[i - 2][j - 1] : 0) + slices[i - 1]);
            }
        }
        return dp[n][choose];
    }

    int maxSizeSlices(vector<int>& slices) {
        vector<int> v1(slices.begin() + 1, slices.end());
        vector<int> v2(slices.begin(), slices.end() - 1);
        int ans1 = calculate(v1);
        int ans2 = calculate(v2);
        return max(ans1, ans2);
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/pizza-with-3n-slices/solution/3n-kuai-pi-sa-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// struct Node {
//     int value, l, r;
// };

// vector<Node> a; // 基于vector实现双向链表

// struct Id {
//     int id;

//     bool operator<(const Id &that) const {
//         return a[id].value < a[that.id].value;
//     }
// };

// void del(int i) {
//     // 这里不需要更新i的左右指针，因为i已经不会再被使用了
//     a[a[i].l].r = a[i].r;
//     a[a[i].r].l = a[i].l;
// }

// class Solution {
// public:
//     int maxSizeSlices(vector<int> &slices) {
//         int n = slices.size();
//         int k = n / 3;

//         // 初始化双向链表
//         a.clear();
//         for (int i = 0; i < n; ++i)
//             a.emplace_back(Node{slices[i], (i - 1 + n) % n, (i + 1) % n});
//         priority_queue<Id> pq;
//         vector<bool> can_take(n, true); // 标记某一序号是否能够选取
//         int idx = 0;
//         for (int i = 0; i < n; ++i)
//             pq.push(Id{i}); // 优先队列初始化
//         int cnt = 0, ans = 0;
//         while (cnt < k) {
//             int id = pq.top().id;
//             pq.pop();
//             if (can_take[id]) { // 当前序号可用
//                 cnt++;
//                 ans += a[id].value;
//                 // 标记前后序号
//                 int pre = a[id].l;
//                 int nxt = a[id].r;
//                 can_take[pre] = false;
//                 can_take[nxt] = false;
//                 // 更新当前序号的值为反悔值
//                 a[id].value = a[pre].value + a[nxt].value - a[id].value;
//                 // 当前序号重新入队
//                 pq.push(Id{id});
//                 // 删除前后序号（更新双向链表）
//                 del(pre);
//                 del(nxt);
//             }
//         }
//         return ans;
//     }
// };


// // 作者：lucifer1004
// // 链接：https://leetcode-cn.com/problems/pizza-with-3n-slices/solution/shuang-xiang-lian-biao-tan-xin-suan-fa-shi-jian-fu/
// // 来源：力扣（LeetCode）
// // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。