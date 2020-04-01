#include<stdio.h>

int main(){
	
	int n;
	fscanf(stdin,"%d", &n);
	if((n%4==2 && n<14)||(n%4==1 && n<21)||(n&4==3 && n<7)){
		printf("No\n");
	}else{
		printf("Yes\n");
	}
	return 0;
}