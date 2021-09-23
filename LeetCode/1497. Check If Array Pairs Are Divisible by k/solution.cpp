class Solution
{
public:
    bool canArrange(vector<int> &arr, int k)
    {
        
        vector<int> mp(k+1,0);
        for (auto a : arr) {
            mp[(a % k + k) % k]++;
            // printf("%d %d %d\n",a,k,(a%k+k)%k);
        }
        if(mp[0]&1)return false;
        for (int i = 1; i < k; i++)
        {
           if(mp[i]!=mp[k-i])return false;
        }
        return true;
    }
};



class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> cnt(k,0);
        for (auto x : arr)
            cnt[(x%k+k)%k]++;
        int left = 1, right = k-1;
        for (; left < right; left++, right--)
            if (cnt[left] != cnt[right])
                return false;
        if (left == right && cnt[left]&1)
            return false;
        return true;
    }
};