template<typename T, typename Op, typename Alloc = std::allocator<T>>
class Queue {
public:
    using value_type = T;
    using size_type = unsigned;

private:
    Op op;
    value_type in_stk_sum;
    std::vector<value_type, Alloc> in_stk, out_stk;

public:
    Queue(const Op& op = {}) : op(op) {}

    template<typename U>
    void push(U&& val) {
        in_stk_sum = !in_stk.empty() ? op(in_stk_sum, val) : val;
        in_stk.emplace_back(std::forward<U>(val));
    }

    void pop() {
        if (!out_stk.empty())
            out_stk.pop_back();
        else {
            if (in_stk.size() > 1) {
                const auto ptr = in_stk.data();
                auto it = ptr + in_stk.size() - 1;
                out_stk.push_back(std::move(*it));
                while (--it != ptr) out_stk.push_back(op(std::move(*it), out_stk.back()));
            }
            in_stk.clear();
        }
    }

    value_type sum() const noexcept {
        if (in_stk.empty()) return out_stk.back();
        if (out_stk.empty()) return in_stk_sum;
        return op(out_stk.back(), in_stk_sum);
    }

    size_type size() const noexcept {
        return in_stk.size() + out_stk.size();
    }

    bool empty() const noexcept {
        return in_stk.empty() && out_stk.empty();
    }
};

作者：白
链接：https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/solutions/2739224/onm-jie-fa-shuang-zhan-hua-dong-chuang-k-0zoz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int minimumValueSum(const vector<int>& nums, const vector<int>& andValues) {
        static constexpr int INF = 0x3f3f3f3f;
        const int n = nums.size();
        vector<int> dp(n + 1, INF);
        vector<int> dp0(n + 1);
        dp[0] = 0;
        for (int e : andValues) {
            Queue<int, bit_and<int>> q0, q1;
            int min_sum = INF;
            dp0[0] = INF;
            for (int i = 0;i < n;++i) {
                q0.push(nums[i]);
                q1.push(nums[i]);
                if (q0.sum() < e) {
                    min_sum = INF;
                    do {
                        q0.pop();
                    } while (!q0.empty() && q0.sum() < e);
                }
                while (!q1.empty() && q1.sum() < e)
                    q1.pop();
                for (;!q1.empty() && q1.sum() == e;q1.pop())
                    min_sum = min(min_sum, dp[i - q1.size() + 1]);
                dp0[i + 1] = min_sum + nums[i];
            }
            swap(dp, dp0);
        }
        return dp[n] < INF ? dp[n] : -1;
    }
};

作者：白
链接：https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/solutions/2739224/onm-jie-fa-shuang-zhan-hua-dong-chuang-k-0zoz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。