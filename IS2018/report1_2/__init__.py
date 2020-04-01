import csv
import numpy as np
import matplotlib.pyplot as plt

#xにsigmoid関数を通した値を返す
def sigmoid(x):
    return 1/(1+np.exp(-1*x))

#xにsigmoid関数の微分を通した値を返す
def d_sigmoid(x):
    return (1-sigmoid(x))*sigmoid(x)

pet_width = [[0 for i in range(0)] for j in range(2)]
pet_length = [[0 for i in range(0)] for j in range(2)]
#IRIS.csvよりデータを取得
with open('IRIS.csv', 'r') as csv_file:
    f = csv.reader(csv_file)
    #petal length,petal width,classはそれぞれcsvファイルの2,3,4行目
    for row in f:
        if row[4] == 'Iris-setosa':
            pet_length[0].append(float(row[2]))
            pet_width[0].append(float(row[3]))
        if row[4] == 'Iris-versicolor':
            pet_length[1].append(float(row[2]))
            pet_width[1].append(float(row[3]))

#各要素を2*nのnumpy配列に格納
x2d = np.array(pet_length)
y2d = np.array(pet_width)
#print(x2d)
#GD method.
#初期値
Beta = np.array([1.0, 1.0])
#学習率
lr = 0.2
#直線のxの値の設定
pred_x = np.arange(np.min(x2d), np.max(x2d), 0.1)
n = len(pred_x)
for i in range(10000):
    #2乗誤差のgradientを求める
    #予測値y_hatはｈ（ｘ）=b1*x+b2にsigmoidを通したもの
    for j in range(2):
        #x2d[0]はラベル0のsetosa
        de_00 = 2*(0-sigmoid(Beta[1]*x2d[0]+Beta[0]))*(-d_sigmoid(Beta[1]*x2d[0]+Beta[0]))*1
        de_01 = 2*(0-sigmoid(Beta[1]*x2d[0]+Beta[0]))*(-d_sigmoid(Beta[1]*x2d[0]+Beta[0]))*x2d[0]
        #x2d[1]はラベル1のversicolor
        de_10 = 2*(1-sigmoid(Beta[1]*x2d[1]+Beta[0]))*(-d_sigmoid(Beta[1]*x2d[1]+Beta[0]))*1
        de_11 = 2*(1-sigmoid(Beta[1]*x2d[1]+Beta[0]))*(-d_sigmoid(Beta[1]*x2d[1]+Beta[0]))*x2d[1]
        #各ラベルでの誤差を結合し平均をとる
        de_0 = np.mean(np.concatenate([de_00, de_10]))
        de_1 = np.mean(np.concatenate([de_01, de_11]))
    dE = np.array([de_0, de_1])
    #βの更新
    Beta = Beta-lr*dE
    print(Beta)
    if i==100:
        pred_y100 = Beta[1]*pred_x+Beta[0]
    elif i==1000:
        pred_y1000 = Beta[1]*pred_x+Beta[0]        
    
pred_y10000 = Beta[1]*pred_x+Beta[0]

#データの散布図のプロット
plt.scatter(x2d[0],y2d[0], label='setora', c='blue')
plt.scatter(x2d[1],y2d[1], label='versicolor', c='green')
plt.plot(pred_x, pred_y100, 
         label='prediction i=100', c='red', alpha=0.3)
plt.plot(pred_x, pred_y1000, 
         label='prediction i=1000', c='red', alpha=0.5)
plt.plot(pred_x, pred_y10000, 
         label='prediction i=10000', c='red')
plt.title('Discrimination of Setosa & Versicolor')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.ylim(-1,4)
plt.legend()
plt.show()