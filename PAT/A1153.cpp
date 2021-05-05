#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");


struct Person{
    string level,site,date,id;
    int score;
    // bool operator==(const Person &other) const
    // {
    //     return id == other.id;
    // }
    // bool operator!=(const Person &other) const
    // {
    //     return !(id == other.id);
    // }
    // bool operator< (const Person& other) const
    // {
    //     return id < other.id;
    // }
};

istream &operator>> (istream &input, Person &cur)
{
    string tmp;
    input >> tmp;
    cur.level = tmp[0];
    cur.site = tmp.substr(1,3);
    cur.date = tmp.substr(4,6);
    cur.id = tmp;
    input >> cur.score;
    return input;
}


// ostream &operator<<(ostream &out, Person &cur)
// {
//     out << cur.id;
//     return out;
// }

class Solution
{
public:
    void decode()
    {
        
    }
};



int main()
{
    // ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    
    Solution sol;
    int n, m;
    map<string,vector<pair<int,string>>> level2score;
    map<string, int> site2cnt, site2score;
    map<string, map<string, int>> date2site2cnt;
    map<string, vector<pair<int, string>>> date2cnt_site;

    cin >> n >> m;
    while (n--)
    {
        Person p;
        cin >> p;
        level2score[p.level].push_back({-p.score, p.id});
        site2cnt[p.site]++;
        site2score[p.site] += p.score;
        date2site2cnt[p.date][p.site]++;
    }
    // for (auto &[key, values] : level2score){
    //     sort(values.begin(), values.end());
    // }
    for (auto &item : level2score)
    {
        auto &values = item.second;
        sort(values.begin(), values.end());
    }
    // for (auto &[date, values] : date2site2cnt){
    //     for (auto &[site, cnt] : values){
    //         date2cnt_site[date].push_back({-cnt,site});
    //     }
    //     auto &arr = date2cnt_site[date];
    //     sort(arr.begin(), arr.end());
    // }
    for (auto &item : date2site2cnt)
    {
        auto &date = item.first;
        auto &values = item.second;
        for (auto &item2 : values)
        {
            auto &site = item2.first;
            auto &cnt = item2.second;
            date2cnt_site[date].push_back({-cnt, site});
        }
        auto &arr = date2cnt_site[date];
        sort(arr.begin(), arr.end());
    }

    int qtype, idx = 1;
    string term;
    while (m--){
        cin >> qtype >> term;
        cout << "Case " << idx++ << ": " << qtype << " " << term << endl;
        bool na = true;
        if (qtype == 1){
            if (level2score.find(term) != level2score.end()){
                // for (auto &[score, id] : level2score[term])
                for (auto &item : level2score[term])
                {
                    cout << item.second << " " << -(item.first) << endl;
                }
                na = false;
            }
        }
        else if (qtype == 2){
            if (site2cnt.find(term) != site2cnt.end()){
                cout << site2cnt[term] << " " << site2score[term] << endl;
                na = false;
            }
            
        }
        else{
            if (date2cnt_site.find(term) != date2cnt_site.end()){
                // for (auto &[cnt, site] : date2cnt_site[term])
                for (auto &item : date2cnt_site[term])
                {
                    cout << item.second << " " << -(item.first) << endl;
                }
                na = false;
            }

        }
        if (na){
            cout << "NA" << endl;
        }
        // cout << a << " " << b << endl;
    }
}