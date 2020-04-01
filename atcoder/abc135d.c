#include<stdio.h>
#include<math.h>

long long mod = 1000000007;

int main(){
	char s[100002];
	int i,len=0,amari=0;
	fscanf(stdin, "%s", s);
	while(s[len]!='\0') len++;
	for(i=1;i<=len;i++){
		if(s[len-i]>=48 && s[len-i]<=57){
			amari+=(s[len-i]-48)
		}else if(s[len-i]==63){
			
		}
	}
	printf("%d %d", s[0], s[2]);
	return 0;
}