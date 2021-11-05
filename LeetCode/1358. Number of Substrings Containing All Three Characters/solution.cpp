class Solution {
public:
    int numberOfSubstrings(string s) {
        vector<int> cc(3,0);
        int cnt = 0, left = 0, n = s.length(), res = 0;
        for (int right = 0; right < n; right++){
            int idx = s[right]-'a';
            if (cc[idx] == 0)
                cnt++;
            cc[idx]++;
            while (cnt == 3){
                int idx = s[left]-'a';
                cc[idx]--;
                if(cc[idx] == 0)
                    cnt--;
                left++;
            }
            res += left;
        }
        return res;

    }
};