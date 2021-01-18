# Overview
Kaggle Competition - [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview) Challenge.
- Logistic Classification
- K-Nearest Neighbors
- Support Vector Machine
- Naive Bayes
- Random Forest Classification

LightGBMは、ある程度基本のアルゴリズムで結果が出てからトライ。

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

Add Standard Scaling

## 3rd Try
[Titanic Tutorial](https://www.kaggle.com/alexisbcook/titanic-tutorial)に倣って、Featuresを減らしてみる。1st submission Score 0.76555から0.77511へ改善。Featuresはあればあるほど良いわけではない...?
<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/kaggle_titanic_2nd_result.PNG">
</p>

## 4th Try
|      |  Logistic  |  K-Nearest  |  SVM  |  Naive Bayes  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- |---- |
| ConfusionMatrix|  [[122  14]<br>[ 30  57]]  |  [[128   8]<br>[ 49  38]]  |  [[119  17]<br>[ 30  57]]  |  [[118  18]<br>[ 27  60]]  | [[117  19]<br>[ 25  62]]  |
| Accuracy       |  0.80269    |  0.74439  |  0.78924  |  0.79821  |  0.80269  |

性別について、LabelEncoderからget_dummiesによるOneHotEncodingへ変更。劇的な改善、というわけにはいかなかった。

## 5th Try
Grid Searchを用いてRandomForestClassifierのハイパーパラメータを調整。
```
from sklearn.model_selection import GridSearchCV
grid_parameters = [
    {'n_estimators': [1, 2, 5, 10, 100, 1000], 
    'criterion': ['gini', 'entropy'],
    'max_features': [1, 2, 5, 10, 20],
    'min_samples_split': [1, 2, 5, 10, 20],
    'min_samples_leaf': [1, 2, 5, 10, 20],
    'bootstrap': [True, False],
    }
]

grid_search = GridSearchCV(RandomForestClassifier(), grid_parameters, cv=5, scoring='accuracy', n_jobs = -1)
grid_search.fit(X_train, y_train)
grid_search.best_params_
```

~~後でsubmitして、結果を確認すること。~~ --> 6thへ。。。

## 6th Try
Grid Search + FeaturesとEDAの見直し。何でもかんでもscaleすればよいってものではないみたい。名義尺度のscalingは止めて、AgeとFareのみを処理してみる。
|      |  Logistic  |  K-Nearest  |  SVM  |  Naive Bayes  |  Random Forest  |
| ---- | ---- | ---- |---- | ---- |---- |
| ConfusionMatrix|  [[115  14]<br>[ 25  69]]  |  [[122   7]<br>[ 51  43]]  |  [[112  17]<br>[ 26  68]]  |  [[118  11]<br>[ 34  60]]  | [[121   8]<br>[ 30  64]]  |
| Accuracy       |  0.82511    |  0.73991  |  0.80717  |  0.79821  |  0.82960  |

submissionの結果は0.75119...
併せてFamily Featureを、元のSibSpとParchに戻してみる。submissionの結果は0.78468でベストを更新。
