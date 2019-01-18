/* printf example */
#include <stdio.h>
#include<math.h>

int main()
{
	double p=37.9750;
	char ans[10]={0};
	printf("%s\n",ans);
	printf("%d",((int) (p*1000)));
	if(((int) (p*1000))%10>4)printf("%.2f true",p+0.01);
   printf ("Characters: %c %c \n", 'a', 65);
   printf ("Decimals: %d %ld\n", 1977, 650000L);
   printf ("Preceding with blanks: %10d \n", 1977);
   printf ("Preceding with zeros: %010d \n", 1977);
   printf ("Some different radices: %d %x %o %#x %#o \n", 100, 100, 100, 100, 100);
   printf ("floats: %10.2f %+.0e %E \n", 3.1416, 3.1416, 3.1416);
   printf ("Width trick: %*d \n", 5, 10);
   printf ("%s \n", "A string");
   return 0;
}
