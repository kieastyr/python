#include<stdio.h>
#include<stdlib.h>

int n, m, a[100000];
long long fibo[100000];

long long ans_fibo(int i){
	if(fibo[i]==-1){
		fibo[i] = ans_fibo(i-1)+ans_fibo(i-2);
	}else return fibo[i];
}

int main(){
	int i, pre_a=-1;
	long long count=1;
	fscanf(stdin,"%d %d", &n, &m);
	for(i=0;i<m;i++){
		fscanf(stdin,"%d", &a[i]);
	}
	for(i=0;i<n;i++){
		fibo[i]=-1;
	}
	fibo[2] = 1;
	fibo[3] = 1;
	for(i=0;i<m;i++){
		if(a[i]-pre_a==1){
			printf("%d\n", 0);
			return 0;
		}else{
			count *= ans_fibo(a[i]-pre_a);
			count %= 1000000007;
			pre_a = a[i];
		}
	}
	count *= ans_fibo(n-pre_a+1);
	printf("%lld\n",count%1000000007);
	return 0;
}
