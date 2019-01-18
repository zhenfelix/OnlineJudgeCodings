binary search exceed time limits
```c++
class Solution {
public:
    int mySqrt(int x) {
        int left=1,right=x;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(mid*mid==x)return mid;
            else if(mid*mid>x){
                right=mid-1;
            }
            else left=mid+1;
        }
        return right;
    }
};
```

correction by considering very large number x
```c++
class Solution {
public:
    int mySqrt(int x) {
        int left=1,right=x;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(mid==x/mid&&mid*mid==x)return mid;
            else if(mid>x/mid){
                right=mid-1;
            }
            else left=mid+1;
        }
        return right;
    }
};
```


simple Solution
```c++
class Solution {
public:
    int mySqrt(int x) {

        long r = x;

        while (r * r > x){
            r = (r + x/r)/2;
        }

        return r;

    }
};
```
