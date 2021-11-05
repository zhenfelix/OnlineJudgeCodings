证明再贪心分割的时候一定会存在一个恰好等于hi的解

class Solution {
public:
    int maximizeSweetness(vector<int>& sweetness, int k) {
        int lo = *min_element(sweetness.begin(), sweetness.end());
        int hi = accumulate(sweetness.begin(), sweetness.end(), 0)/(k+1);

        auto check = [&](int x){
            int sums = 0, cnt = 0;
            for (auto s : sweetness){
                sums += s;
                if (sums >= x){
                    sums = 0;
                    cnt++;
                }
                if (cnt > k)
                    return true;
            }
            return false;
        };

        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (check(mid))
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return hi;
    }
};