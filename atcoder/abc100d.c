#include<stdio.h>
#include<stdlib.h>


long long int temp(int i, long long int xsum, long long int ysum, long long int zsum, int num, long long int *x, long long int *y, long long int *z){
	
	if(i==-1){
		if(num==0){
			return llabs(xsum)+llabs(ysum)+llabs(zsum);
		}else{
			return 0;
		}
	}
	if(i==num-1){
		int j;
		for(j=i;j>=0;j--){
			xsum += x[i];
			ysum += y[i];
			zsum += z[i];
		}
		return llabs(xsum)+llabs(ysum)+llabs(zsum);
	}else{
		long long int a,b;
		a = temp(i-1, xsum+x[i], ysum+y[i], zsum+z[i], num-1, x, y, z);
		b = temp(i-1, xsum, ysum, zsum, num, x, y, z);
		if(a>b){
			return a;
		}else{
			return b;
		}
	}
	
}

int main(){
	int n, m, i;
	fscanf(stdin, "%d %d", &n, &m);
	long long int x[n], y[n], z[n];
	for(i=0; i<n; i++){
		fscanf(stdin, "%lld %lld %lld", &x[i], &y[i], &z[i]);
		//printf("%lld\n",x[i]);
	}
	printf("%lld\n",temp(n-1, 0, 0, 0, m, x, y, z));
	return 0;
}