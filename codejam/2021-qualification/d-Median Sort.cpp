//quick sort
// #include <bits/stdc++.h>

// using namespace std;
// ofstream flog("log_solution");

// const int inf = 0x3f3f3f3f;

// class Solution
// {
// public:
//     int median(int a, int b, int c){
//         int res;
//         cout << a << " " << b << " " << c << endl;
//         cin >> res;
//         // flog << a << " " << b << " " << c << endl;
//         // flog << res << endl;
//         return res;
//     }

//     void quickSort(int lo, int mid, int hi, vector<int> &arr){
//         int tmp = median(arr[lo], arr[mid], arr[hi]);
//         if (tmp == arr[lo])
//             std::swap(arr[lo], arr[mid]);
//         else if (tmp == arr[hi])
//             std::swap(arr[mid], arr[hi]);
//         for (int i = mid+1, j = hi; i < j;){
//             int tmp = median(arr[lo], arr[mid], arr[i]);
//             if (tmp == arr[mid]){
//                 std::swap(arr[i], arr[--j]);
//             }
//             else{
//                 std::swap(arr[i], arr[mid]);
//                 i++;mid++;
//             }
//         }
//         // flog << "lo : " << lo << "; mid: " << mid << "; hi: " << hi << endl;
//         // for (int i = 0; i < arr.size(); i++)
//         // {
//         //     if (i > 0)
//         //         flog << " ";
//         //     flog << arr[i];
//         // }
//         // flog << endl;
//         if (lo+1 < mid)
//             quickSort(lo, lo+1, mid, arr);
//         if (mid+1 < hi)
//             quickSort(mid, mid+1, hi, arr);
//     }

//     vector<int> medianSort(int n)
//     {
//         vector<int> arr;
//         for (int i = 1; i<= n; i++)
//             arr.push_back(i);
//         quickSort(0, 1, n-1, arr);
//         for (int i = 0; i < n; i++){
//             if (i > 0)
//                 cout << " ";
//             cout << arr[i];
//         }
//         cout << endl;
//         int res;
//         cin >> res;

//         return arr;
//     }
// };

// const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_input.txt";
// const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_output_.txt";

// int main()
// {
//     ios::sync_with_stdio(false);
//     // freopen(input, "r", stdin);
//     // freopen(output, "w", stdout);
//     // freopen("input", "r", stdin);
    
//     vector<int> vec;
//     Solution sol;
//     int T, N, Q;
//     // while (cin >> T >> N >> Q)
//     cin >> T >> N >> Q;
//     {
//         flog << T << " " << N << " " << Q << endl;

//         while (T--)
//         {
//             vec = sol.medianSort(N);

//             for (int i = 0; i < vec.size(); i++)
//             {
//                 if (i > 0)
//                     flog << " ";
//                 flog << vec[i];
//             }
//             flog << endl;
//         }
//     }
// }

























//insert sort
// #include <bits/stdc++.h>

// using namespace std;
// ofstream flog("log_solution");

// const int inf = 0x3f3f3f3f;

// class Solution
// {
// public:
//     int median(int a, int b, int c){
//         int res;
//         cout << a << " " << b << " " << c << endl;
//         cin >> res;
//         // flog << a << " " << b << " " << c << endl;
//         // flog << res << endl;
//         return res;
//     }

//     void insertSort(vector<int> &arr){
//         int n = arr.size(), mi = inf;
//         for (int i = 2; i < n; i++){
//             int mid = median(arr[0],arr[i-1],arr[i]);
//             if (mid == arr[0])
//                 std::swap(arr[0], arr[i]);
//             else if (mid == arr[i-1])
//                 std::swap(arr[i-1], arr[i]);
//         }
//         for (int i = 2; i < n; i++){
//             int lo = 1, hi = i-1;
//             while (lo <= hi){
//                 int idx = (lo+hi)/2;
//                 if (median(arr[0], arr[idx], arr[i]) == arr[idx])
//                     lo = idx+1;
//                 else 
//                     hi = idx-1;
//             }
//             for (int j = i; j > lo; j--)
//                 std::swap(arr[j-1], arr[j]);
//         }
//     }

