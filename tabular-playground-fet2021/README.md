 
 DNNの構築に参考にさせていただきました。 [Training Neural Networks for price prediction with TensorFlow](https://towardsdatascience.com/training-neural-networks-for-price-prediction-with-tensorflow-8aafe0c55198)

### One-Hot Encoding + LightGBM + Optunalgb #1
```
best iteration is:
[240]	valid_0's rmse: 0.843208

RMSE mean = 0.8443752568883091

RMSE =
[0.8419209395120772, 0.8468206963707028, 0.8465763877136017, 0.8433839714573956, 0.8431742893877682]

```

### LabelEncoding + LightGBM + Optunalgb
```
best iteration is:
[496]	valid_0's rmse: 0.846404

RMSE mean = 0.8439166449466087

RMSE = 
[0.8418867235659401, 0.8459705621396664, 0.8462503548708349, 0.8426787534876693, 0.8427968306689325]
```

### One-Hot Encoding + LightGBM + Optunalgb #2
```
best iteration is:
[250]	valid_0's rmse: 0.84199

RMSE mean = 0.8436708819222328
RMSE = [0.8413491500747229, 0.8458946722871605, 0.8458234293911292, 0.8425916655314868, 0.8426954923266646]

#second challenge
RMSE mean = 0.8436708819222328
RMSE = [0.8413491500747229, 0.8458946722871605, 0.8458234293911292, 0.8425916655314868, 0.8426954923266646]
```
