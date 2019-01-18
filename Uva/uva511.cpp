#include <iostream>
#include <map>
#include <set>
#include <vector>
#include<string>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;

struct MAP{
    string name;
    double x1,x2,y1,y2,s;
};
struct LOC{
    string name;
    double x,y;
};
struct MAP_LOC{
    string name;
    double x1,x2,y1,y2,s,d0,r,lr;
};
typedef vector<MAP> maps;
typedef vector<MAP_LOC> map_locs;
maps mm;
map<string,map_locs>dic;
set<string>locs;

double dis(double x1,double y1,double x2,double y2){
    return pow(x1-x2,2)+pow(y1-y2,2);
}
bool cmp(MAP_LOC a,MAP_LOC b){
    if(a.s!=b.s)return a.s>b.s;
    else if(a.d0!=b.d0)return a.d0<b.d0;
    else if(a.r!=b.r)return a.r<b.r;
    else if (a.lr!=b.lr)return a.lr>b.lr;
    else return a.x1<b.x1;
}
void print_result(string str,int level){
    map_locs tt;
    if(!locs.count(str))cout<<str<<" at detail level "<<level<<" unknown location"<<endl;
    else if(!dic.count(str))cout<<str<<" at detail level "<<level<<" no map contains that location"<<endl;
    else{
        tt=dic[str];
        int len=tt.size();
        if(len<level)cout<<str<<" at detail level "<<level<<" no map at that detail level; using "<<tt[len-1].name<<endl;
        else cout<<str<<" at detail level "<<level<<" using "<<tt[level-1].name<<endl;
    }
}

int main(){
//    freopen("uva511.txt","r",stdin);
//    freopen("ans.txt", "w", stdout);
    string str;
    int choice;
    while(getline(cin, str)){
        if(str=="MAPS")choice=1;
        else if (str=="LOCATIONS")choice=2;
        else if(str=="REQUESTS")choice=3;
        else if(str=="END")break;
        else{
            stringstream ss(str);
            if(choice==1){
                MAP temp;
                double x1,x2,y1,y2;
                ss>>temp.name>>x1>>y1>>x2>>y2;
                if(x1>x2)swap(x1,x2);
                if(y1>y2)swap(y1, y2);
                temp.x1=x1,temp.x2=x2,temp.y1=y1,temp.y2=y2;
                temp.s=(y2-y1)*(x2-x1);
                mm.push_back(temp);
            }
            else if (choice==2){
                map_locs entry;
                double x,y;string name;
                ss>>name>>x>>y;
                locs.insert(name);
                for(int i=0;i<mm.size();i++){
                    if(mm[i].x1<=x&&x<=mm[i].x2&&mm[i].y1<=y&&y<=mm[i].y2){
                        MAP_LOC temp;
                        temp.name=mm[i].name;
                        temp.x1=mm[i].x1;temp.x2=mm[i].x2;temp.y1=mm[i].y1;temp.y2=mm[i].y2;
                        temp.s=mm[i].s;
                        temp.d0=dis((temp.x1+temp.x2)/2,(temp.y1+temp.y2)/2,x,y);
                        temp.r=abs((temp.y1-temp.y2)/(temp.x1-temp.x2)-0.75);
                        temp.lr=dis(temp.x2,temp.y1,x,y);
                        entry.push_back(temp);
                    }
                }
                if(entry.size()>0){
                    sort(entry.begin(),entry.end(),cmp);
                    dic[name]=entry;
                }
            }
            else if(choice==3){
                string name;int level;
                ss>>name>>level;
                print_result(name,level);
            }
        }
    }
    return 0;
}
