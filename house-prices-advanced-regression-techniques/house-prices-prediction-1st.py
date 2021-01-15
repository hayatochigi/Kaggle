# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', 81)


# %%
# trainデータを取得、NaN値などの状況を確認
dataset = pd.read_csv('data/train.csv', sep=',')
dataset_header = dataset.columns
print(f'Raw dataset shape: {dataset.shape[0]} * {dataset.shape[1]}')

# Idは不要のため削除
dataset = dataset.drop('Id', axis=1)

# NaNチェック
# datasetから一列ずつ取り出して、nullが含まれている場合はそのカラム名を返す

for data in dataset:
    numof_null = dataset[data].isnull().sum()
    if numof_null > 0:
        # nullが占める全体の割合 (%)
        null_ratio = numof_null/dataset.shape[0] * 100

        # とりあえず試行として... 1%より小さい割合のデータセットについては削除
        if null_ratio < 1:
            dataset = dataset.dropna(subset=[data])
        #else:
            #print(f'{data} have {numof_null} NaN (ratio is {null_ratio:.2f}%)')
print(f'NaN removed dataset shape: {dataset.shape[0]} * {dataset.shape[1]}')


# %%
# NaNデータの処理

# LotFrontageのNaN値処理: NaNの場合はストリートに面していないと見なしZeroで置き換え
dataset['LotFrontage'] = dataset['LotFrontage'].fillna(0)

# Alleyは"No alley access"="NA"のため、NaN処理なし

# BsmtQualは"Basementなし"="NA"のため、NaN処理なし (BsmtCondも同様)
# Bsmt系はBasementがなければNAになるが... なぜBsmtExposureとBsmtFinType2は38で他は37?

# Garage系はそのまま。81 NaNであることは81の住宅でガレージがないことを示す
# GarageYrBltは年のデータでNaNがある。せっかくなので後ほどmedianで置換

# PoolQCは"プールなし"="NA"のため、NaN処理なし
# Fenceは"Fenceなし"="NA"のため、NaN処理なし

# MiscFeatureはその他のカテゴリ。とりあえず割愛
dataset = dataset.drop('MiscFeature', axis=1)


# %%
# Data Preprocessing
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

# dtypeが数値でないものはラベルエンコーディング
for x in dataset:
    if np.dtype(dataset[x]) == object:
        dataset[x] = label_encoder.fit_transform(dataset[x])

# GarageYrBltのNaNを補完
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
dataset['GarageYrBlt'] = imputer.fit_transform(np.reshape(dataset['GarageYrBlt'].values, (dataset['GarageYrBlt'].shape[0], 1)))[:,0]

#独立変数X, 従属変数y
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values
from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#X = scaler.fit_transform(X)

# train, testデータへ分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# %%
# (Multiple) Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
y_train_pred = regressor.predict(X_train)

# trainデータとtestデータそれぞれのR2スコアを表示する関数
def print_r2_score(y_train, y_test, y_train_pred, y_pred):
    from sklearn.metrics import r2_score
    print(f'R2 Score(train) is {r2_score(y_train, y_train_pred):.5f}')
    print(f'R2 Score(test) is {r2_score(y_test, y_pred):.5f}')

print_r2_score(y_train, y_test, y_train_pred, y_pred)


# %%
# Polymial Regression
from sklearn.preprocessing import PolynomialFeatures
polynomial_instance = PolynomialFeatures(degree = 2)
X_poly_train = polynomial_instance.fit_transform(X_train)
X_poly_test = polynomial_instance.fit_transform(X_test)

regressor = LinearRegression()
regressor.fit(X_poly_train, y_train)
y_train_pred = regressor.predict(X_poly_train)
y_pred = regressor.predict(X_poly_test)

print_r2_score(y_train, y_test, y_train_pred, y_pred)


# %%
# SVR
from sklearn.svm import SVR
svr_regressor = SVR(kernel='linear')
svr_regressor.fit(X_train, y_train)
y_pred = svr_regressor.predict(X_test)
y_train_pred = svr_regressor.predict(X_train)

print_r2_score(y_train, y_test, y_train_pred, y_pred)


# %%
# Random Forest
from sklearn.ensemble import RandomForestRegressor
rndm_regressor = RandomForestRegressor(n_estimators = 100, random_state=0)
rndm_regressor.fit(X_train, y_train)
y_pred = rndm_regressor.predict(X_test)
y_train_pred = rndm_regressor.predict(X_train)

print_r2_score(y_train, y_test, y_train_pred, y_pred)


