// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int idx = 0;
    int remain = 0;
    char* temp = new char[4];
    bool init = true;
    
    int read(char *buf, int n) {
        if(init){
            remain = read4(temp);
            init = false;
        }
        int i = 0;
        while(i < n && idx < remain){
            buf[i] = temp[idx%4];
            ++i;
            ++idx;
            if(idx%4 == 0) {
                remain += read4(temp);
            }
        }
        // remain -= i;
        return i;
    }
};