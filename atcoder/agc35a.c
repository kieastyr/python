#include<stdio.h>
#include<stdlib.h>

int main(){
	int i, n, a[100000];
	fscanf(stdin,"%d", &n);
	for(i=0;i<n;i++){
		fscanf(stdin,"%d", &a[i]);
	}
	for(i=0;i<n;i++){
		if(a[(i-1)%n]^a[(i+1)%n]==a[i]){
			
		}
	}
	return 0;
}
