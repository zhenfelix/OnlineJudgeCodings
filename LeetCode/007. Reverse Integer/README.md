```c++
class Solution {
public:
    int reverse(int x) {
        int num=x;
        int sum=0;
        int pnum=0;
        while(num)
        {
            int temp=num%10;
            sum=sum*10+temp;
            if((sum-temp)/10!=pnum)//determine whethere it is reversible
                return 0;
            pnum=sum;
            num=num/10;
        }
        return sum;
    }
};
```
