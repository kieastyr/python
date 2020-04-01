#include<stdio.h>

int main(){
	
	int n, i, count=0;
	fscanf(stdin, "%d", &n);
	int a[n];
	for(i=0; i<n; i++){
		fscanf(stdin, "%d", &a[i]);
		while(a[i]%2==0){
			count++;
			a[i] /= 2;
		}
	}
	printf("%d\n", count);
	return 0;
}