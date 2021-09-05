class Solution {
public:
    int maxFrequency(vector<int>& A, long k) {
        int i = 0, j;
        sort(A.begin(), A.end());
        for (j = 0; j < A.size(); ++j) {
            k += A[j];
            if (k < (long)A[j] * (j - i + 1))
                k -= A[i++];
        }
        return j - i;
    }
};


using ll = long long;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        map<int,int> mp; 
        for (auto x : nums)
            mp[x]++;
        int pre = mp.begin()->first;
        ll res = 0, ops = 0, cnt = 0;
        auto left = mp.begin();
        for (auto right = mp.begin(); right != mp.end(); right++){
            int cur = right->first;
            ops += (cur-pre)*cnt;
            cnt += right->second;
            while (ops > k){
                ops -= (cur-left->first);
                left->second--;
                cnt--;
                if (left->second == 0)
                    left++;
            }
            res = max(res, cnt);
            pre = right->first;
        }
        return res;
    }
};