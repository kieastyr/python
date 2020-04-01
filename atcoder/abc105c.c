#include<stdio.h>
#include<math.h>

int power(int a, int b){
	int i, ans=1;
	for(i=0; i<b; i++){
		ans *= a;
	}
	return ans;
}

int *getBinary(int n){
	int i;
	int out[]=0;
	for(i=0;n!=0;i++){
		if(n%2==1){
			out += power(10,i);
			n -= 1;
		}
		n /= 2;
	}
	return out;
}

int main(){
	int n, out=0;
	fscanf(stdin,"%d", &n);
	/*if(n<=-2){
		n /= -2;
		
	}*/
		printf("%lld\n", getBinary(n));
	return 0;
}
