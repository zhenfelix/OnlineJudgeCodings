class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        for (int pile : piles)
            pq.emplace(pile);
        while (k > 0) {
            k--;
            int t = pq.top();
            pq.pop();
            pq.emplace(t - t / 2);
        }
        int ans = 0;
        while (!pq.empty())
            ans += pq.top(), pq.pop();
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/avaR15/view/EIciXR/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。