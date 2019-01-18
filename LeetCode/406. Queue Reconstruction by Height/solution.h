class Solution {
public:
    static bool comp(pair<int,int> a, pair<int,int> b){
        return (a.first>b.first)||(a.first==b.first&&a.second<b.second);
    }
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int, int>> ans;
        sort(people.begin(), people.end(), comp);
        for(auto p: people)ans.insert(ans.begin()+p.second, p);
        return ans;
    }
};