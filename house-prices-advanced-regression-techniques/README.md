# Overview
Kaggle Competition - [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) Challenge.
- (Multiple) Linear Regression
- Polymial Regression
- Support Vector Regression
- Random Forest Tree

# Preprocessing
pandasとscikit-learnを用いて試行錯誤

# Log
## 1st Try
|  R2 Score|  Linear  |  Polymial  |  SVR  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- |
|  train  |  0.84957  |  1.00000    |  0.73542  |  0.97807  |
|  test   |  0.85429  |  -71.93622  |  0.82955  |  0.90000  |

Polymial Regressionは典型的な過学習を示している。Random Forestは毎回、他と比べてR2 Score高い気がする。

## 2nd Try
|  R2 Score|  Linear  |  Polymial  |  SVR (linear)  |  SVR (rbf)  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- | ---- |
|  train  |  0.84957  |  1.00000    |  0.13559  |  -0.04504  |  0.97806  |
|  test   |  0.85439  |  0.38913    |  0.16839  |  -0.03856  |  0.90044  |

ZScoreによるスケーリングを実施。SVRはkernelがlinearもrbfもいまいち


## 3rd Try
KaggleへSubmit。
<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/kaggle_house_predict_1st.PNG">
</p>

## 4th Try
|  R2 Score|  Linear  |  Polymial  |  SVR (linear)  |  SVR (rbf)  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- | ---- |
|  train  |  0.95596  |  1.00000    |  0.08158  |  -0.05313  |  0.97790  |
|  test   |  -1500861377121772800.00000  |  0.70588    |  0.07970  |  -0.06164  |  0.85959  |

EDA手法を見直して、数値尺度と名義尺度で行うpreprocessingを変更。testデータに対し当てはまりがよろしくない。
ここでそういえばp値とシャピロウィルク検定を全く考慮していなかったことを思い出す。

- 人による変数ピックアップは、人のバイアスが影響する可能性がある
- 独立変数を減らしてしっかり予測できるのが良いモデル
- 過度な独立変数は汎用性がない、過学習が起きやすくなる


## 4th Try
Backward Eliminationを用いて独立変数を選択。"理論と実践から学ぶ機械学習のすべて with Python"より。
```
import statsmodels.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()X_opt = X[:, [0, 1, 3, 4, 5]]
 
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()X_opt = X[:, [0, 3, 4, 5]]
 
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()X_opt = X[:, [0, 3, 5]]
 
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()X_opt = X[:, [0, 3]]
 
X_opt = X_opt.astype(np.float64)regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
 
regressor_OLS.summary()
```
