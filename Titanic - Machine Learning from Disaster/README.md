# Overview
Kaggle Competition - [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview) Challenge.
- Logistic Classification
- K-Nearest Neighbors
- Support Vector Machine
- Naive Bayes
- Random Forest Classification

# Log
## 1st Try
|      |  Logistic  |  K-Nearest  |  SVM  |  Naive Bayes  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- |---- |
| ConfusionMatrix|  [[120  17]<br>[ 26  60]]  |  [[121  16]<br>[ 46  40]]  |  [[121  16]<br>[ 30  56]]  |  [[111  26]<br>[ 22  64]]  | [[121  16]<br>[ 37  49]]  |
| Accuracy       |  0.80717    |  0.72197  |  0.79372  |  0.78475  |  0.76233  |

Features Scalingなし。

## 2nd Try
|      |  Logistic  |  K-Nearest  |  SVM  |  Naive Bayes  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- |---- |
| ConfusionMatrix|  [[122  24]<br>[ 20  57]]  |  [[136  10]<br>[ 27  50]]  |  [[128  18]<br>[ 21  56]]  |  [[122  24]<br>[ 21  56]]  | [[131  15]<br>[ 36  41]]  |
| Accuracy       |  0.80269    |  0.83408  |  0.82511  |  0.79821  |  0.77130  |

Standard Scaling

## 3rd Try
[Titanic Tutorial](https://www.kaggle.com/alexisbcook/titanic-tutorial)に倣って、Featuresを減らしてみる。
<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/kaggle_titanic_2nd_result.PNG">
</p>
