#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct Institute
{
    int cnt, tws;
    vector<int> scores;
    string name;
    Institute() = default;
    Institute(string name_)
        : name(name_), cnt(0), tws(0.0), scores(vector<int>(3,0))
        {}
};


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int n, sc;
    string id, school;
    vector<Institute> arr;
    map<string,int> mp, s2idx = {{"B",0},{"A",1},{"T",2}};
    cin >> n;
    while (n--)
    {
        cin >> id >> sc >> school;
        std::transform(school.begin(), school.end(), school.begin(), [](char ch){ return std::tolower(ch); });
        if (mp.find(school) == mp.end()){
            mp.insert({school, arr.size()});
            arr.push_back(Institute(school));
        }
        int idx = mp[school];
        arr[idx].scores[s2idx[id.substr(0, 1)]] += sc;
        arr[idx].cnt++;
    }
    for (auto &item : arr){
        item.tws = item.scores[0]/1.5 + item.scores[1] + item.scores[2]*1.5;
    }
    sort(arr.begin(), arr.end(), [](const Institute &a, const Institute &b){
        if (a.tws == b.tws){
            if (a.cnt == b.cnt)
                return a.name < b.name;
            return a.cnt < b.cnt;
        }
        return a.tws > b.tws;
    });
    int len = arr.size(), pre_tws = -1, rank = -1;
    cout << len << endl;
    for (int i = 0; i < len; i++){
        if (arr[i].tws != pre_tws)
            rank = i+1;
        pre_tws = arr[i].tws;
        cout << rank << " " << arr[i].name << " " << arr[i].tws << " " << arr[i].cnt << endl;
    }
    return 0;
}
