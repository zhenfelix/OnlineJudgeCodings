#include <cstdio>
#include <cmath>
#include <algorithm>
typedef long long LL;
int main() {
    int n;
    scanf("%d", &n);
    // sqrtΪ����N��ansLenΪ�����������ansIΪ��Ӧ�ĵ�һ������
    int sqr = (int)sqrt(1.0 * n), ansI = 0, ansLen = 0;
    for(int i = 2; i <= sqr; i++) {    // ���������ĵ�һ������
        int temp = 1, j = i;    // tempΪ��ǰ���������ĳ˻�
        while(1) {    // ��j��i��ʼ���ϼ�1������ܵ�����
            temp *= j;    // ��õ�ǰ���������ĳ˻�
            if(n % temp != 0) break;    // �����������n����ô��������
            if(j - i + 1 > ansLen) {    // �����˸����ĳ���
                ansI = i;    // ���µ�һ������
                ansLen = j - i + 1;    // ���������
            }
            j++;    // j��1����һ������
        }
    }
    if(ansLen == 0) {    // ��󳤶�Ϊ0��˵������n��Χ��û�н�
        printf("1\n%d", n);    // ���n����
    } else {
        printf("%d\n", ansLen);    // �����󳤶�
        for(int i = 0; i < ansLen; i++) {
            printf("%d", ansI + i);    // ���[ansI,ansI+ansLen)
            if(i < ansLen - 1) {
                printf("*");    // �������ĳ˺�
            }
        }
    }
    return 0;
}

