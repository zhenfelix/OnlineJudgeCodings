// O(NK) 解法：
// 一共使用 K 个单调栈。
// 对于每个数字来说，遇到一次比自己大的，就升一级（进入下一个单调栈）。
// 但有可能一次好几个数字升级，为了保证每个单调栈的单调性，需要将这些数字整体移动到下一个单调栈，因此需要借助一个临时栈中转一下。
 
const int K = 2;
 
class Solution {
public:
    vector<int> secondGreaterElement(vector<int>& nums) {
        vector<stack<int>> s(K); // 一共需要 K 个单调栈
        stack<int> tmp;
        int n = nums.size();
        vector<int> ans(n, -1);
        for (int i = 0; i < n; ++i) {
            // 从最后一个单调栈开始处理
            for (int k = K - 1; k >= 0; --k) {
                while (!s[k].empty() && nums[s[k].top()] < nums[i]) 
                    // 最后一个单调栈，毕业！
                    if (k == K - 1)
                        ans[s[k].top()] = nums[i];
                    // 进入中间舱
                    else
                        tmp.push(s[k].top());
                    s[k].pop();
                }
                if (k + 1 < K) {
                    // 倒序进入下一个单调栈，保证所有单调栈的单调性
                    while (!tmp.empty()) {
                        s[k + 1].push(tmp.top());
                        tmp.pop();
                    }
                }
            }
            s[0].push(i);
        }
        return ans;
    }



class Solution {
public:
    vector<int> secondGreaterElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        auto cmp = [&](int a, int b){
            return nums[a] > nums[b];
        };
        priority_queue<int, vector<int>, decltype(cmp)> q1(cmp), q2(cmp);

        for(int i = 0; i < n; ++i){
            int num = nums[i];
            while(!q2.empty() && nums[q2.top()] < num){
                ans[q2.top()] = num;
                q2.pop();
            }
            while(!q1.empty() && nums[q1.top()] < num){
                q2.push(q1.top());
                q1.pop();
            }
            q1.push(i);
        }

        return ans;
    }
};


// 作者：kotori-5
// 链接：https://leetcode.cn/problems/next-greater-element-iv/solution/c-by-kotori-5-7s4z/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    vector<int> secondGreaterElement(vector<int>& nums) {
        int n = nums.size();
        
        // 将所有下标按 nums[i] 降序为第一关键字，i 升序为第二关键字排序
        typedef pair<int, int> pii;
        vector<pii> vec;
        for (int i = 0; i < n; i++) vec.push_back(pii(-nums[i], i));
        sort(vec.begin(), vec.end());

        vector<int> ans(n);
        set<int> st;
        // 按排序后的顺序枚举下标
        for (int i = 0; i < n; i++) {
            // 找到有序列表里比 i 大的第二个数
            auto it = st.upper_bound(vec[i].second);
            if (it != st.end() && next(it) != st.end()) ans[vec[i].second] = nums[*next(it)];
            else ans[vec[i].second] = -1;
            // 将当前下标加入有序列表
            st.insert(vec[i].second);
        }
        return ans;
    }
};



作者：TsReaper
链接：https://leetcode.cn/circle/discuss/fL5HMZ/view/UX8btI/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。