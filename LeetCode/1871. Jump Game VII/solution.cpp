class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.length();
        if (s[n-1] == '1')
            return false;
        s[0] = '#';
        int reach = 0;
        for (int i = 0; i < n; i++){
            if (s[i] == '#'){
                reach = max(reach, i+minJump);
                while (reach < n && reach <= i+maxJump){
                    if (s[reach] == '0')
                        s[reach] = '#';
                    reach++;
                }
            }
        }
        return s[n-1] == '#';
    }
};