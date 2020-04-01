#include<stdio.h>
#include<math.h>

int main(){
	
	int i, smin, tmax, snum=0, tnum=0, num, count;
	char s[256], t[256];
	scanf("%s", s);
	scanf("%s", t);
	while(s[++snum]!='\0');
	while(t[++tnum]!='\0');
	num = snum<tnum?snum:tnum;
	for(count=0; count<num;count++){
		smin=0;
		tmax=0;
		i=-1;
		while(s[++i] != '\0')	if(s[i] < s[smin])	smin = i;
		i=-1;
		while(t[++i] != '\0')	if(t[i] > t[tmax])	tmax = i;
		if(s[smin]<t[tmax]){
			printf("Yes\n");
			break;
		}else if(s[smin]==t[tmax]){
			s[smin] = 'z'+1;
			t[tmax] = 'a'-1;
		}else{
			printf("No\n");
			break;
		}
	}
	if(count==num){	
		if(snum<tnum)	printf("Yes\n");
		else	printf("No\n");
	}
	return 0;
}