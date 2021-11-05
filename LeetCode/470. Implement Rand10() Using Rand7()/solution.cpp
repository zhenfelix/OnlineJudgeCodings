    stack<int> cache;
    int rand10() {
        while (cache.size() == 0) generate();
        int res = cache.top(); cache.pop();
        return res;
    }

    void generate() {
        int n = 19;
        long cur = 0, range = long(pow(7, n));
        for (int i = 0; i < n; ++i) cur += long(pow(7, i)) * (rand7() - 1);
        while (cur < range / 10 * 10) {
            cache.push(cur % 10 + 1);
            cur /= 10;
            range /= 10;
        }
    }



// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

// class Solution {
// public:
//     int rand10() {
//         while (true){
//             int a = rand7(), b = rand7();
//             int c = (a-1)*7+b-1;
//             if (c < 40)
//                 return c%10+1;
//         }

//     }
// };

class Solution {
public:
    int rand10() {
        int a, b, idx;
        while (true) {
            a = rand7();
            b = rand7();
            idx = b + (a - 1) * 7;
            if (idx <= 40) {
                return 1 + (idx - 1) % 10;
            }
            a = idx - 40;
            b = rand7();
            // get uniform dist from 1 - 63
            idx = b + (a - 1) * 7;
            if (idx <= 60) {
                return 1 + (idx - 1) % 10;
            }
            a = idx - 60;
            b = rand7();
            // get uniform dist from 1 - 21
            idx = b + (a - 1) * 7;
            if (idx <= 20) {
                return 1 + (idx - 1) % 10;
            }
        }
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/yong-rand7-shi-xian-rand10-by-leetcode-s-qbmd/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。