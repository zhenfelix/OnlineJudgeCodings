class Solution {
public:
    int storeWater(vector<int>& bucket, vector<int>& vat) {
        const int maxn = 10000;
        int res = 0x3f3f3f3f;
        int n = bucket.size();
        for (int i = 0; i < maxn; ++i)
        {
            int cnt = 0;
            for (int j = 0; j < n; ++j)
            {
                if (i == 0)
                {
                    if (vat[j] == 0)
                        continue;
                    else
                        {
                            cnt = 0x3f3f3f3f;
                            break;
                        }
                }
                cnt += max((vat[j]-1)/i + 1 - bucket[j], 0);
            }
            res = min(res, i+cnt);
        }
        return res;
    }
};