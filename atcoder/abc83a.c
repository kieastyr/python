#include<stdio.h>
#include<math.h>

int main(){
	int a, b, c, d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	
	if(a+b == c+d)	printf("Balanced\n");
	else if	(a+b > c+d) printf("Left\n");
	else	printf("Right\n");
	
}
