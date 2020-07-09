from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as R2
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA  # 主成分分析器
import sys
import pickle
import pandas as pd


# データセットの読み込み
df = pd.read_csv("dataset.csv")
df.info()

# 標準化 -> pca
df_std = df.iloc[:, 2:10].apply(lambda x: (x-x.mean())/x.std(), axis=0)
df_std.info()
pca = PCA()
pca.fit(df_std)
feature = pca.transform(df_std)
df_pca = pd.DataFrame(feature, columns=[f"PC{x+1}" for x in range(len(df_std.columns))])
df_pca.head()

# データセットから説明変数と回帰対象の変数を取り出し(今回はWater Solubilityを回帰)
best_score = 0.0
best_model = None
for max_var in range(1, len(df_pca.columns)):
    print(f"PC num:{max_var}")
    X = df_pca[[f"PC{i+1}" for i in range(max_var)]]
    y = df["Water Solubility"]

    # 学習用と評価用にデータを分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 線形回帰
    model = LR()
    model.fit(X_train, y_train)
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # 決定係数R2でモデルの性能評価
    print("Train score: ", R2(y_train, y_train_pred))
    test_score = R2(y_test, y_test_pred)
    print("Test score: ", test_score)
    if test_score > best_score:
        print(f"PC num:{max_var} is Best!")
        best_score = test_score
        best_model = model

# モデルの保存
pickle.dump(best_model, open("src/mymodel.pkl", "wb"))
