// #include <iostream>
// #include <string>
// #include <cmath>
// #include <cstdio>
// #include <vector>
// #include <set>
// //#include <pair>
// using namespace std;



// int main()
// {
// //    freopen("input.txt","r",stdin);
//     int n,tmp,a,b;
//     vector<int> claim;
//     bool flag=false;
//     claim.push_back(0);
//     cin>>n;
//     for(int i=0;i<n;i++){cin>>tmp;claim.push_back(tmp);}
//     for (int i=1; i<=n; i++) {
//         for(int j=i+1;j<=n;j++){
//             int k;
//             int black=1,white=1;
//             for(k=1;k<=n;k++){
//                 int val=claim[k];
//                 if((val>0&&(val==i||val==j))||(val<0&&(-val)!=i&&(-val)!=j)){
//                     if(k==i||k==j)black--;
//                     else white--;
//                 }
//                 if(black<0||white<0)break;
//             }
//             if(k>n&&black==0&&white==0){flag=true;b=j;break;}
//         }
//         if(flag){a=i;break;}
//     }
//     if(flag)cout<<a<<" "<<b<<endl;
//     else cout<<"No Solution"<<endl;
//     return 0;
// }



#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> v(n+1);
    for (int i = 1; i <= n; i++) cin >> v[i];
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            vector<int> lie, a(n + 1, 1);
            a[i] = a[j] = -1;
            for (int k = 1; k <= n; k++)
                if (v[k] * a[abs(v[k])] < 0) lie.push_back(k);
            if (lie.size() == 2 && a[lie[0]] + a[lie[1]] == 0) {
                cout << i << " " << j;
                return 0;
            }
        }
    }
    cout << "No Solution";
    return 0;
}