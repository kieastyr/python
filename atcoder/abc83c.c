#include<stdio.h>
#include<math.h>

int main(){
	long long int x,y;
	int count=0;
	scanf("%lld %lld",&x,&y);
	while(x<=y){
		x*=2;
		count++;
	}
	printf("%d\n",count);
}
