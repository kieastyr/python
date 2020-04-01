#include<stdio.h>
#include<math.h>

int try(int *a, int i, int sum, int n){
	if(i==0){
		if(sum+a[i]==n)	return 0;
		else	return 1;
	}else{
		return try(a, i-1, sum+a[i], n)*try(a, i-1, sum-a[i], n);
	}
}

int main(){
		
	char s[8000];
	int x, y, i=-1, j=0, k=0, dir=1, tox[4000] = {}, toy[4000] = {};
	scanf("%s", s);
	scanf("%d %d", &x, &y);
	while(s[++i]!='\0'){
		if(s[i]=='F'){
			if(dir==1)	tox[j]++;
			else	toy[k]++;
		}else{
			dir*=-1;
			if(dir==1)	j++;
			else	k++;
		}
	}/*
	for(i=0;i<=j;i++){
		printf("%d ",tox[i]);
	}
	printf("\n");
	for(i=0;i<=k;i++){
		printf("%d ",toy[i]);
	}
	printf("\n");
	printf("%d %d\n", try(tox, j, 0, x), try(toy, k, 0, y));
	*/
	if(try(tox, j, 0, x)==0 && try(toy, k, 0, y)==0)	printf("Yes\n");
	else	printf("No\n");
	return 0;
}