class Solution {
public:
    int maximumGain(string s, int x, int y) {
        char a = 'a', b = 'b';  
        int ca = 0, cb = 0, res = 0;
        s.push_back('$');
        if (x > y)
            swap(x,y), swap(a,b);
        for (auto ch : s){
            if (ch == a){
                if (cb){
                    cb--;
                    res += y;
                }
                else
                    ca++;
            }
            else if (ch == b){
                cb++;
            }
            else{
                res += min(ca,cb)*x;
                ca = cb = 0;
            }
        }
        return res;

    }
};