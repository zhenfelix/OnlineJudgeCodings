class Solution {
public:
    bool sumGame(string num) {
        int n = num.length(), cnt = 0, sums = 0;
        for (int i = 0; i < n; i++){
            int flag = (i < n/2) ? -1 : 1;
            if (num[i] == '?')
                cnt += flag;
            else
                sums += flag*(num[i]-'0');
        }
        if (cnt*sums > 0 || abs(cnt)&1)
            return true;
        sums = abs(sums);
        cnt = abs(cnt);
        return sums != cnt/2*9;
    }
};