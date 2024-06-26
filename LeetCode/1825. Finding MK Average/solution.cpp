// class MKAverage {
// public:
//     long long m, k, sum = 0;
//     multiset<int> lower, middle, upper;
//     queue<int> nums;
    
//     MKAverage(int m, int k) {
//         this->m = m;
//         this->k = k;
//     }
    
//     void shiftLeft(multiset<int>& l, multiset<int>& r) {
//         l.insert(*r.begin());
//         r.erase(r.begin());
//     }
    
//     void shiftRight(multiset<int>& l, multiset<int>& r) {
//         r.insert(*l.rbegin());
//         l.erase(--l.end());
//     }
    
//     void addElement(int num) {
//         nums.push(num);
        
//         if(lower.size() && *lower.rbegin() >= num) lower.insert(num);
//         else if(upper.size() && *upper.begin() <= num) upper.insert(num);
//         else middle.insert(num), sum += num;
        
//         if(lower.size() > k) sum += *lower.rbegin(), shiftRight(lower, middle);
//         if(upper.size() > k) sum += *upper.begin(), shiftLeft(middle, upper);
        
//         if(nums.size() > m) {
//             int d = nums.front(); nums.pop();
//             if(lower.find(d) != lower.end()) lower.erase(lower.find(d));
//             else if(middle.find(d) != middle.end()) middle.erase(middle.find(d)), sum -= d;
//             else upper.erase(upper.find(d));
//         }
        
//         if(lower.size() < k && middle.size()) sum -= *middle.begin(), shiftLeft(lower, middle);
//         if(upper.size() < k && middle.size()) sum -= *middle.rbegin(), shiftRight(middle, upper);
//     }
    
//     int calculateMKAverage() {
//         if(nums.size() < m) return -1;
//         return sum / (m - 2*k);
//     }
// };



class MKAverage {
public:
    long long m, k;
    const int maxn = 100010;
    queue<int> q;
    std::vector<long long> tree_cnt;
    std::vector<long long> tree_sums;
    
    MKAverage(int m, int k) {
        this->m = m;
        this->k = k;
        tree_cnt.resize(maxn,0);
        tree_sums.resize(maxn,0);
    }

    void _add(std::vector<long long> &tree, int x, int delta)
    {
        while (x <= maxn-1)
        {
            tree[x] += delta;
            x += (x&(-x));
        }
    }

    long long _query(std::vector<long long> &tree, int x)
    {
        long long res = 0;
        while (x > 0)
        {
            res += tree[x];
            x -= (x&(-x));
        }
        return res;
    }
    
    int _find(std::vector<long long> &tree, int cnt)
    {
        int lo = 0, hi = maxn;
        while (lo <= hi)
        {
            // int mid = (lo+hi)/2;
            int mid = (lo+hi)>>1;
            if (_query(tree, mid) >= cnt)
            {
                hi = mid - 1;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return lo;
    }
    
    void addElement(int num)
    {
        q.push(num);
        _add(tree_cnt, num, 1);
        _add(tree_sums, num, num);
        if (q.size() > m)
        {
            num = q.front(); q.pop();
            _add(tree_cnt, num, -1);
            _add(tree_sums, num, -num);
        }
    }
    
    int calculateMKAverage() {
        if(q.size() < m) return -1;
        long long sum = 0;
        int left = _find(tree_cnt, k);
        int right = _find(tree_cnt, m-k);
        sum += _query(tree_sums, right) - (_query(tree_cnt, right)-(m-k))*right;
        sum -= _query(tree_sums, left) - (_query(tree_cnt, left)-k)*left;
        return sum / (m - 2*k);
    }
};




// class MKAverage {
// public:
//     int m, k;
//     long long sums;
//     multiset<int> top, bottom, mid;
//     queue<int> q;
//     MKAverage(int m_, int k_):
//         m(m_), k(k_), sums(0)
//     {

//     }

//     void remove(int num){
//         auto it = mid.find(num);
//         if (it != mid.end()){
//             mid.erase(it);
//             sums -= num;
//             return;
//         }
//         it = bottom.find(num);
//         if (it != bottom.end()){
//             bottom.erase(it);
//             if (!mid.empty()){
//                 num = *mid.begin();
//                 mid.erase(mid.begin());
//                 sums -= num;
//                 bottom.insert(num);
//             }
//             return;
//         }
//         it = top.find(num);
//         if (it != top.end()){
//             top.erase(it);
//             if (!mid.empty()){
//                 it = mid.end();
//                 it--;
//                 num = *it;
//                 mid.erase(it);
//                 sums -= num;
//                 top.insert(num);
//             }
//             else if (!bottom.empty()){
//                 it = bottom.end();
//                 it--;
//                 num = *it;
//                 bottom.erase(it);
//                 top.insert(num);
//             }
//             return;
//         }
//         return;
//     }

//     void add(int num){
//         top.insert(num);
//         if (top.size() <= k)
//             return;
//         num = *top.begin();
//         top.erase(top.begin());
//         bottom.insert(num);
//         if (bottom.size() <= k)
//             return;
//         auto it = bottom.end();
//         num = *(--it);
//         bottom.erase(it);
//         sums += num;
//         mid.insert(num);
//         return;
//     }
    
//     void addElement(int num) {
//         if (q.size() == m){
//             remove(q.front());
//             q.pop();
//         }
//         q.push(num);
//         add(num);
//     }
    
//     int calculateMKAverage() {
//         if (q.size() < m)
//             return -1;
//         return sums/(m-k*2);
//     }
// };

// /**
//  * Your MKAverage object will be instantiated and called as such:
//  * MKAverage* obj = new MKAverage(m, k);
//  * obj->addElement(num);
//  * int param_2 = obj->calculateMKAverage();
//  */