#include<stdio.h>
#include<math.h>

int main(){
		
	int n, i, j, num, count=0;
	char c;
	scanf("%d", &n);
	int a[n];
	for(i=0; i<n; i++){
		scanf("%d", &a[i]);
	}
	for(j=0; j<n; j++){
		if(a[j]){
			num = a[j]-1;
			i=j+1;
			while(i<n){
				if(a[i]==a[j]){
					a[i]=a[--n];
					num--;
				}else{
					i++;
				}
			}
			//printf("num=%d\n", num);
			if(num>0)	count += a[j]-num;
			else if(num<0)	count -= num;
		}
	}
	printf("%d\n", count);
	return 0;
}