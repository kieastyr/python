from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as R2
from sklearn.decomposition import PCA  # 主成分分析器
import sys
import pickle
import pandas as pd
import lightgbm as lgb

max_var = 14
eps = 1e-20


def main():
    # 保存したモデルの読み込み
    model = pickle.load(open("src/mymodel.pkl", "rb"))

    # 標準入力からデータの読み込み
    input_data = []
    for line in sys.stdin:
        input_data.append(line.strip().split(","))

    df = pd.DataFrame(data=input_data[1:], columns=input_data[0])
    # 標準化 -> pca
    df_std = df.iloc[:, 2:102].astype(float).apply(lambda x: (x-x.mean())/(x.std()+eps), axis=0)
    pca = PCA()
    pca.fit(df_std)
    feature = pca.transform(df_std)
    df_pca = pd.DataFrame(feature, columns=[f"PC{x + 1}" for x in range(len(df_std.columns))])

    # 読み込んだモデルで回帰
    X = df_pca[[f"PC{i + 1}" for i in range(max_var)]]
    # X = df[["MaxEStateIndex", "MinEStateIndex"]]
    y_pred = model.predict(X)

    # 結果を標準出力
    for output in y_pred:
        print(output)


if __name__ == "__main__":
    main()
