#include<stdio.h>
#include<math.h>

int main(){
	
	int a, b, c;
	char s[256];
	scanf("%d", &a);
	scanf("%d %d", &b, &c);
	scanf("%s", s);
	printf("%d %s\n", a+b+c, s);
	
	return 0;
}