import csv
import numpy as np
import matplotlib.pyplot as plt

sep_length = []
sep_width = []
#IRIS.csvよりデータを取得
with open('IRIS.csv', 'r') as csv_file:
    f = csv.reader(csv_file)
    #sepal lengthとsepal widthはそれぞれcsvファイルの0,1行目
    for row in f:
        sep_length.append(float(row[0]))
        sep_width.append(float(row[1]))

#各要素をnumpy配列に格納
x = np.array(sep_length)
y = np.array(sep_width)
#print(x)

#GD method.
#初期値
Beta = np.array([1.0, 1.0])
#学習率
lr = 0.02
#直線のxの値の設定
pred_x = np.arange(np.min(x), np.max(x), 0.1)
for i in range(10000):
    #2乗誤差のgradientを求める
    e0 = np.mean(2*(y-Beta[1]*x-Beta[0])*(-1))
    e1 = np.mean(2*(y-Beta[1]*x-Beta[0])*(-x))
    E = np.array([e0, e1])
    #βの更新
    Beta = Beta-lr*E
    print(Beta)
    if i==100:
        pred_y100 = Beta[1]*pred_x+Beta[0]
    elif i==1000:
        pred_y1000 = Beta[1]*pred_x+Beta[0]        
    
pred_y10000 = Beta[1]*pred_x+Beta[0]

#データの散布図のプロット
plt.scatter(x,y, label='data', c='blue')
plt.plot(pred_x, pred_y100, 
         label='prediction i=100', c='red', alpha=0.3)
plt.plot(pred_x, pred_y1000, 
         label='prediction i=1000', c='red', alpha=0.5)
plt.plot(pred_x, pred_y10000, 
         label='prediction i=10000', c='red')
plt.title('Sepal Width Prediction from Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()