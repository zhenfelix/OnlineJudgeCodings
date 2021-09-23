class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        int mi = *min_element(bloomDay.begin(), bloomDay.end());
        int mx = *max_element(bloomDay.begin(), bloomDay.end());
        int lo = mi, hi = mx;
        while (lo <= hi){
            int day = (lo+hi)/2;
            int fs = 0, cnt = 0;
            bool flag = false;
            for (auto d : bloomDay){
                if (d <= day){
                    fs++;
                    if (fs == k){
                        cnt++;
                        fs = 0;
                    }
                }
                else
                    fs = 0;
                if (cnt >= m){
                    flag = true;
                    break;
                }
            }
            if (flag)
                hi = day-1;
            else
                lo = day+1;
        }
        if (lo > mx)
            return -1;
        return lo;

    }
};