class Solution {
public:
    double myPow(double x, int n) {
        if(n<0)x=1/x,n=-(n);
        if(n<0)return x*myPow(x,-(n+1));//n=INT_MIN
        if(n==0)return 1;
        double ans=myPow(x,n/2);
        ans*=ans;
        if(n%2==1)ans*=x;
        return ans;
    }
};