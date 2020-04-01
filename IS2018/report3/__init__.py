import csv
import numpy as np
import matplotlib.pyplot as plt

#aとbの距離を返す。ここでa,bの要素数はそれぞれ4を想定
def culc_dist(a, b):
    return np.sqrt(np.sum(np.square(a-b)))

#aとbの距離を返す。aの要素数は2×n、bの要素数は2
def max_dist(a, b):
    b = b[:, np.newaxis]
    dist = np.sqrt(np.sum(np.square(a-b), axis=0))
    return np.max(dist)

sep_width = [[0 for i in range(0)] for j in range(3)]
sep_length = [[0 for i in range(0)] for j in range(3)]
pet_width = [[0 for i in range(0)] for j in range(3)]
pet_length = [[0 for i in range(0)] for j in range(3)]
#IRIS.csvよりデータを取得
with open('IRIS.csv', 'r') as csv_file:
    f = csv.reader(csv_file)
    #row1~5がsepal length,sepal width,petal length,petal width, classに対応
    for row in f:
        if row[4] == 'Iris-setosa':
            sep_length[0].append(float(row[0]))
            sep_width[0].append(float(row[1]))
            pet_length[0].append(float(row[2]))
            pet_width[0].append(float(row[3]))
        elif row[4] == 'Iris-versicolor':
            sep_length[1].append(float(row[0]))
            sep_width[1].append(float(row[1]))
            pet_length[1].append(float(row[2]))
            pet_width[1].append(float(row[3]))
        elif row[4] == 'Iris-virginica':
            sep_length[2].append(float(row[0]))
            sep_width[2].append(float(row[1]))
            pet_length[2].append(float(row[2]))
            pet_width[2].append(float(row[3]))           
#データ数
n = np.array(sep_length).size
#各データに対応する要素で4次元データxとする
x = np.empty([4,n])
x[0,:] = np.reshape(np.array(sep_length), [-1,])
x[1,:] = np.reshape(np.array(sep_width), [-1,])
x[2,:] = np.reshape(np.array(pet_length), [-1,])
x[3,:] = np.reshape(np.array(pet_width), [-1,])
# print(x)

#重心をランダムに初期化(重心3つ×4次元)
centroid = np.empty([3,4])
for i in range(4):
    #np.min(x[i])からnp.max(x[i])までの任意の値をとる
    centroid[:,i] = np.min(x[i])+(np.max(x[i])-np.min(x[i]))*np.random.rand(3)
# print(centroid)

#ラベルをランダムに初期化（各データに対し0,1,2のいずれか）
clustering = np.random.randint(0, 3, size=n)
# print(clustering)

#繰り返しの終了を判別するフラグ
flag = True
#試行回数
num = 0
while(flag):
    flag = False
    num += 1
    #重心の更新
    for k in range(3):
        for i in range(4):
            centroid[k,i] = np.mean(x[i,np.where(clustering==k)], axis=1)
    #ラベルを最も近いものに更新
    for j in range(n):
        distance = [culc_dist(x[:,j], centroid[k,:]) for k in range(3)]
        if np.argmin(distance) != clustering[j]:
            #更新があればまだ試行を続ける
            flag = True
            clustering[j] = np.argmin(distance)
    print(num, clustering)


#データのプロット
label_list = [['setora', 'blue'], ['versicolor', 'green'], ['verginica', 'red']]
#Sepal WidthとSepal lengthでの表示
fig = plt.figure()
ax = fig.add_subplot(111)
#k=3のそれぞれでプロット
for k, index in enumerate(label_list):
    #散布図のプロット
    plt.scatter(np.reshape(x[0,np.where(clustering==k)],[-1]),
                np.reshape(x[1,np.where(clustering==k)],[-1]),
                label=index[0], c=index[1])
    #クラスkに分類されたデータの座標の取得
    coordinates = np.reshape(np.array([x[0,np.where(clustering==k)],
                x[1,np.where(clustering==k)]]), [2,-1])
    #中心を重心、半径をそこから最も遠い点までの距離とした円の描画
    c = plt.Circle((centroid[k,0],centroid[k,1]), 
               np.max(max_dist(coordinates,centroid[k,[0,1]])), 
               color=index[1] ,fill=False)
    #重心のプロット
    plt.scatter(centroid[k,0], centroid[k,1], c=index[1], marker='X')
    ax.add_patch(c)
    plt.title('k-means clustering in Sepal Width - Sepal length')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()

#Petal WidthとPetal lengthでの表示
fig = plt.figure()
ax = fig.add_subplot(111)
for k, index in enumerate(label_list):
    #散布図のプロット
    plt.scatter(np.reshape(x[2,np.where(clustering==k)],[-1]),
                np.reshape(x[3,np.where(clustering==k)],[-1]),
                label=index[0], c=index[1])
    #クラスkに分類されたデータの座標の取得
    coordinates = np.reshape(np.array([x[2,np.where(clustering==k)],
                x[3,np.where(clustering==k)]]), [2,-1])
    #中心を重心、半径をそこから最も遠い点までの距離とした円の描画
    c = plt.Circle((centroid[k,2],centroid[k,3]), 
               np.max(max_dist(coordinates,centroid[k,[2,3]])), 
               color=index[1] ,fill=False)
    #重心のプロット
    plt.scatter(centroid[k,2], centroid[k,3], c=index[1], marker='X')
    ax.add_patch(c)
    plt.title('k-means clustering in Petal Width - Petal length')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
plt.show()

#Petal LengthとSepal lengthでの表示
fig = plt.figure()
ax = fig.add_subplot(111)
for k, index in enumerate(label_list):
    #散布図のプロット
    plt.scatter(np.reshape(x[0,np.where(clustering==k)],[-1]),
                np.reshape(x[2,np.where(clustering==k)],[-1]),
                label=index[0], c=index[1])
    #クラスkに分類されたデータの座標の取得
    coordinates = np.reshape(np.array([x[0,np.where(clustering==k)],
                x[2,np.where(clustering==k)]]), [2,-1])
    #中心を重心、半径をそこから最も遠い点までの距離とした円の描画
    c = plt.Circle((centroid[k,0],centroid[k,2]), 
               np.max(max_dist(coordinates,centroid[k,[0,2]])), 
               color=index[1] ,fill=False)
    #重心のプロット
    plt.scatter(centroid[k,0], centroid[k,2], c=index[1], marker='X')
    ax.add_patch(c)
    plt.title('k-means clustering in Petal Length - Sepal length')
plt.xlabel('sepal Length')
plt.ylabel('Petal Length')
plt.legend()
plt.show()

#Sepal WidthとPetal lengthの表示
fig = plt.figure()
ax = fig.add_subplot(111)
for k, index in enumerate(label_list):
    #散布図のプロット
    plt.scatter(np.reshape(x[1,np.where(clustering==k)],[-1]),
                np.reshape(x[3,np.where(clustering==k)],[-1]),
                label=index[0], c=index[1])
    #クラスkに分類されたデータの座標の取得
    coordinates = np.reshape(np.array([x[1,np.where(clustering==k)],
                x[3,np.where(clustering==k)]]), [2,-1])
    #中心を重心、半径をそこから最も遠い点までの距離とした円の描画
    c = plt.Circle((centroid[k,1],centroid[k,3]), 
               np.max(max_dist(coordinates,centroid[k,[1,3]])), 
               color=index[1] ,fill=False)
    #重心のプロット
    plt.scatter(centroid[k,1], centroid[k,3], c=index[1], marker='X')
    ax.add_patch(c)
    plt.title('k-means clustering in Sepal Width - Petal length')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.legend()
plt.show()
    