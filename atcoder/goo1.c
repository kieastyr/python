#include<stdio.h>

int main(void){
	int x, n, m, i, j, k, closest=0;
	struct object{
		char name[20];
		int price;
	};
	scanf("%d", &x);
	scanf("%d", &n);
	struct object flavor[n]; 
	for(i=0;i<n;i++) scanf("%s %d", flavor[i].name, &flavor[i].price);
	scanf("%d", &m);
	struct object option[m];
	for(i=0;i<m;i++) scanf("%s %d", option[i].name, &option[i].price);
	
	for(i=0;i<m;i++){
		closest();
	}
	
	return 0;
}