using ll = long long;


class Solution
{
public:
    int minSkips(vector<int> &dist, int speed, int hoursBefore)
    {
        int n = dist.size();
        vector<ll> dist_(n);
        ll tot = 0;
        for (int i = 0; i < n; i++)
        {
            tot += dist[i];
            dist_[i] = dist[i] * static_cast<ll>(speed);
        }
        if (tot > static_cast<ll>(speed) * hoursBefore)
            return -1;
        vector<ll> dp(n, 0);

        for (int j = 0; j < n; j++)
        {
            ll pre = j > 0 ? dp[j - 1] : 0;
            ll cur = pre;
            for (int i = j; i < n; i++)
            {
                ll tmp = dp[i];
                
                if (cur % speed)
                    cur += (speed - (cur % speed));
                cur += dist_[i] / speed;
                pre += dist_[i] / speed;
                dp[i] = cur;
                if (j > 0)
                {
                    dp[i] = min(dp[i], pre);
                }
                cur = dp[i];
                pre = tmp;
            }
            if (cur <= static_cast<ll>(speed) * hoursBefore)
                return j;
        }
        return -1;
    }
};