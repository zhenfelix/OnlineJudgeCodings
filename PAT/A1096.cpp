#include <cstdio>
#include <cmath>
#include <algorithm>
typedef long long LL;
int main() {
    int n;
    scanf("%d", &n);
    // sqrt为根号N，ansLen为最长连续整数，ansI为对应的第一个整数
    int sqr = (int)sqrt(1.0 * n), ansI = 0, ansLen = 0;
    for(int i = 2; i <= sqr; i++) {    // 遍历连续的第一个整数
        int temp = 1, j = i;    // temp为当前连续整数的乘积
        while(1) {    // 让j从i开始不断加1，看最长能到多少
            temp *= j;    // 获得当前连续整数的乘积
            if(n % temp != 0) break;    // 如果不能整除n，那么结束计算
            if(j - i + 1 > ansLen) {    // 发现了更长的长度
                ansI = i;    // 更新第一个整数
                ansLen = j - i + 1;    // 更新最长长度
            }
            j++;    // j加1，下一个整数
        }
    }
    if(ansLen == 0) {    // 最大长度为0，说明根号n范围内没有解
        printf("1\n%d", n);    // 输出n本身
    } else {
        printf("%d\n", ansLen);    // 输出最大长度
        for(int i = 0; i < ansLen; i++) {
            printf("%d", ansI + i);    // 输出[ansI,ansI+ansLen)
            if(i < ansLen - 1) {
                printf("*");    // 输出间隔的乘号
            }
        }
    }
    return 0;
}

