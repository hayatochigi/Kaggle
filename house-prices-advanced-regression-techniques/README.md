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
