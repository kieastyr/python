#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int red_len = 11;
double red_coeff[] =  {-1.64903754e-36, -2.81699625e-32,  7.24868536e-28,  5.20894510e-24, -6.17439033e-20, -2.52087872e-16,  1.82008814e-12,  3.15384582e-09, -2.05473014e-05,  1.97587418e-02,  2.28442477e+02};
int green_len = 9;
double green_coeff[] = {-1.91231585e-28, -1.87006898e-24,  1.49660342e-20,  1.80884460e-16,  1.19408928e-14, -4.76772607e-09, -1.70751518e-05,  3.02167011e-02,  2.51984061e+02};
int blue_len = 10;
double blue_coeff[] = {-1.79232104e-31, -7.10519519e-28,  1.66525626e-23,  4.84614854e-20, -4.41751965e-16, -6.45627798e-13,  4.15638445e-09, -2.52220696e-06, -2.81728902e-02,  1.48304915e+02};

//多項式計算用関数
int poly_func(int x, double *coeff, int coeff_len){
	int i;
	double sum=0;
	for(i=0;i<coeff_len;i++){
		sum += coeff[i]*pow(x,coeff_len-i-1);
	}
	return (int)sum;
}

//cm_moonに入力する2次元配列img[][]の各要素数もimg_x,img_yとして必要。colorでrgbのどれかを指定する。
void cm_moon(int img_x, int img_y, int img[img_x][img_y], char color, int img_color[img_x][img_y]){
	int len, i, j;
	double *coeff;
	
	//各色に対応して係数と次元数（len-1）を代入
	if(color=='r'){
		len = red_len;
		coeff = (double *)malloc(len*sizeof(double));
		if(coeff==NULL){
			printf("メモリ確保失敗\n");
			exit(1);
		}
		for(i=0;i<len;i++){
			coeff[i] = red_coeff[i];
		}
	}else if(color=='g'){
		len = green_len;
		coeff = (double *)malloc(len*sizeof(double));
		if(coeff==NULL){
			printf("メモリ確保失敗\n");
			exit(1);
		}
		for(i=0;i<len;i++){
			coeff[i] = green_coeff[i];
		}
	}else if(color=='b'){
		len = blue_len;
		coeff = (double *)malloc(len*sizeof(double));
		if(coeff==NULL){
			printf("メモリ確保失敗\n");
			exit(1);
		}
		for(i=0;i<len;i++){
			coeff[i] = blue_coeff[i];
		}
	}
	
	//imgの各要素を計算
	for(j=0;j<img_y;j++){
		for(i=0;i<img_x;i++){
			img_color[i][j] = poly_func(img[i][j], coeff, len);
			if(img_color[i][j]<0) img_color[i][j]=0;
			else if(img_color[i][j]>255) img_color[i][j]=255;
		}
	}
	free(coeff);
}

int main(){
	int img_x=128, img_y=128, i, j;
	int img[img_x][img_y], img_r[img_x][img_y], img_g[img_x][img_y], img_b[img_x][img_y];
	srand((unsigned)time(NULL));
	
	//imgの各要素をランダムで決定
	for(j=0;j<img_y;j++){
		for(i=0;i<img_x;i++){
			img[i][j] = rand()%(7093+8148)-8148;
			printf("%d ", img[i][j]);
		}
	}
	
	cm_moon(img_x, img_y, img, 'r', img_r);
	cm_moon(img_x, img_y, img, 'g', img_g);
	cm_moon(img_x, img_y, img, 'b', img_b);
	
	for(j=0;j<img_y;j++){
		for(i=0;i<img_x;i++){
			printf("%d %d %d\n", img_r[i][j], img_g[i][j], img_b[i][j]);
		}
	}
	return 0;
}