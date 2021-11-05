using tiii = tuple<int,int,int>;

class BIT{
public:
    vector<vector<int>> tree;
    int nw, nd;
    BIT(int nw, int nd){
        this->nw = nw;
        this->nd = nd;
        tree.resize(nw+1);
        for (int i = 0; i <= nw; i++)
            tree[i].assign(nd+1,0);
    }

    int query(int w, int d){
        int res = 0;
        for (int i = w; i > 0; i -= i&(-i)){
            for (int j = d; j > 0; j -= j&(-j)){
                res = max(res, tree[i][j]);
            }
        }
        return res;
    }

    void update(int w, int d, int v){
        for (int i = w; i <= nw; i += i&(-i)){
            for (int j = d; j <= nd; j += j&(-j)){
                tree[i][j] = max(tree[i][j], v);
            }
        }
    }
};

class Solution {
public:
    int pileBox(vector<vector<int>>& box) {
        set<int> ws, ds;
        unordered_map<int,int> w2id, d2id;
        vector<tiii> arr;
        for (auto &b : box){
            ws.insert(b[0]);
            ds.insert(b[1]);
            arr.push_back({b[2],-b[0],-b[1]});
        }
        sort(arr.begin(), arr.end());
        int nw = 0;
        for (auto w : ws) w2id[w] = ++nw;
        int nd = 0;
        for (auto d : ds) d2id[d] = ++nd;
        int res = 0;
        BIT T(nw,nd);
        for (auto &[h,w,d] : arr){
            w = -w; d = -d;
            int ph = T.query(w2id[w]-1,d2id[d]-1);
            res = max(res, ph+h);
            T.update(w2id[w],d2id[d],ph+h);
        }
        return res;
    }
};






















#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

const int MAXN = 3e3 + 5;
const int INF = 0x7fffffff;

int tree[MAXN*4][MAXN*4],n,m,qxl,qxr,qyl,qyr,x,y,val;

bool cmp(vector<int> a, vector<int> b){
    if ((a[2]<b[2])||(a[2]==b[2]&&a[0]>b[0])||(a[2]==b[2]&&a[0]==b[0]&&a[1]>b[1]))return true;
    else return false;
}

class Solution {
public:
    int query_x(int xl, int xr, int vx){
        if(xr<qxl||xl>qxr)return 0;
        if (xl>=qxl&&xr<=qxr)return query_y(xl,xr,vx,0,m,0);
        int xm=(xl+xr)/2;
        return max(query_x(xl,xm,vx*2+1),query_x(xm+1,xr,vx*2+2));
    }
    int query_y(int xl, int xr, int vx, int yl, int yr, int vy){
        if(yr<qyl||yl>qyr)return 0;
        if(yl>=qyl&&yr<=qyr)return tree[vx][vy];
        int ym=(yl+yr)/2;
        return max(query_y(xl,xr,vx,yl,ym,vy*2+1),query_y(xl,xr,vx,ym+1,yr,vy*2+2));
    }
    void update_x(int xl, int xr, int vx){
        if(xl<xr){
            int xm=(xl+xr)/2;
            if(x<=xm)update_x(xl,xm,vx*2+1);
            else update_x(xm+1,xr,vx*2+2);
        }
        update_y(xl,xr,vx,0,m,0);
    }
    void update_y(int xl, int xr, int vx, int yl, int yr, int vy){
        if(yl==yr){
            if(xl==xr)tree[vx][vy]=val;
            else tree[vx][vy]=max(tree[vx*2+1][vy],tree[vx*2+2][vy]);
        }
        else{
            int ym=(yl+yr)/2;
            if(y<=ym)update_y(xl,xr,vx,yl,ym,vy*2+1);
            else update_y(xl,xr,vx,ym+1,yr,vy*2+2);
            tree[vx][vy]=max(tree[vx][vy*2+1],tree[vx][vy*2+2]);
        }
    }
    int pileBox(vector<vector<int>>& box) {
        memset(tree,0,sizeof(tree));
        std::vector<int> ws(1,0),ds(1,0);
        unordered_map<int,int> w2id, d2id;
        sort(box.begin(),box.end(),cmp);
        for (int i = 0; i < box.size(); ++i)
        {
            ws.push_back(box[i][0]);
            ds.push_back(box[i][1]);
        }
        sort(ws.begin(),ws.end());
        sort(ds.begin(),ds.end());
        n = 0;
        for (int i = 1; i < ws.size(); ++i)
        {
            if(ws[i]>ws[i-1])w2id[ws[i]] = ++n;           
        }
        m = 0;
        for (int i = 1; i < ds.size(); ++i)
        {
            if(ds[i]>ds[i-1])d2id[ds[i]] = ++m; 
        }
        // SegmentTree T(n,m);
        for(auto wdh: box){
            x=w2id[wdh[0]];y=d2id[wdh[1]];
            qxl=0;qxr=x-1;qyl=0;qyr=y-1;
            int hsum = query_x(0,n,0);
            val = hsum+wdh[2];
            update_x(0,n,0);
        }
        // for(auto x=w2id.begin();x!=w2id.end();x++)cout<<x->first<<' '<<x->second<<endl;
        qxl=0;qxr=n;qyl=0;qyr=m;
        return query_x(0,n,0);

    }
};



