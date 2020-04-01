#include<stdio.h>

int main(){
	
	int n,k, out;
	fscanf(stdin,"%d %d", &n, &k);
	if(n%k==0){
		out = 0;
	}else{
		out = 1;
	}
	printf("%d", out);
		
	return 0;
}