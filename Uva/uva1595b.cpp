#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
struct point{
    double x,y;
    bool operator < (const point &a)const{
        if(a.y==y) return a.x>x;
        else return a.y>y;
    }
};
vector<point>a;
vector<point>b;
int main(){
    int t;
    double mid=0;
    cin>>t;
    while(t--){
        int n,k=1;
        point p;
        cin>>n;
        while(n--){
            cin>>p.x>>p.y;
            a.push_back(p);
            b.push_back(p);
        }
        if(n==1){
            cout<<"YES"<<endl;
            a.clear();
            b.clear();
            continue;
        }
        sort(a.begin(),a.end());
        for(int i=1;i<a.size();i++){
            if(a[0].y!=a[i].y){
                mid=(a[0].x+a[i-1].x)/2;
                break;
            }
        }
        for(int i=0;i<b.size();i++) b[i].x=2*mid-b[i].x;
        sort(b.begin(),b.end());
        for(int i=0;i<a.size();i++){
            if(a[i].x!=b[i].x||a[i].y!=a[i].y){
                k=0;
                break;
            }
        }
        if(k) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        a.clear();
        b.clear();
    }
    return 0;
}