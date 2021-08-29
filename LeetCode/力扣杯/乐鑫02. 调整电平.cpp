class Solution {
public:
    int adjustLevel(int cnt) {
        int res = 0;
        for (int i = 1; i*i <= cnt; i++)
            res++;
        return res;
    }
};

class Solution {
public:
    int adjustLevel(int cnt) {

        return sqrt(cnt);
    }
};