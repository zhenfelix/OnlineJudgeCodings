const int mx = 250;
std::vector<bool> flag(mx*mx+1, false);
bool is_init = false;

class Solution {
public:
    
    void init(){
        for (int i = 1; i <= mx; i++){
            flag[i*i] = true;
        }
        is_init = true;
    }
    int countTriples(int n) {
        if (!is_init)
            init();
        int cnt = 0;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++)
            {
                if (i*i+j*j > n*n)
                    continue;
                cnt += flag[i*i+j*j];
            }

        }
        return cnt;
    }
};