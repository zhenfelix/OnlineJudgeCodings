class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        multiset<int> st(people.begin(), people.end());
        int cnt = 0;
        while (!st.empty()){
            auto b = st.end();
            b = prev(b);
            int cur = *b;
            st.erase(b);
            auto it = st.upper_bound(limit-cur);
            if (it != st.begin()){
                it = prev(it);
                st.erase(it);
            }
            // for (auto v : st)
            //     cout << v << " ";
            // cout << endl;
            cnt++;
        }
        return cnt;
    }
};


class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        if(people.size() < 2)
            return people.size();
        sort(people.begin(),people.end());
        int num = 0 ;
        int left = 0;
        int right = people.size()-1;
        while(left<right)
        {
            if(people[right]+people[left] > limit)
            {
                right--;
                num++;
            }
            else
            {
                left++;
                right--;
                num++;
            }
        }
        if(left == right)
            num++;
        return num;
    }
};