//     vector<int> medianSort(int n)
//     {
//         vector<int> arr;
//         for (int i = 1; i<= n; i++)
//             arr.push_back(i);
//         insertSort(arr);
//         for (int i = 0; i < n; i++){
//             if (i > 0)
//                 cout << " ";
//             cout << arr[i];
//         }
//         cout << endl;
//         int res;
//         cin >> res;

//         return arr;
//     }
// };

// const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_input.txt";
// const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_output_.txt";

// int main()
// {
//     ios::sync_with_stdio(false);
//     // freopen(input, "r", stdin);
//     // freopen(output, "w", stdout);
//     // freopen("input", "r", stdin);
    
//     vector<int> vec;
//     Solution sol;
//     int T, N, Q;
//     // while (cin >> T >> N >> Q)
//     cin >> T >> N >> Q;
//     {
//         flog << T << " " << N << " " << Q << endl;

//         while (T--)
//         {
//             vec = sol.medianSort(N);

//             for (int i = 0; i < vec.size(); i++)
//             {
//                 if (i > 0)
//                     flog << " ";
//                 flog << vec[i];
//             }
//             flog << endl;
//         }
//     }
// }
























//insert sort with ternary search
#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");


class Solution
{
public:
    map<tuple<int,int,int>,int> memo;
    int median(int a, int b, int c){
        // auto it = memo.find({a, b, c});
        // if (it != memo.end())
        // {
        //     flog << "Found in memo" << endl;
        //     return it->second;
        // }

        int res;
        cout << a << " " << b << " " << c << endl;
        cin >> res;
        // vector<int> permu = {a,b,c};
        // do{
        //     memo[{permu[0],permu[1],permu[2]}] = res;
        //     flog << "Permutation : " << permu[0] << " " << permu[1] << " " << permu[2] << endl;
        // }while(std::next_permutation(permu.begin(), permu.end()));
        
        // flog << a << " " << b << " " << c << endl;
        // flog << res << endl;
        return res;
    }

    void insertSort(vector<int> &arr){
        int n = arr.size();
        
        for (int i = 2; i < n; i++){
            int lo = 0, hi = i-1;
            while (lo < hi){
                int a = max(lo, lo+(hi-lo+1)/3-1);
                int b = min(hi, max(a+1, lo+((hi-lo+1)/3)*2-1));
                flog << "lo: " << lo << " a: " << a << " b: " << b << " hi: " << hi << " i: " << i << endl;
                int mid = median(arr[a], arr[b], arr[i]);
                if (mid == arr[b]){
                    lo = b + 1;
                    if (lo == hi)
                        lo--;
                }
                else if (mid == arr[i]){
                    lo = a+1;
                    hi = b-1;
                    if (lo == hi){
                        lo--;
                        hi++;
                    }                    
                }
                else{
                    hi = a-1;
                    if (lo == hi)
                        hi++;
                }
            }
            for (int j = i; j > lo; j--)
                std::swap(arr[j-1], arr[j]);
        }
    }

    vector<int> medianSort(int n)
    {
        memo.clear();
        vector<int> arr;
        for (int i = 1; i<= n; i++)
            arr.push_back(i);
        insertSort(arr);
        for (int i = 0; i < n; i++){
            if (i > 0)
                cout << " ";
            cout << arr[i];
        }
        cout << endl;
        int res;
        cin >> res;

        return arr;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    
    vector<int> vec;
    Solution sol;
    int T, N, Q;
    // while (cin >> T >> N >> Q)
    cin >> T >> N >> Q;
    {
        flog << T << " " << N << " " << Q << endl;

        while (T--)
        {
            vec = sol.medianSort(N);

            for (int i = 0; i < vec.size(); i++)
            {
                if (i > 0)
                    flog << " ";
                flog << vec[i];
            }
            flog << endl;
        }
    }
}