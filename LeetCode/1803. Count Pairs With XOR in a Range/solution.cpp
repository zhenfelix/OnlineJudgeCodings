// class Solution {
// public:
//     int tr[20005*16][2],cnt[20005*16],tot=0;
//     void insert(int x) {
//         int p=0;
//         for(int i=15;i>=0;--i) {
//             int idx=x>>i&1;
//             if(!tr[p][idx]) tr[p][idx]=++tot;
//             p=tr[p][idx];
//             cnt[p]++;
//         }
//     }
//     int query(int x, int hi) {
//         int ret=0,p=0;
//         for(int i=15;i>=0;--i) {
//             int a=x>>i&1,h=hi>>i&1;
//             if(a==0 && h==0) {
//                 ret+=cnt[tr[p][1]];
//                 p=tr[p][0];
//             }
//             if(a==0 && h==1) {
//                 p=tr[p][1];
//             }
//             if(a==1 && h==0) {
//                 ret+=cnt[tr[p][0]];
//                 p=tr[p][1];
//             }
//             if(a==1 && h==1) {
//                 p=tr[p][0];
//             }
//             if(!p) return ret;
//         }
//         // >hi
//         return ret;
//     }
//     int countPairs(vector<int>& a, int l, int h) {
//         for(int i:a) insert(i);
//         int ret=0;
//         for(int i:a) {
//             ret+=query(i,l-1)-query(i,h);
//         }
//         return ret/2;
//     }
// };


class Solution
{
public:
    int countPairs(vector<int>& A, int low, int high) {
        return test(A, high + 1) - test(A, low);
    }

    int test(vector<int>& A, int x) {
        unordered_map<int, int> count, count2;
        for (int a : A) count[a]--;
        int res = 0;
        while (x) {
            for (auto const& [k, v] : count) {
                count2[k >> 1] += v;
                if (x & 1)
                    if (count.find((x - 1) ^ k) != count.end())
                        res += v * count[(x - 1) ^ k];
            }
            swap(count, count2);
            count2.clear();
            x >>= 1;
        }
        return res / 2;
    }
};