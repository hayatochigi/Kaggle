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

以下メモ
- 人による変数ピックアップは、人のバイアスが影響する可能性がある
- 独立変数を減らしてしっかり予測できるのが良いモデル
- 過度な独立変数は汎用性がない、過学習が起きやすくなる


## 5th Try
- [Stacked Regressions : Top 4% on LeaderBoard](https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard/notebook#Modelling) EDAについて非常に参考になった。
- [Comprehensive data exploration with Python](https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python) モデル構築についてはこちら。  
Grid Searchなどモデルのチューンを全く指定ない状態で、結構ランキングをあげることができた。
<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/kaggle_house_1st_stacked_model.png">
</p>

