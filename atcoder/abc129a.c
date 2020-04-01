#include<stdio.h>
#include<math.h>

int main(){
	int p, q, r;
	fscanf(stdin,"%d %d %d", &p, &q, &r);
	if(p<q){
		if(q<r) printf("%d\n", p+q);
		else printf("%d\n", p+r);
	}else if(p<r) printf("%d\n", p+q);
	else printf("%d\n", q+r);
	return 0;
}
