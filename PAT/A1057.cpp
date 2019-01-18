// #include <iostream>
// #include <string>
// #include <cmath>
// #include <cstdio>
// #include <vector>
// #include <set>
// #include <map>
// #include <stack>
// #include <unordered_set>
// #include <algorithm>
// using namespace std;


// int main()
// {
//     // freopen("input.txt","r",stdin);
//     int n;
//     stack<int> st;
//     vector<int> nums;
//     string str;
//     cin>>n;
//     while (n--) {
//         cin>>str;
//         if(str=="Pop"){
//             if(st.size()==0)cout<<"Invalid"<<endl;
//             else {
//                 cout<<st.top()<<endl;
//                 int idx=nums.size()-1;
//                 while (idx>=0) {
//                     if(st.top()==nums[idx])break;
//                     idx--;
//                 }
//                 nums.erase(nums.begin()+idx);
//                 st.pop();
//             }
//         }
//         else if(str=="PeekMedian"){
//             if(st.size()==0)cout<<"Invalid"<<endl;
//             else {
//                 cout<<nums[(nums.size()-1)/2]<<endl;
//             }
//         }
//         else {
//             int x; cin>>x;
//             st.push(x);
//             int idx=nums.size()-1;
//             while (idx>=0) {
//                 if(x>nums[idx])break;
//                 idx--;
//             }
//             idx++;
// //            if(idx==nums.size())nums.push_back(x);
// //            else
//                 nums.insert(nums.begin()+idx, x);
//         }
//     }
//     return 0;
// }

//time exceeded



#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <unordered_set>
#include <algorithm>
using namespace std;

const int maxn=100010;

int main()
{
    freopen("input.txt","r",stdin);
    int n=sqrt(maxn),m;
    stack<int> st;
    vector<int> table(maxn,0),blocks(maxn/n+1,0),ans;
    string str;
    cin>>m;
    while (m--) {
        cin>>str;
        if(str=="Pop"){
            if(st.size()==0)cout<<"Invalid"<<endl;
            else {
                int x=st.top();
                st.pop();
                table[x]--;
                blocks[(x-1)/n]--;
                cout<<x<<endl;
            }
        }
        else if(str=="PeekMedian"){
            if(st.size()==0)cout<<"Invalid"<<endl;
            else {
                int k,len=st.size();
                k=(len+1)/2;
                int id_block=0;
                while (k>0) {
                    k-=blocks[id_block++];
                }
                id_block--;
                k+=blocks[id_block];
                int x=n*id_block+1;
                while (k>0) {
                    k-=table[x++];
                }
                x--;
                cout<<x<<endl;
            }
        }
        else {
            int x; cin>>x;
            st.push(x);
            table[x]++;
            blocks[(x-1)/n]++;
            }
    }
    return 0;
}

//分块的思想
// cut into blocks
//1057. Stack (30)五种解法总结（大杂烩）
//https://blog.csdn.net/sinat_29278271/article/details/47291659


# include <cstdio>
# include <stack>
using namespace std;
class BIT
{
private:
    int *Elem;
    int Size;
    int lowbit(int n)
    {
        return n&(-n);
    }
public:
    BIT(int size):Size(size+1)  /*想想看还是+1好了，要不申请了100的空间只能用到99感觉太奇怪了*/
    { 
        Elem = new int[Size];
        for (int i=0;i<Size;i++)/*还没试过用memset初始化，下次试试*/
            Elem[i] = 0;
    }
    int GetSum(int right)/*[0,right]*/
    {
        int sum = 0;
        while (right)
        {
            sum += Elem[right];
            right -= lowbit(right);
        }
        return sum;
    }
    int GetSum(int left,int right)/*[left,right]*/
    {
        return GetSum(left-1) - GetSum(right);
    }
    void Add(int value,int index)
    {
        while (index < Size)
        {
            Elem[index] += value;
            index += lowbit(index);
        } 
    }
    ~BIT()
    {
      delete[] Elem;
    }
};
BIT bit(100000);
int getmid(int size)
{
    int index = (size+1)/2;
    int left = 1,right = 100000,mid;
    while(left<right)
    {
        mid = (left+right)/2;
        if(bit.GetSum(mid)<index)
            left = mid+1;
        else
            right = mid;
    }
    return left;
}
int main()
{
  int n,tmp;
  scanf("%d",&n);
  stack<int> s;
  char str[10];
  while (n--)
  {
      scanf("%s",str);
      switch(str[1])
      {
          case 'e':
              {
              if (s.empty()) 
                  printf("Invalid\n");
              else 
                  printf("%d\n",getmid(s.size()));
              break;
              }
          case 'o':
              {
              if (s.empty())
                  printf("Invalid\n");
              else 
                  {
                  tmp = s.top();s.pop();
                  printf("%d\n",tmp);
                  bit.Add(-1,tmp);
                  }
              break;
              }
          case 'u':
              {
                  scanf("%d",&tmp);s.push(tmp);
                  bit.Add(1,tmp);
              }
              break;
      }
  }
  return 0;
}
//树状数组+二分查找
