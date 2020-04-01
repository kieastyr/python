#include<stdio.h>
#include<stdlib.h>

struct object{
char name[20];
int price;
};


int main(void)
{ 
    int a,l,x,n,m,cost,closest;
    scanf("%d",&a);
    for(l=0;l<a;l++){
        cost=0;closest=100000;
 scanf("%d",&x);
 scanf("%d",&n);
struct object flavors[n];
    int i;
    for (i=0;i<n;i++){ 
scanf("%s",flavors[i].name);
scanf("%d",&flavors[i].price);
}
    scanf("%d",&m);
struct object options[m];  
for (i=0;i<m;i++){ 
scanf("%s",options[i].name);
scanf("%d",&options[i].price); }
 int j,k;
for(i=0;i<n;i++){
    cost=flavors[i].price;
    if(abs(cost-x)<abs(closest-x)){closest=cost;}else if(abs(cost-x)==abs(closest-x)){if(closest>cost)closest=cost;}
    printf("%d\n",closest);
	for(j=0;j<m;j++){
        cost+=options[j].price;
        if(abs(cost-x)<abs(closest-x)){closest=cost;}else if(abs(cost-x)==abs(closest-x)){if(closest>cost)closest=cost;}
        cost-=options[j].price;
	    printf("%d\n",closest);
    }
	for(j=0;j<m;j++){
        cost+=options[j].price;
        for(k=j+1;k<m;k++){
        cost+=options[k].price;
        if(abs(cost-x)<abs(closest-x)){closest=cost;}else if(abs(cost-x)==abs(closest-x)){if(closest>cost)closest=cost;}
        cost-=options[k].price;
		printf("%d\n",closest);
        }
        cost-=options[j].price;
    }
}
    printf("Case #%d: %d\n",l+1,closest);
    
}
}