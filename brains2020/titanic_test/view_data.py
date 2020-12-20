from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import seaborn as sns
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def normalize(ds):
    max_num = ds.max()
    min_num = ds.min()
    return (ds - min_num) / (max_num - min_num) + min_num


df_train = pd.read_csv("./data/train.csv")
df_train = df_train.replace({"Sex": {"male": 0, "female": 1}})
df_train["Fare"] = normalize(df_train["Fare"])
x_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
y_column = ['Survived']
pair = df_train[x_columns+y_column]
print(pair.head())
# pg = sns.pairplot(pair, hue='Survived')
# pg.savefig("pair_plot.png")


train_x, valid_x, train_y, valid_y = train_test_split(df_train[x_columns], df_train[y_column], test_size=0.33, random_state=0)

lgb_params = {"objective": "binary",
              "metric": "binary_logloss",
              "boosting_type": "gbdt",
              "num_iterations": 500,
              "min_data_in_leaf": 9
              }

lgb_train = lgb.Dataset(train_x, train_y)
lgb_eval = lgb.Dataset(valid_x, valid_y, reference=lgb_train)
model = lgb.train(lgb_params, lgb_train, valid_sets=lgb_eval,
                  num_boost_round=500,
                  verbose_eval=10,
                  early_stopping_rounds=20)
# predict
pred_y = model.predict(valid_x, num_iteration=model.best_iteration)
pred_y_bi = np.where(pred_y < 0.5, 0, 1)
print(accuracy_score(valid_y, pred_y_bi))
