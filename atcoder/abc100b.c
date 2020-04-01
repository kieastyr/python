#include<stdio.h>

int main(){
	
	int d,n,temp=1;
	fscanf(stdin, "%d %d", &d, &n);
	switch(d){
		case 2:
			temp *= 100;
		case 1:
			temp *= 100;
	}
	if(n==100){
		n += 1;
	}
	printf("%d\n", n*temp);
	return 0;
}