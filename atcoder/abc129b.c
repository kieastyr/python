#include<stdio.h>
#include<stdlib.h>

int main(){
	int n, i, w[100];
	fscanf(stdin,"%d", &n);
	for(i=0;i<n;i++){
		fscanf(stdin,"%d", &w[i]);
	}
	int cut = 2/n, sum1=0, sum2=0, flag=1, min;
	for(i=0;i<cut;i++) sum1 += w[i];
	for(i=cut;i<n;i++) sum2 += w[i];
	min = sum2-sum1;
	if(min>0){ //sum2>sum1
		while(flag){
			if(min-2*w[cut]<=0 || cut==n-1){
				min = abs(min)<abs(min-2*w[cut])?min:min-2*w[cut];
				flag = 0;
			}else{
				min = min-2*w[cut];
			}
			cut++;
		}
	}else if(min<0){
		while(flag){
			if(min+2*w[cut]>=0 || cut==0){
				min = abs(min)<abs(min+2*w[cut])?min:min+2*w[cut];
				flag = 0;
			}else{
				min = min+2*w[cut];
			}
			cut--;
		}
	}
	printf("%d\n",abs(min));
	return 0;
}