// class Solution {
// public:
//     unordered_map<int,int> seg[3010<<2];
//     int qx1,qy1,qx2,qy2;
//     int x,y,val;
//     int n;
//     int cur;
//     int queryx(int idx, int xleft, int xright){
//         if(xleft>xright || qx1>xright || qx2<xleft) return 0;
//         if(qx1<=xleft && qx2>=xright){
//             int res=queryy(idx,0,0,n);
//             return res;
//         }

//         int mid=(xleft+xright)/2;
//         int l=queryx(idx*2+1,xleft,mid);
//         int r=queryx(idx*2+2,mid+1,xright);
//         return max(l,r);
//     }
//     int queryy(int idx, int idy, int yleft, int yright){
//         if(qy1>yright || qy2<yleft) return 0;
//         if(qy1<=yleft && qy2>=yright) return seg[idx][idy];

//         int mid=(yleft+yright)/2;
//         int l=queryy(idx,idy*2+1,yleft,mid);
//         int r=queryy(idx,idy*2+2,mid+1,yright);
//         return max(l,r);
//     }

//     void updatex(int idx, int xleft, int xright){
//         if(xleft>xright || x<xleft || x>xright) return;
//         if(xleft==xright){
//             updatey(idx,xleft,xright,0,0,n);
//             return;
//         }
//         int mid=(xleft+xright)/2;
//         updatex(idx*2+1,xleft,mid);
//         updatex(idx*2+2,mid+1,xright);
//         updatey(idx,xleft,xright,0,0,n);
//     }

//     void updatey(int idx, int xleft, int xright, int idy, int yleft, int yright){
//         if(yleft>yright || y<yleft || y>yright) return;
//         if(yleft==yright){
//             if(xleft==xright) {
//                 seg[idx][idy]=val;
//             }
//             else seg[idx][idy]=max(seg[idx*2+1][idy],seg[idx*2+2][idy]);
//             return;
//         }
//         int mid=(yleft+yright)/2;
//         updatey(idx,xleft,xright,idy*2+1,yleft,mid);
//         updatey(idx,xleft,xright,idy*2+2,mid+1,yright);
//         seg[idx][idy]=max(seg[idx][idy*2+1],seg[idx][idy*2+2]);
//     }

//     int pileBox(vector<vector<int>>& box) {
//         unordered_map<int,int> wid;
//         unordered_map<int,int> did;
//         sort(box.begin(),box.end(),[](vector<int>& v1, vector<int>& v2){
//             return v1[0]<v2[0];
//         });
//         n=box.size();
//         for(int i=0;i<n;i++){
//             if(i==0) wid[box[i][0]]=1;
//             else {
//                 if(box[i][0]>box[i-1][0]) wid[box[i][0]]=i+1;
//             }
//         }
//         sort(box.begin(),box.end(),[](vector<int>& v1, vector<int>& v2){
//             return v1[1]<v2[1];
//         });
//         for(int i=0;i<n;i++){
//             if(i==0) did[box[i][1]]=1;
//             else {
//                 if(box[i][1]>box[i-1][1]) did[box[i][1]]=i+1;
//             }
//         }
//         sort(box.begin(),box.end(),[](vector<int>& v1, vector<int>& v2){
//             return v1[2]==v2[2]?v1[0]>v2[0]: v1[2]<v2[2];
//         });
      
//         int res=0;
//         vector<int> dp(n,0);
//         for(int i=0;i<n;i++){
//             qx1=0;
//             qy1=0;
//             qx2=wid[box[i][0]]-1;
//             qy2=did[box[i][1]]-1;
//             int q=queryx(0,0,n);
//             dp[i]=q+box[i][2];
//             res=max(res,dp[i]);
//             x=wid[box[i][0]];
//             y=did[box[i][1]];
//             val=dp[i];
//             cur=i;
//             updatex(0,0,n);
//         }
//         return res;
//     }

   
// };