 
 DNNの構築に参考にさせていただきました。 [Training Neural Networks for price prediction with TensorFlow](https://towardsdatascience.com/training-neural-networks-for-price-prediction-with-tensorflow-8aafe0c55198)

### One-Hot Encoding + LightGBM + Optunalgb #1
```
best iteration is:
[240]	valid_0's rmse: 0.843208

RMSE mean = 0.8443752568883091

RMSE =
[0.8419209395120772, 0.8468206963707028, 0.8465763877136017, 0.8433839714573956, 0.8431742893877682]

```

### LabelEncoding + RobustScaler + LightGBM + Optunalgb
```
best iteration is:
[496]	valid_0's rmse: 0.846404

RMSE mean = 0.8439166449466087

RMSE = 
[0.8418867235659401, 0.8459705621396664, 0.8462503548708349, 0.8426787534876693, 0.8427968306689325]
```

### One-Hot Encoding + RobustScaler + LightGBM + Optunalgb #2
```
best iteration is:
[250]	valid_0's rmse: 0.84199

RMSE mean = 0.8436708819222328
RMSE = [0.8413491500747229, 0.8458946722871605, 0.8458234293911292, 0.8425916655314868, 0.8426954923266646]

#second challenge
RMSE mean = 0.8436708819222328
RMSE = [0.8413491500747229, 0.8458946722871605, 0.8458234293911292, 0.8425916655314868, 0.8426954923266646]
```

### One-Hot Encoding + StandardScaler + LightGBM + Optunalgb
```
best iteration is:
[255]	valid_0's rmse: 0.847465

RMSE mean = 0.844401165812503
RMSE = [0.8423521171301173, 0.8463045408944343, 0.8466526687737727, 0.8434694053761003, 0.8432270968880907]
```

### One-Hot Encoding + NoScaler + LightGBM + Optunalgb
```
best iteration is:
[338]	valid_0's rmse: 0.840835
RMSE mean = 0.8438536808283884
RMSE = [0.8419508921091942, 0.8456143349146623, 0.846160590374425, 0.842607144534302, 0.8429354422093588]
```

### One-Hot Encoding + RobustScaler + Optuna
```
LightGBM Best is trial 26 with value: 0.840814232174324
{'num_leaves': 87, 'max_depth': 9, 'learning_rate': 0.009582240516938432, 'n_estimators': 2553, 'reg_alpha': 0.037580598353005736, 'reg_lambda': 0.02686007922451687, 'colsample_bytree': 0.5534542046480458}
RMSE mean = 0.843631059031493
RMSE = [0.8416875412520916, 0.8454876743541762, 0.8459821874055197, 0.8427222174572888, 0.8422756746883893]

XGBoost Best is trial 16 with value: 0.8414031616263706
{'eta': 0.6967322281466614, 'gamma': 0.0036942646535044962, 'max_depth': 6, 'sub_sample': 0.553569633282626, 'colsample_bytree': 0.554663669927102, 'lambda': 0.001701369247469206, 'alpha': 0.009630419498745284, 'learning_rate': 0.03446986865236482, 'n_estimators': 603}
```
