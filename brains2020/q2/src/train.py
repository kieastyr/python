from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as R2
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.decomposition import PCA  # 主成分分析器
import sys
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb
import warnings

warnings.simplefilter('ignore', FutureWarning)
eps = 1e-20

# データセットの読み込み
df = pd.read_csv("dataset.csv")
df.info()

# 標準化 -> pca
df_std = df.iloc[:, 2:102].astype(float).apply(lambda x: (x - x.mean()) / (x.std() + eps), axis=0)
df_std.info()
pca = PCA()
pca.fit(df_std)
feature = pca.transform(df_std)
df_pca = pd.DataFrame(feature, columns=[f"PC{x + 1}" for x in range(len(df_std.columns))])
df_pca.to_csv("src/dataset_pca.csv")

# データセットから説明変数と回帰対象の変数を取り出し(今回はWater Solubilityを回帰)
best_num = 0
best_score = 0.0
best_model = None
test_score_dict = {}
for max_var in range(30, len(df_std.columns) // 2 + 1, 3):
    X = df_pca[[f"PC{i + 1}" for i in range(max_var)]]
    # if True:
    #     X = df_pca[[f"PC{i+1}" for i in range(5)]]
    y = df["Water Solubility"]

    # 学習用と評価用にデータを分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # xgboost
    model = xgb.XGBRegressor(random_state=17, silent=True)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    xgb_params = {'objective': 'reg:squarederror',
                  'eval_metric': 'rmse',
                  # 'learning_rate': 0.1, 'max_depth': 10,
                  # 'subsample': 0.85, 'colsample_bytree': 0.5
                  }

    # 学習時に用いる検証用データ
    evals = [(dtrain, 'train'), (dtest, 'eval')]
    # 学習過程を記録するための辞書
    evals_result = {}
    model = xgb.train(xgb_params,
                      dtrain,
                      num_boost_round=100,  # ラウンド数を増やしておく
                      evals=evals,
                      evals_result=evals_result,
                      )
    y_train_pred = model.predict(dtrain)
    y_test_pred = model.predict(dtest)

#     model = xgb.XGBRegressor(random_state=17, silent=True)
#     params = {'learning_rate': [0.05, 0.1], 'max_depth': [3, 5, 10, 100],
#               'subsample': [0.8, 0.85, 0.9, 0.95], 'colsample_bytree': [0.5, 1.0]}
#     # StratifiedKFoldでグリッドサーチ
#     # skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
#     cv = GridSearchCV(estimator=model, param_grid=params,
#                       cv=5, scoring="neg_mean_squared_error", n_jobs=1, verbose=0)
#     cv.fit(X_train, y_train)
#     y_train_pred = cv.predict(X_train)
#     y_test_pred = cv.predict(X_test)
#
    # 決定係数R2でモデルの性能評価
    test_score = R2(y_test, y_test_pred)
    print("max_var ", max_var)
    print("Train score: ", R2(y_train, y_train_pred))
    print("Test score: ", test_score)
    test_score_dict[max_var] = test_score
    # # 決定係数R2でモデルの性能評価
    # test_score = R2(y_test, y_test_pred)
    # if test_score > best_score:
    #     print("Train score: ", R2(y_train, y_train_pred))
    #     print("Test score: ", test_score)
    #     print(f"PC num:{max_var} is Best!")
    #     best_num = max_var
    #     best_score = test_score
    #     best_model = model

for k, v in test_score_dict.items():
    print(f"{k}: {v}")

n = int(input("choose PC num>"))
X = df_pca[[f"PC{i + 1}" for i in range(n)]]
y = df["Water Solubility"]

# 学習用と評価用にデータを分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# xgboost
model = xgb.XGBRegressor(random_state=17, silent=True)

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

xgb_params = {
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse',
    # 'learning_rate': 0.1, 'max_depth': 10,
    # 'subsample': 0.85, 'colsample_bytree': 0.5
}

# 学習時に用いる検証用データ
evals = [(dtrain, 'train'), (dtest, 'eval')]
# 学習過程を記録するための辞書
evals_result = {}
model = xgb.train(xgb_params,
                  dtrain,
                  num_boost_round=100,  # ラウンド数を増やしておく
                  evals=evals,
                  evals_result=evals_result,
                  )
y_train_pred = model.predict(dtrain)
y_test_pred = model.predict(dtest)

# 学習の課程を折れ線グラフとしてプロットする
train_metric = evals_result['train']['rmse']
plt.plot(train_metric, label='train loss')
eval_metric = evals_result['eval']['rmse']
plt.plot(eval_metric, label='eval loss')
plt.grid()
plt.legend()
plt.xlabel('rounds')
plt.ylabel('logloss')
plt.show()

# 決定係数R2でモデルの性能評価
test_score = R2(y_test, y_test_pred)
print("Train score: ", R2(y_train, y_train_pred))
print("Test score: ", test_score)

# モデルの保存
model.save_model('src/mymodel.bin')
# pickle.dump(best_model, open("src/mymodel.pkl", "wb"))
print(f"var{n} is used")
