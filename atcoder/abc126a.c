#include<stdio.h>
#include<math.h>

int main(){
	
	int n, k;
	scanf("%d %d",&n, &k);
	k--;
	char s[n];
	scanf("%s", s);
	if(s[k]=='A'){
		s[k]='a';
	}else if(s[k]=='B'){
		s[k]='b';
	}else{
		s[k]='c';
	}
	printf("%s",s);
	return 0;
}