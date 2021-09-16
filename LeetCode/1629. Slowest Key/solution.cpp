class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        vector<int> tik(26,0);
        int res = 0, idx = -1, pre = 0, n = releaseTimes.size();
        for (int i = 0; i < n; i++){
            int cur = releaseTimes[i];
            char ch = keysPressed[i];
            if (cur-pre > tik[ch-'a'])
                tik[ch-'a'] = cur-pre;
            pre = cur;
        }
        for (int i = 25; i >= 0; i--){
            if (tik[i] > res){
                res = tik[i];
                idx = i;
            }
        }
        return 'a'+idx;
    }
};